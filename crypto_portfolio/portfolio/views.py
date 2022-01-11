from django.shortcuts import render
from django.views.generic import ListView
from . import portfolio_utils as pu
from .forms import AssetForm
from django.http import HttpResponseRedirect
from .models import Asset, Portfolio

def home(request):
    data = pu.make_request()
        
    if request.GET:
        id = request.GET.get('id')
        graph = pu.get_plot(pu.get_ml_data(id), 1)
    else:
        id = 'bitcoin'
        graph = pu.get_plot(pu.get_ml_data(id), 1)
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
    total = pu.total_balance(user_assets.filter(coin_id='tether'), 'tether')

    plot = pu.get_balance_plot(total)

    #print(user_assets.values('coin_id'))
    for asset in user_assets.all():
        for elem in data:
            if asset.coin_id == elem['id']:
                pass
                #print(asset.coin_id)


    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            #removed price from form
            for elem in data:
                if elem['id'] == form.cleaned_data['id']:
                    _price = elem['current_price']

            asset = Asset(amount = form.cleaned_data['amount'],
                          price = _price, 
                          portfolio = current_portfolio,
                          coin_id = form.cleaned_data['id'],
                          name = form.cleaned_data['id'].capitalize()
                          )
            asset.save()
            user_assets = Asset.objects.filter(portfolio=current_portfolio)

            return HttpResponseRedirect('../../portfolio/profile') 
    user_data = pu.add_data(user_assets, data)
    return render(request, 'portfolio/portfolio.html', context={ 'assets': user_assets, 'api_data': data, 'user_data': user_data, 'plot': plot})
     #       return HttpResponseRedirect('../../portfolio/profile') #why does it work?!
#
   # return render(request, 'portfolio/portfolio.html', context={ 'assets': user_assets, 'api_data': data, })
#>>>>>>> 5018676d1b0c61d968dde09a22c2c94a8981e453

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
