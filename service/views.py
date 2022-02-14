from django.shortcuts import render, redirect
from .forms import SignupForm, ServiceProviderForm, SellProductForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from  django.utils.decorators import method_decorator
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


@login_required
def service_provider_form(request):
    form = ServiceProviderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('service:providers')

    return render(request, 'providers.html', {'form': form})


@login_required
def provider_list(request):
    provider = ServiceProvider.objects.all()
    return render(request, 'agrovet.html', {'providers': provider})


@login_required
def market(request):
    return render(request, 'market.html')


@login_required
def sell_product(request):
    form = SellProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('service:home')
    return render(request, 'sell.html', {'form': form})







