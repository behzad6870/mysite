from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index_view(requests):
    return render(requests,'website/index.html')

def about_view(requests):
   return render(requests,'website/about.html')


def contact_view(requests):
    return render(requests,'website/contact.html')

def test_view(requests):
    context={'name':'behzad','last_name':'mirza'}
    return render(requests,'website/test.html',context)




