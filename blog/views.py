from django.shortcuts import render
from .models import Post

def blog_view(requests):
    posts=Post.objects.filter(status=1)
    context={'posts':posts}
    return render(requests,'blog/blog-home.html',context)

def single_block(requests):
    return render(requests,'blog/blog-single.html')
def test_view(requests):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(requests,'test.html',context)
