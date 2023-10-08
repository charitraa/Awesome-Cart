from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="ShopeHome"),
    path('shop/about/', views.about, name="about"),
    path('shop/contact/', views.contact, name="contact"),
    path('shop/tracker/', views.tracker, name="tracker"),
    path('shop/search/', views.search, name="search"),
    path('shop/productview/<int:myid>', views.productview, name="productview"),
    path('shop/checkout/', views.checkout, name="checkout"),

]
