from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello ')


def New(request):
    return render(request, 'Blog/index.html')