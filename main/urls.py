from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('lk', views.lk),
    path('portfolio-details.html', views.portfolio),
    path('inner-page.html', views.inner),
    path('index.html', views.index),
    path('accounts/login/portfolio-details.html', views.portfolio),
    path('accounts/login/index.html', views.index),
    path('accounts/logout/index.html', views.index),
    path('accounts/signup/index.html', views.index),
    path('accounts/profile/', views.index),
    path('accounts/confirm-email/index.html', views.index),
    path("signup/", views.signup, name="account_signup"),
    path("login/", views.login, name="account_login"),
]
