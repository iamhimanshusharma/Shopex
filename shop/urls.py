from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('shop_registration', views.shop_registration, name="shop_registration"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('profile', views.profile, name="profile"),
    path('settings', views.settings, name="settings"),
    path('add_products', views.add_products, name="add_products"),
    path('picture_change', views.picture_change, name="picture_change"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)