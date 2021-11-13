from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html', {'title': 'Home page'})
    
def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About page'})
