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
        return redirect('service:profile')

    return render(request, 'sell.html', {'form': form})


def product_details(request, product_id):
    product = get_object_or_404(Sell, pk=product_id)
    images = ProductImage.objects.filter(name_id__exact=product_id)

    return render(request, 'product_details.html', {'product': product, 'images': images})


def search(request):
    if request.method == 'GET':
        product = request.GET.get('product_name')
        query_list = Sell.objects.filter(product_name__contains=product)
        return render(request, 'search.html', {'query_list': query_list})

    return redirect('service:market')


def profile(request):
    products = Sell.objects.filter(seller=request.user)
    return render(request, 'profile.html', {'products': products})


def article_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        image_form = ImageForm(request.POST, request.FILES)
        images = request.FILES.getlist('image')
        if form.is_valid() and image_form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
            article.save()
            for img in images:
                instance = ArticleImage(name=article, image=img)
                instance.save()
            return redirect('service:home')
    else:
        form = ArticleForm()
        image_form = ImageForm()
    return render(request, 'article.html', {'form': form, 'image_form': image_form})


def market_home(request):
    products = Sell.objects.all()
    return render(request, 'market_home.html', {'products': products})


def search_home(request):
    if request.method == 'GET':
        product = request.GET.get('product_name')
        query_list = Sell.objects.filter(Q(product_name__contains=product)|Q(location__contains=product))
        return render(request, 'search_home.html', {'query_list': query_list})

    return redirect('service:market_home')


def page_not_found(request, exception):
    return render(request, 'status.html', status=404)


def articles_list(request):
    articles = Article.objects.all()
    images = ArticleImage.objects.filter(name__owner_id=object_ids(User.objects.all()))
    return render(request, 'holder.html', {'articles': articles, 'images': images})


def user_product_details(request, product_id):
    product = get_object_or_404(Sell, pk=product_id, )
    images = ProductImage.objects.filter(name_id__exact=product_id)
    if request.method == 'POST':
        image_form = ProductImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            for img in request.FILES.getlist('image'):
                instance = ProductImage(name=product, image=img)
                instance.save()
    else:
        image_form = ProductImageForm()
    return render(request, 'user_product_details.html', {'product': product, 'images': images, 'image_form': image_form})


def edit_user_product(request, product_id):
    message = ''
    product = get_object_or_404(Sell, pk=product_id)
    if request.method == 'POST':
        form = SellProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            message = 'Changes Saved ..'
    else:
        form = SellProductForm(instance=product)
    return render(request, 'user_product_form.html', {'form': form, 'product': product, 'message': message})


def delete_product(request, product_id):
    product = get_object_or_404(Sell, pk=product_id)
    product.delete()
    return redirect('service:profile')


def article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article_details.html', {'article': article})


class ArticleD(TemplateView):
    template_name = 'article_details.html'


def home_product_details(request, product_id):
    product = get_object_or_404(Sell, pk=product_id)
    images = ProductImage.objects.filter(name_id__exact=product_id)
    return render(request, 'home_product_details.html', {'product': product, 'images': images})


def object_ids(request):
    for object_id in request:
        obj = object_id.pk
        return obj


