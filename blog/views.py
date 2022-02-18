# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK

from blog.models import Post, Comment
from .forms import PostModelForm, PostForm, CommentModelForm


@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    # email = request.data.get('email')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)

    # 여기서 authenticate로 유저 validate
    user = authenticate(username=username, password=password)
    print('>>>> user ', user)

    if not user:
        return Response({'error': 'Invalid credentials'}, status=HTTP_404_NOT_FOUND)

    # user 로 토큰 발행
    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key}, status=HTTP_200_OK)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


# 댓글 등록
def add_comment_tp_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = CommentModelForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


# 글 삭제
@login_required
def post_remove(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('everyPost')


# 글 수정(model Form) 사용
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostModelForm(instance=post)
    return render(request, 'blog/post_edit.html', {'postform': form})


# 글 등록(form 사용)
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            cleaned_data_dict = form.cleaned_data
            post = Post.objects.create(
                author=request.user,
                title=cleaned_data_dict['title'],
                text=cleaned_data_dict['text'],
                published_date=timezone.now()
            )
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'postform': form})


# 글 등록(modelform 사용)
def post_new_modelform(request):
    if request.method == 'POST':
        post_form = PostModelForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        post_form = PostModelForm()
    return render(request, 'blog/post_edit.html', {'postform': post_form})


# 글 상세정보
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post_key': post})


# 글 목록 Pagination 이용
# www.codingfactory.net
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(posts, 2)
    try:
        # page number(페이지번호)를 화면에서 쿼리스트링으로 전달받는다
        page_number = request.GET.get('page')
        # 전달받은 페이지번호로 Page객체생성
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'post_list': page})


# 글 목록
def post_list_first(request):
    my_name = '장고웹프레임워크'
    http_method = request.method
    # return HttpResponse('''
    #     <h2>Welcome {name}</h2>
    #     <p>Http Method : {method}</p>
    #     <p>Http headers user-agent  : {header}</p>
    #     <p>Http Path : {mypath}</p>
    # '''.format(name=my_name, method=http_method, header=request.headers['user-agent'], mypath=request.path)
    #                     )

    # return render(request, 'blog/post_list.html')

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'post_list': posts})
