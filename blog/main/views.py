from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "view_name":"home",
    }
    return render(request, 'main/home.html', context)