from django.shortcuts import render, get_object_or_404
from .models import Blog

def homepage(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/homepage.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context)
