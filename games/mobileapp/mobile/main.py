from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import requests
import kivy

kivy.require('2.2.1')

class Header(BoxLayout):
    def __init__(self, **kwargs):
        super(Header,self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [10,20]
        self.spacing = 10

        # Label de titre
        title_label = Label(text='NFL Bet Master', font_size='20sp', bold=True)
        

class GameTab(TabbedPanelItem):
    def __init__(self, game_data, **kwargs):
        super(GameTab, self).__init__(**kwargs)
        self.game_data = game_data
        self.content = BoxLayout(orientation='vertical')
        self.add_widget(self.content)
        self.display_game_data()

    def display_game_data(self):
        self.content.clear_widgets()
        if not self.game_data:
            self.content.add_widget(Label(text="No games available"))
        else:
            for game in self.game_data:
                game_details = f"{game['home_team']} vs {game['away_team']}\n" \
                                f"Date: {game['date']}\n"

                if 'score' in game:
                    game_details += f"Final Score: {game['score']}\n"
                    game_details += f"{game['commentary']}\n"
                elif 'odds' in game:
                    game_details += f"Odds: {game['home_team_odds']} vs {game['away_team_odds']}\n"
                    game_details += f"Starting Time: {game['start_time']}\n"
                    game_details += f"End Time: {game['end_time']}\n"
                    game_details += f"Weather: {game['weather']}\n"

                game_label = Label(text=game_details, size_hint=(1, None), height=100)
                self.content.add_widget(game_label)

class GameTabs(TabbedPanel):
    def __init__(self, past_games, current_games, upcoming_games, **kwargs):
        super(GameTabs, self).__init__(**kwargs)
        self.add_widget(GameTab(game_data=past_games, text="Past Games"))
        self.add_widget(GameTab(game_data=current_games, text="Current Games"))
        self.add_widget(GameTab(game_data=upcoming_games, text="Upcoming Games"))

class SportsApp(App):
    def build(self):
        # Récupération des données de l'API

        # Pour les équipes
        teams_url = 'http://localhost:8000/api/teams/'
        response = requests.get(teams_url)
        if response.status_code == 200:
            teams_data = response.json()
            print(teams_data)
        else:
            print('Error while recovering teams.')

        # Pour la liste des jeux
        games_url = 'http://localhost:8000/api/games/'
        response = requests.get(games_url)
        if response.status_code == 200:
            games_data = response.json()
            print(teams_data)
        else:
            print('Error while recovering games.')

        # Pour les joueurs
        players_url = 'http://localhost:8000/api/players/'
        response = requests.get(players_url)
        if response.status_code == 200:
            players_data = response.json()
            print(players_data)
        else:
            print('Error while recovering players.')

        # Pour les paris
        bets_url = 'http://localhost:8000/api/bets/'
        response = requests.get(bets_url)
        if response.status_code == 200:
            bets_data = response.json()
            print(bets_data)
        else:
            print('Error while recovering bets.')

        # Retourner l'instance de GameTabs avec les données de l'API
        return GameTabs(past_games=games_data, current_games=games_data, upcoming_games=games_data)

if __name__ == '__main__':
    SportsApp().run()

