from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello")

def blog(request):
    return HttpResponse("blog")

def contact(request):
    return HttpResponse("contact")