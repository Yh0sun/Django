# Create your views here.


from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone

from customer.forms import CustomerForm
from customer.models import Customer


def ctm_new(request):
    if request.method == 'POST':
        ctm = CustomerForm(request.POST)
        if ctm.is_valid():
            cleaned_data_dict = ctm.cleaned_data
            ctm = Customer.objects.create(
                name=cleaned_data_dict['name'],
                birthdate=cleaned_data_dict['birthdate'],
                email=cleaned_data_dict['email'],
                gender=cleaned_data_dict['gender'],
            )
            return redirect('ctm_detail', pk=ctm.pk)
    else:
        ctm = CustomerForm()
    return render(request, 'customer/ctm_edit.html', {'ctm': ctm})


def ctm_detail(request, pk):
    ctm = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer/ctm_detail.html', {'ctm_key': ctm})


def ctm_list(request):
    name = 'customers'
    http_method = request.method
    # return HttpResponse('''
    # <h1> ~ {name} ~ </h1>
    #  <p>Http Method : {method}</p>
    # <p>Http headers user-agent  : {header}</p>
    # <p>Http Path : {mypath}</p>
    # '''.format(name=name, method=http_method, header=request.headers['user-agent'], mypath=request.path)
    #                     )

    customers = Customer.objects.all()
    return render(request, 'customer/ctm_list.html', {'ctm_list': customers})
