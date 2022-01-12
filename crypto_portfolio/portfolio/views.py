from django.shortcuts import render
from django.views.generic import ListView
from numpy import unique
from . import portfolio_utils as pu
from .forms import AssetForm
from django.http import HttpResponseRedirect
from .models import Asset, Portfolio

def home(request):
    data = pu.make_request()
        
    if request.GET:
        id = request.GET.get('id')
        graph = pu.get_plot(pu.get_ml_data(id), id, 1)
    else:
        id = 'bitcoin'
        graph = pu.get_plot(pu.get_ml_data(id), id, 1)
    return render(request, 'portfolio/home.html', context={ 'api_data':data, 'name':id, 'graph': graph })

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
                          date = form.cleaned_data['date'],
                          coin_id = form.cleaned_data['id'],
                          name = form.cleaned_data['id'].capitalize()
                          )
            asset.save()
            user_assets = Asset.objects.filter(portfolio=current_portfolio)
            return HttpResponseRedirect('../../portfolio/profile')

    user_data = pu.add_data(user_assets, data)
    unique_user_data = []
    for asset1 in user_data:
        found = False
        for asset2 in unique_user_data:
            if asset1['id'] == asset2['id']:
                found = True
                break
        if not found:
            unique_user_data.append(asset1)
        


    balance_coin_id = ''
    if request.GET:
        balance_coin_id = request.GET.get('balance')
    else:
        for asset in user_assets:
            balance_coin_id = asset.coin_id      

    print(balance_coin_id)

    if balance_coin_id != '':
        total = pu.total_balance(user_assets.filter(coin_id=balance_coin_id), balance_coin_id)
        plot = pu.get_balance_plot(total, balance_coin_id)
        return render(request, 'portfolio/portfolio.html', context={ 'assets': user_assets, 'api_data': data, 'user_data': user_data, 'unique_user_data': unique_user_data, 'plot': plot})
    else:
        return render(request, 'portfolio/portfolio.html', context={ 'assets': user_assets, 'api_data': data, 'unique_user_data': unique_user_data, 'user_data': user_data})

    
    

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
