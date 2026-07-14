from django.shortcuts import render

def blog_view(requests):
    return render(requests,'blog/blog-home.html')

def single_block(requests):
    return render(requests,'blog/blog-single.html')
