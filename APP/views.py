from django.shortcuts import render
from blocgs.models import Category,Blog

def home(request):
    
    featured_post=Blog.objects.filter(is_featured=True, satus='Published').order_by('-updated_at')
    posts=Blog.objects.filter(is_featured=False,satus='Published')
    context={
        
        'featured_post':featured_post,
        'posts':posts,
    }
    return render(request,"home.html",context)         