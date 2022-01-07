from django.shortcuts import render
from django.views.generic import ListView
from . import portfolio_utils as pu
from .forms import AssetForm
from .utils import *
from django.http import HttpResponseRedirect
from .models import Asset, Portfolio

def home(request):
    current_user = request.user

    try:
        current_portfolio = Portfolio.objects.get(user=current_user)
        user_assets = Asset.objects.filter(portfolio=current_portfolio)
        for asset in user_assets:
                asset.graph = pu.get_plot(pu.get_ml_data(asset.coin_id))
    except:
        current_portfolio = Portfolio.objects.create(user=current_user)
        user_assets = {}

    for asset in user_assets:
        asset.graph = pu.get_plot(pu.get_ml_data(asset.coin_id))
    
    return render(request, 'portfolio/home.html', context={ 'assets': user_assets})

def profile(request):
    current_user = request.user
    
    try:
        current_portfolio = Portfolio.objects.get(user=current_user)
        user_assets = Asset.objects.filter(portfolio=current_portfolio)
    except:
        current_portfolio = Portfolio.objects.create(user=current_user)
        user_assets = {}


    data = pu.make_request()

    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = Asset(amount = form.cleaned_data['amount'],
                          price = form.cleaned_data['price'], 
                          portfolio = current_portfolio,
                          coin_id = form.cleaned_data['id'],
                          name = form.cleaned_data['id'].capitalize()
                          )
            asset.save()
            user_assets = Asset.objects.filter(portfolio=current_portfolio)
            return HttpResponseRedirect('../../portfolio/profile') #why does it work?!

    return render(request, 'portfolio/portfolio.html', context={ 'assets': user_assets, 'api_data': data})

def form(request):
    if request.GET:
        id = request.GET.get('id')
        data = pu.make_request()
        form = AssetForm()
        form = AssetForm(initial={'id': id})
        return render(request, 'portfolio/form.html', context= {'api_data': data, 'form': form})
    else:
        return render(request, 'portfolio/portfolio.html')

def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About page'})
