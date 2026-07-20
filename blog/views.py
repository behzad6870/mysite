from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

def blog_view(requests):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    context={'posts':posts}
    return render(requests,'blog/blog-home.html',context)

def single_block(requests,pid):
    posts=Post.objects.filter(status=1,published_date__lte=timezone.now())
    #post=get_object_or_404(posts,pk=pid)
    post=get_object_or_404(Post,pk=pid,status=1)
    if get_object_or_404(Post,pk=pid):
        post.counted_views+=1
        post.save()
    list=[]  
    for p in posts:
        list.append(p.id)  
    if get_object_or_404(Post,pk=pid):
        if pid+1 in list:
            post_next=Post.objects.get(id=pid+1)
        else:
            post_next=None    
        if pid-1 in list:  
            post_prev=Post.objects.get(id=pid+-1)  
        else:
            post_prev=None    
                
    context={'post':post,'post_next':post_next,'post_prev':post_prev}
    return render(requests,'blog/blog-single.html',context)
def test_view(requests,pid):
    #post=Post.objects.get(id=pid)
    post=get_object_or_404(Post,pk=pid)
    if get_object_or_404(Post,pk=pid):
        post.counted_views+=1
        post.save()
    context={'post':post}
    return render(requests,'test.html',context)
