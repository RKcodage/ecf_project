"""
URL configuration for ecf_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from games import views
from games.views import TeamAPIView, PlayerAPIView, GameAPIView, BetAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bets/', views.bets, name='bets'),
    path('details/<int:game_id>/', views.details, name='games-details'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('api/teams/', views.TeamAPIView.as_view(), name='team-list'),  # Liste des équipes
    path('api/teams/<int:game_id>/', views.TeamAPIView.as_view(), name='team-detail'),  # Détail d'une équipe par ID
    path('api/games/', views.GameAPIView.as_view(), name='game-list'),  # Liste des jeux
    path('api/games/<int:game_id>/', views.GameAPIView.as_view(), name='game-detail'),  # Détail d'un jeu par ID
    path('api/players/', views.PlayerAPIView.as_view(), name='player-list'),  # Liste des joueurs
    path('api/players/<int:game_id>/', views.PlayerAPIView.as_view(), name='player-detail'),  # Détail d'un joueur par ID
    path('api/bets/', views.BetAPIView.as_view(), name='bet-list'),  # Liste des paris
    path('api/bets/<int:game_id>/', views.BetAPIView.as_view(), name='bet-detail'),  # Détail d'un pari par ID
    path('roster/', views.roster, name='roster'),
    path('', include('games.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)