from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(requ):
    p="10"
    return render(requ,"personal/home.html",{"p":p})

def contact(request):
    return render(request, 'personal/basic.html', dict(content=['Please email me','pranielgurung@gmail.com']))