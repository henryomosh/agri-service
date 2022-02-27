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
    path('articles/', views.articles_list, name='articles'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('user-product-details/<int:product_id>/', views.user_product_details, name='user_product_details'),
    path('user-product-edit/<int:product_id>/', views.edit_user_product, name='edit_product'),
    path('user-product-delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('article-details/<int:article_id>/', views.article_details, name='article details'),
    path('article-details/', views.ArticleD.as_view(), name='articles_det'),
    path('product-details/<int:product_id>/', views.home_product_details, name='home_product_details'),

]

handler404 = "service.views.page_not_found"