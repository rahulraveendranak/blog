from django.shortcuts import render,HttpResponse
from blogs.models import blog
# Create your views here.
def home(request):
    return render(request,'index.html')

def blog(request):
    blogs = blog.objects.all()
    context = {'blogs': blogs}
    return render(request,'bloghome.html', context)

def blogpost(request,slug):
    return HttpResponse(f"you are viewing{slug}")

def contact(request):
    return render(request,'contact.html')

def search(request):
    return render(request,'search.html')