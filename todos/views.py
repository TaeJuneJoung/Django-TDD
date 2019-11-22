from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    # return render(request, 'home.html')
    return HttpResponse('<html><title>TDD Python</title></html>')