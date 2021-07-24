from django.shortcuts import render
from articles.views import articles
# Create your views here.
def home(request):
    
    context = {
        "view_name":"home",
        "articles": articles(),
    }
    
    
    
    return render(request, 'main/home.html', context)