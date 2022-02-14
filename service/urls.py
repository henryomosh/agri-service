from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('about_us/', views.AboutUsTemplateView.as_view(), name='about_us'),
    path('contact/', views.ContactTemplateView.as_view(), name='contact'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('account/', views.AccountTemplateView.as_view(), name='account'),
    path('blog/', views.BlogTemplateView.as_view(), name='blog'),
    path('gallery/', views.GalleryTemplateView.as_view(), name='gallery'),
    path('services/', views.ServicesTemplateView.as_view(), name='services'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('providers/', views.service_provider_form, name='providers'),
    path('agrovets/', views.provider_list, name='agrovets'),
    path('market/', views.market, name='market'),
    path('sell_product/', views.sell_product, name='sell'),
]