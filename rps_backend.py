# rps_backend.py
import random

class RPSGame:
    def __init__(self):
        self.score_player = 0
        self.score_bot = 0
        self.choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}

    def play_round(self, choice_key):
        if choice_key not in self.choices:
            return None, None, "Invalid choice!"

        player_choice = self.choices[choice_key]
        bot_choice = random.choice(list(self.choices.values()))

        # Determine winner
        result = ""
        if player_choice == bot_choice:
            result = "Tie!"
        elif (
            (player_choice == "Rock" and bot_choice == "Scissors") or
            (player_choice == "Paper" and bot_choice == "Rock") or
            (player_choice == "Scissors" and bot_choice == "Paper")
        ):
            result = "Win"
            self.score_player += 1
        else:
            result = "Lose"
            self.score_bot += 1

        return player_choice, bot_choice, result

    def get_score(self):
        return self.score_player, self.score_bot

    def reset_score(self):
        self.score_player = 0
        self.score_bot = 0
