from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name="shorten_url"),
    path('display/', views.display_all, name="display_all"),
    path('<str:user_input>/', views.redirect_to_url, name="redirect_to_url"),
]