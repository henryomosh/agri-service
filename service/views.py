from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from .models import *


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class AboutUsTemplateView(TemplateView):
    template_name = 'about_us.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


class AccountTemplateView(TemplateView):
    template_name = 'account.html'


class BlogTemplateView(TemplateView):
    template_name = 'blog_list.html'


class GalleryTemplateView(TemplateView):
    template_name = 'gallery.html'


class ServicesTemplateView(TemplateView):
    template_name = 'services.html'


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('service:home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([username, password]):
            return render(request, 'login.html', {'error_message': 'You must provide username and password !'})
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('service:home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password !'})

    return render(request, 'login.html')


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'


def log_out(request):
    logout(request)
    return redirect('service:login')


def market(request):
    products = Sell.objects.all()
    return render(request, 'market.html', {'products': products})


def sell_product(request):
    form = SellProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        sell = form.save(commit=False)
        sell.seller = request.user
        sell.save()
        return redirect('service:market')

    return render(request, 'sell.html', {'form': form})


def product_details(request, product_id):
    product = get_object_or_404(Sell, pk=product_id)
    return render(request, 'product_details.html', {'product': product})


def search(request):
    if request.method == 'GET':
        product = request.GET.get('product_name')
        query_list = Sell.objects.filter(product_name__contains=product)
        return render(request, 'search.html', {'query_list': query_list})

    return redirect('service:market')


def profile(request):
    return render(request, 'profile.html')


def article_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
            article.save()
            return redirect('service:home')
    else:
        form = ArticleForm()
    return render(request, 'article.html', {'form': form})


def market_home(request):
    products = Sell.objects.all()
    return render(request, 'market_home.html', {'products': products})


def search_home(request):
    if request.method == 'GET':
        product = request.GET.get('product_name')
        query_list = Sell.objects.filter(product_name__contains=product)
        return render(request, 'search_home.html', {'query_list': query_list})

    return redirect('service:market_home')


def page_not_found(request, exception):
    return render(request, 'status.html', status=404)

