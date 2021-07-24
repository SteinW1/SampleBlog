from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article

# Create your views here.
def articles():
    articles = Article.objects.all()
    return articles

class ArticleView(DetailView):
    model = Article

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        pass
        
class ArticleCreateView(CreateView):
    model = Article
    
class ArticleUpdateView(UpdateView):
    model = Article

class ArticleDeleteView(DeleteView):
    model = Article