from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('about-us/', views.AboutUsTemplateView.as_view(), name='about_us'),
    path('contact/', views.ContactTemplateView.as_view(), name='contact'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('account/', views.AccountTemplateView.as_view(), name='account'),
    path('blog/', views.BlogTemplateView.as_view(), name='blog'),
    path('gallery/', views.GalleryTemplateView.as_view(), name='gallery'),
    path('services/', views.ServicesTemplateView.as_view(), name='services'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('market/', views.market, name='market'),
    path('sell-product/', views.sell_product, name='sell'),
    path('search-product/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('article-post/', views.article_form, name='article'),
    path('market-home/', views.market_home, name='market_home'),
    path('search-home/', views.search_home, name='search_home'),

    path('product/<int:product_id>/', views.product_details, name='product_details'),
]

handler404 = "service.views.page_not_found"