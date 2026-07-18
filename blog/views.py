from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

def blog_view(requests):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    context={'posts':posts}
    return render(requests,'blog/blog-home.html',context)

def single_block(requests,pid):
    post=get_object_or_404(Post,pk=pid)
    if get_object_or_404(Post,pk=pid):
        post.counted_views+=1
        post.save()
    context={'post':post}
    return render(requests,'blog/blog-single.html',context)
def test_view(requests,pid):
    #post=Post.objects.get(id=pid)
    post=get_object_or_404(Post,pk=pid)
    if get_object_or_404(Post,pk=pid):
        post.counted_views+=1
        post.save()
    context={'post':post}
    return render(requests,'test.html',context)
