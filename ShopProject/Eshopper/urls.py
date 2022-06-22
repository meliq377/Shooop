from django.urls import path
from .views import *

app_name = 'Eshopper'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', index, name='home'),
    path('category/<str:slug>', get_category, name='get_category'),
    path('brand/<str:slug>', get_brand, name='get_brand'),
    path('product/<str:slug>', detail_product, name='detail_product'),
    path('ajax_price_range/', ajax_price_range, name='ajax_price_range'),
]