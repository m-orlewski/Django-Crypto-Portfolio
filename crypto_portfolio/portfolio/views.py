from django.shortcuts import render
from django.views.generic import ListView
from . import portfolio_utils as pu
from .utils import *

from .models import Asset, Portfolio

def home(request): 
    return render(request, 'portfolio/home.html')

def profile(request):
    current_user = request.user
    
    try:
        current_portfolio = Portfolio.objects.get(user=current_user)
        user_assets = Asset.objects.filter(portfolio=current_portfolio)
    except:
        user_assets = {}

    data = pu.make_request()

    chart = get_plot([1,2,3], [1,4,9])

    return render(request, 'portfolio/portfolio.html', context={ 'assets': user_assets, 'api_data': data, 'chart': chart})

def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About page'})
