from django.urls import path
from . import views


urlpatterns = [
    path('list', views.productlist, name = 'product_list'),
    path('detail/<post_id>', views.productdetails),
    path('about/', views.about),
    path('contact/', views.contact),
    path('home/', views.index),
    path('register/', views.register),
    path('login/', views.user_login),
    path('profile/',views.profile),
    path('signout/', views.signout),
    path('changepass/',views.changepass)

]