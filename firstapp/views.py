from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.





def home(request):
    content = {
        'post':Post.objects.all()
    }
    
    return render(request,'blog/home.html',content)


def about(request):
   
    return render(request,'blog/about.html')


@login_required
def footballers(request):
    return render(request,'blog/footballers.html')