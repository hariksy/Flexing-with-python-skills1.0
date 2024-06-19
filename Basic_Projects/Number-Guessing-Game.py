import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt

# Function to provide random message prompts with Game of Thrones references
def message_prompts():
    messages = [
        "Winter is coming... but your guess was not the one.",
        "You know nothing, Jon Snow... especially the number I'm thinking of.",
        "The night is dark and full of errors... like your guess.",
        "Valar Morghulis... but your guess was not the one to live.",
        "You must be as blind as Maester Aemon, for your guess was far from the mark.",
        "In the game of numbers, you win or you guess again.",
        "Dracarys! Your guess went up in flames.",
        "You may be the King in the North, but you're not the Guesser of the Number.",
        "The North remembers... that your guess was incorrect.",
        "When you play the number guessing game, you win or you die. Unfortunately, you didn't win this time.",
        "The things I do for love... do not include giving hints for your guess.",
        "You drink and you know things... but you don't know the number you guessed.",
        "I am the sword in the darkness... but not the number in your guess.",
    ]
    return random.choice(messages)  # Return a random message from the list

class GameOfThronesGuessingGame(QWidget):
    def __init__(self):
        super().__init__()

        # Game state variables
        self.level = 1
        self.attempts = 0
        self.secret_number = 0
        self.max_attempts = {1: 10, 2: 7, 3: 5}
        self.ranges = {1: 50, 2: 100, 3: 200}
        self.hint_frequency = {1: 1, 2: 2, 3: 3}
        self.players = []
        self.current_player_index = 0
        self.scores = {}

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Game of Guessing")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #1a1a1a; color: #f0e68c;")

        font = QFont("Verdana", 12)

        # Load Game of Thrones-like font
        QFontDatabase.addApplicationFont("C:\Windows\Fonts\Game of Thrones Regular.ttf")
        got_font = QFont("Game of Thrones", 15, QFont.Bold)

        self.layout = QVBoxLayout()

        # Welcome Page
        welcome_label = QLabel("Valar Morghulis\nWelcome to the Game of Guessing!")
        welcome_label.setFont(got_font)
        welcome_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(welcome_label)
        self.instructions_label = QLabel("Lowest point wins\nEnter player names separated by commas.")
        self.instructions_label.setFont(font)
        self.instructions_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.instructions_label)

        self.input_layout = QHBoxLayout()
        
        self.player_input = QLineEdit()
        self.player_input.setFont(font)
        self.player_input.returnPressed.connect(self.add_players)
        self.input_layout.addWidget(self.player_input)

        self.add_player_button = QPushButton("Add Players")
        self.add_player_button.setFont(font)
        self.add_player_button.clicked.connect(self.add_players)
        self.input_layout.addWidget(self.add_player_button)

        self.layout.addLayout(self.input_layout)

        self.guess_layout = QVBoxLayout()
        
        self.guess_input_layout = QHBoxLayout()
        self.guess_label = QLabel("Enter your guess:")
        self.guess_label.setFont(font)
        self.guess_input_layout.addWidget(self.guess_label)

        self.guess_input = QLineEdit()
        self.guess_input.setFont(font)
        self.guess_input.returnPressed.connect(self.check_guess)  # Connect Enter key to check_guess
        self.guess_input_layout.addWidget(self.guess_input)

        self.guess_button = QPushButton("Submit Guess")
        self.guess_button.setFont(font)
        self.guess_button.clicked.connect(self.check_guess)
        self.guess_input_layout.addWidget(self.guess_button)

        self.guess_layout.addLayout(self.guess_input_layout)

        self.result_label = QLabel("")
        self.result_label.setFont(font)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.guess_layout.addWidget(self.result_label)

        self.score_label = QLabel("Score: 0")
        self.score_label.setFont(font)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.guess_layout.addWidget(self.score_label)

        self.next_level_button = QPushButton("Next Level")
        self.next_level_button.setFont(font)
        self.next_level_button.clicked.connect(self.next_level)
        self.next_level_button.setEnabled(False)
        self.guess_layout.addWidget(self.next_level_button)

        self.exit_button = QPushButton("Exit Game")
        self.exit_button.setFont(font)
        self.exit_button.clicked.connect(self.exit_game)
        self.guess_layout.addWidget(self.exit_button)

        self.layout.addLayout(self.guess_layout)
        self.guess_layout.setEnabled(False)

        self.setLayout(self.layout)

    def add_players(self):
        player_names = self.player_input.text().strip().split(',')
        if player_names:
            self.players = [name.strip() for name in player_names]
            self.scores = {player: 0 for player in self.players}
            self.current_player_index = 0
            self.instructions_label.setText(f"Player {self.players[self.current_player_index]}'s turn")
            self.guess_layout.setEnabled(True)
            self.add_player_button.setEnabled(False)
            self.player_input.setEnabled(False)
            self.start_game()

    def start_game(self):
        self.attempts = 0
        self.secret_number = random.randint(1, self.ranges[self.level])
        self.instructions_label.setText(f"Level {self.level} - {self.players[self.current_player_index]}, guess the number between 1 and {self.ranges[self.level]}")
        self.guess_input.clear()
        self.result_label.setText("")
        self.next_level_button.setEnabled(False)
        self.guess_button.setEnabled(True)

    def check_guess(self):
        try:
            guess = int(self.guess_input.text())
            self.attempts += 1

            if guess < self.secret_number:
                self.result_label.setText("Too low! " + (message_prompts() if self.attempts % self.hint_frequency[self.level] == 0 else ""))
            elif guess > self.secret_number:
                self.result_label.setText("Too high! " + (message_prompts() if self.attempts % self.hint_frequency[self.level] == 0 else ""))
            else:
                self.result_label.setText(f"Congratulations! {self.players[self.current_player_index]}, you guessed it in {self.attempts} attempts!")
                self.scores[self.players[self.current_player_index]] += self.attempts
                self.score_label.setText(f"Score: {self.scores[self.players[self.current_player_index]]}")
                self.next_level_button.setEnabled(True)
                self.guess_button.setEnabled(False)

            if self.attempts >= self.max_attempts[self.level] and guess != self.secret_number:
                self.result_label.setText(f"You've used all {self.max_attempts[self.level]} attempts. The number was {self.secret_number}.")
                self.next_level_button.setEnabled(True)
                self.guess_button.setEnabled(False)
        except ValueError:
            self.result_label.setText("Please enter a valid number.")

    def next_level(self):
        self.scores[self.players[self.current_player_index]] += self.attempts
        if self.level < 3:
            self.level += 1
            self.start_game()
        else:
            self.current_player_index += 1
            if self.current_player_index < len(self.players):
                self.level = 1
                self.start_game()
            else:
                winner = min(self.scores, key=self.scores.get)
                scoreboard = "\n".join([f"{player}: {score} points" for player, score in self.scores.items()])
                QMessageBox.information(self, "Scoreboard", f"Game Over!\n\n{scoreboard}\n\nWinner: {winner}\n\nValar Dohaeris")
                self.reset_game()

    def reset_game(self):
        self.level = 1
        self.attempts = 0
        self.secret_number = 0
        self.players = []
        self.current_player_index = 0
        self.scores = {}
        self.add_player_button.setEnabled(True)
        self.player_input.setEnabled(True)
        self.guess_layout.setEnabled(False)
        self.instructions_label.setText("Lowest point wins\nEnter player names separated by commas.")
        self.score_label.setText("Score: 0")
        self.next_level_button.setText("Next Level")
        self.next_level_button.clicked.disconnect(self.show_scoreboard)
        self.next_level_button.clicked.connect(self.next_level)

    def exit_game(self):
        self.show_scoreboard()

    def show_scoreboard(self):
        winner = min(self.scores, key=self.scores.get)
        scoreboard = "\n".join([f"{player}: {score} points" for player, score in self.scores.items()])
        QMessageBox.information(self, "Scoreboard", f"Game Over!\n\n{scoreboard}\n\nWinner: {winner}\n\nValar Dohaeris")
        self.reset_game()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = GameOfThronesGuessingGame()
    game.show()
    sys.exit(app.exec_())
