from django.shortcuts import render
from django.views.generic import ListView
from . import portfolio_utils as pu

from .models import Asset, Portfolio

def home(request): 
    return render(request, 'portfolio/home.html')

def profile(request):
    current_user = request.user
    current_portfolio = Portfolio.objects.get(user=current_user)
    user_assets = Asset.objects.filter(portfolio=current_portfolio)
    return render(request, 'portfolio/portfolio.html', context={ 'assets': user_assets})

def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About page'})
