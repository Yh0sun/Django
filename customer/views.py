from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ctm_list(request):
    name = 'customers'
    http_method = request.method
    return HttpResponse('''
    <h1> ~ {name} ~ </h1>
     <p>Http Method : {method}</p>
    <p>Http headers user-agent  : {header}</p>
    <p>Http Path : {mypath}</p>
    '''.format(name=name, method=http_method, header=request.headers['user-agent'], mypath=request.path)
                        )


