from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('lk', views.lk),
    path('portfolio-details.html', views.portfolio),
    path('inner-page.html', views.inner),
    path('index.html', views.index),
    path('/accounts/login/index.html', views.index),
    path('/accounts/login/portfolio-details.html', views.portfolio),
    path('accounts/login/index.html', views.index),
]
