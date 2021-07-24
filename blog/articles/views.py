from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.
def articles():
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    ordering = ['-date_posted']
    paginate_by = 1

    #return render(request, 'articles/articles.html',context)

class ArticleView(DetailView):
    model = Article

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        pass
        
#TODO:
#   def article post
#   def article delete
#   def article update