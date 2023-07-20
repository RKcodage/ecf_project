from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team, Game, Player, Bet
from .serializers import TeamSerializer, PlayerSerializer, GameSerializer, BetSerializer
from datetime import timedelta
from django.contrib import messages

def is_staff_or_superuser(user):
    return user.is_staff or user.is_superuser

def home(request):
    # Retrieve past games in reverse order (most recent first)
    past_games = Game.objects.filter(datetime__lt=timezone.now() + timedelta(minutes=90)).order_by('-datetime')
    # Retrieve current games
    current_games = Game.objects.filter(datetime__lte=timezone.now(), datetime_end__gte=timezone.now())
    # Retrieve upcoming games
    upcoming_games = Game.objects.filter(datetime__gte=timezone.now() + timedelta(minutes=90)).order_by('datetime')
    context = {
    'past_games': past_games,
    'current_games': current_games,
    'upcoming_games': upcoming_games
    }
    return render(request, 'games/home.html', context)


def about(request) :
    return render(request, 'games/about.html', {'title' :''})

# users authorizations 
@login_required
@user_passes_test(is_staff_or_superuser)
def match(request):
    # Retrieve current and upcoming games
    current_games = Game.objects.filter(datetime__lte=timezone.now(), datetime_end__gt=timezone.now())
    upcoming_games = Game.objects.filter(datetime__gt=timezone.now())

    context = {
        'current_games': current_games,
        'upcoming_games': upcoming_games
    }

    return render(request, 'games/home.html', context)

@login_required
@user_passes_test(is_staff_or_superuser)
def details(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    context = {
        'game': game
    }
    return render(request, 'games/details.html', context)


def roster(request):
    home_team_name = request.GET.get('home_team')
    away_team_name = request.GET.get('away_team')

    home_team = Team.objects.filter(name=home_team_name).first()
    away_team = Team.objects.filter(name=away_team_name).first()

    context = {
        'home_team': home_team,
        'away_team': away_team
    }

    return render(request, 'games/roster.html', context)

@login_required
def bets(request):
    # Retrieve past games in reverse order (most recent first)
    past_games = Game.objects.filter(datetime__lt=timezone.now() + timedelta(minutes=90)).order_by('-datetime')

    # Retrieve current games
    current_games = Game.objects.filter(datetime__lte=timezone.now(), datetime_end__gte=timezone.now())

    # Retrieve upcoming games
    upcoming_games = Game.objects.filter(datetime__gte=timezone.now() + timedelta(minutes=90)).order_by('datetime')

    success_message = None

    if request.method == 'POST':
        if 'bet_id' in request.POST:
            bet_id = request.POST.get('bet_id')
            bet = get_object_or_404(Bet, id=bet_id)

            if 'cancel_bet' in request.POST:
                # Delete the bet object if the Cancel Bet button was pressed
                bet.delete()
                success_message = 'Bet canceled successfully.'
            else:
                bet_amount = request.POST.get('bet_amount')
                if float(bet_amount) == 0:
                    # Delete the bet if the bet_amount is set to 0
                    bet.delete()
                    success_message = 'Bet deleted successfully.'
                else:
                    # Update the bet_amount
                    bet.bet_amount = bet_amount
                    bet.save()
                    success_message = 'Bet updated successfully.'

        else:
            game_id = request.POST.get('game_id')
            team_id = request.POST.get('team_id')
            bet_amount = request.POST.get('bet_amount')

            # Create a new Bet object
            game = get_object_or_404(Game, id=game_id)
            team = get_object_or_404(Team, id=team_id)
            bet = Bet(user=request.user, game=game, team=team, bet_amount=bet_amount)
            bet.save()
            success_message = 'Bet placed successfully.'

        messages.success(request, success_message)

        return redirect('bets')

    # Retrieve user's bets
    user_bets = Bet.objects.filter(user=request.user)

    template_context = {
        'past_games': past_games,
        'current_games': current_games,
        'upcoming_games': upcoming_games,
        'user_bets': user_bets,
    }
    return render(request, 'games/bets.html', template_context)


def terminate_match(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    
    # Perform the necessary actions to terminate the match
    # For example, update the end time of the game
    game.datetime_end = timezone.now()
    game.save()
    success_message = 'Game has been terminated.'
    messages.success(request, success_message)
    # Redirect back to the match URL
    return redirect('games:home')

class TeamAPIView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response (serializer.data)

class GameAPIView(APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response (serializer.data)

class PlayerAPIView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response (serializer.data)

class BetAPIView(APIView):
    def get(self, request):
        bets = Bet.objects.all()
        serializer = BetSerializer(bets, many=True)
        return Response (serializer.data)


