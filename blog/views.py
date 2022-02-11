from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def post_list(request):
    my_name = '장고웹프레임워크'
    http_method = request.method
    return HttpResponse('''
        <h2>Welcome {name}</h2>
        <p>Http Method : {method}</p>
        <p>Http headers user-agent  : {header}</p>
        <p>Http Path : {mypath}</p>
    '''.format(name=my_name, method=http_method, header=request.headers['user-agent'], mypath=request.path)
                        )

