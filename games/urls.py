from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='games-home'),
    path('about/', views.about, name='games-about'),
]
