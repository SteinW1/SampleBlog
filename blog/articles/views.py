from django.shortcuts import render
from django.views.generic import ListView
from .models import Articles

# Create your views here.
def articles():
    model = Article
    template_name = 'articles/articles.html'
    context_object_name = 'articles'
    ordering = ['-date_posted']
    paginate_by = 1

    #return render(request, 'articles/articles.html',context)

class ArticleView(DetailView):
    model = Articles

class ArticleListView(ListView):
    model = Articles
    template = '' # template not added yet
    context_object_name = 'articles'
    paginate_by = 4

    def get_context_data(**kwargs):
        

# def article post
# def article delete
# def article update