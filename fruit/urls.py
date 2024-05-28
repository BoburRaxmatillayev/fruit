from .views import HomeView,ShopDetailView,ContactView,shop_view,add_comment

from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
    path('shop/<slug:slug>/', ShopDetailView.as_view(),name="detail-page"),
    path('shop/',shop_view,name="shop-page"),
    path("contact/",ContactView.as_view(),name="contact-page"),
    path('add_comment/', add_comment, name='add_comment')
]