# ui_game.py
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QLineEdit, QSpacerItem, QSizePolicy, QMessageBox)
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtCore import Qt
from rps_backend import RPSGame


class NameInputPage(QWidget):
    """Initial page to input user's name."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Your Name 🎮")
        self.setFixedSize(500, 500)

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)
        self.title_label = QLabel("Rock 🪨 Paper 📄 Scissor ✂️")
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        # Label
        self.label = QLabel("Enter your name:")
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Name input
        self.name_input = QLineEdit()
        self.name_input.setFont(QFont("Arial", 14))
        self.name_input.setPlaceholderText("Your name...")
        self.name_input.setFixedWidth(250)
        self.name_input.setStyleSheet("""
            QLineEdit {
                background-color: #3a3a5c;
                color: white;
                border-radius: 8px;
                padding: 5px;
            }
        """)

        # Submit button
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.setFont(QFont("Arial", 12))
        self.submit_btn.setFixedWidth(150)
        self.submit_btn.clicked.connect(self.submit_name)
        self.submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #3a3a5c;
                color: white;
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #5656a5;
            }
        """)

        # Add widgets to layout
        layout.addWidget(self.label)
        layout.addWidget(self.name_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.submit_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        # Apply dark palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#1e1e2f"))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)


    def submit_name(self):
        name = self.name_input.text().strip().capitalize()
        if name == "":
            name = "Player"
        self.game_ui = RPSGameUI(name)
        self.game_ui.show()
        self.close()


class RPSGameUI(QWidget):
    """Main Rock Paper Scissors Game UI."""
    def __init__(self, username="Player"):
        super().__init__()
        self.username = username
        self.setWindowTitle("Rock Paper Scissors 🎮")
        self.setFixedSize(500, 500)

        # Game logic
        self.game = RPSGame()

        # Setup UI
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # --- Title ---
        self.title_label = QLabel("Rock 🪨 Paper 📄 Scissor ✂️")
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.title_label)

        # --- Top Buttons: Reset & Exit ---
        top_btn_layout = QHBoxLayout()
        self.reset_btn = QPushButton("🔄 Reset Score")
        self.exit_btn = QPushButton("🚪 Exit")

        for btn in (self.reset_btn, self.exit_btn):
            btn.setFont(QFont("Arial", 11))
            btn.setFixedWidth(120)

        self.reset_btn.clicked.connect(self.reset_game)
        self.exit_btn.clicked.connect(self.exit_game)

        top_btn_layout.addWidget(self.reset_btn, alignment=Qt.AlignmentFlag.AlignLeft)
        top_btn_layout.addStretch()
        top_btn_layout.addWidget(self.exit_btn, alignment=Qt.AlignmentFlag.AlignRight)
        main_layout.addLayout(top_btn_layout)

        # --- Score Labels ---
        score_layout = QHBoxLayout()
        self.player_score_label = QLabel(f"{self.username}: 0")
        self.computer_score_label = QLabel("Computer: 0")
        for lbl in (self.player_score_label, self.computer_score_label):
            lbl.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.player_score_label.setContentsMargins(20, 0, 0, 0)
        self.computer_score_label.setContentsMargins(0, 0, 20, 0)
        score_layout.addWidget(self.player_score_label, alignment=Qt.AlignmentFlag.AlignLeft)
        score_layout.addStretch()
        score_layout.addWidget(self.computer_score_label, alignment=Qt.AlignmentFlag.AlignRight)
        main_layout.addLayout(score_layout)

        # --- Result Display ---
        self.result_label = QLabel("Make your move!")
        self.result_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.result_label)

        # --- Move Display ---
        move_layout = QHBoxLayout()
        move_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.player_move_label = QLabel("🪨")
        self.vs_label = QLabel("VS")
        self.computer_move_label = QLabel("📄")
        for lbl in (self.player_move_label, self.computer_move_label):
            lbl.setFont(QFont("Arial", 40))
        self.vs_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.vs_label.setStyleSheet("color: red;")
        move_layout.addWidget(self.player_move_label)
        move_layout.addSpacing(20)
        move_layout.addWidget(self.vs_label)
        move_layout.addSpacing(20)
        move_layout.addWidget(self.computer_move_label)
        main_layout.addLayout(move_layout)

        # --- Spacer ---
        main_layout.addSpacerItem(QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # --- Choice Buttons ---
        btn_layout = QHBoxLayout()
        self.rock_btn = QPushButton("🪨\nRock")
        self.paper_btn = QPushButton("📄\nPaper")
        self.scissor_btn = QPushButton("✂️\nScissor")
        for btn in (self.rock_btn, self.paper_btn, self.scissor_btn):
            btn.setFont(QFont("Arial", 17))
            btn.setFixedSize(100, 100)
        self.rock_btn.clicked.connect(lambda: self.play("r"))
        self.paper_btn.clicked.connect(lambda: self.play("p"))
        self.scissor_btn.clicked.connect(lambda: self.play("s"))
        btn_layout.addWidget(self.rock_btn)
        btn_layout.addWidget(self.paper_btn)
        btn_layout.addWidget(self.scissor_btn)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)
        self.apply_style()

    def play(self, choice):
        player, bot, result = self.game.play_round(choice)

        # Update hand icons
        self.player_move_label.setText(self.get_icon(player))
        self.computer_move_label.setText(self.get_icon(bot))

        # Update result text
        if result == "Win":
            self.result_label.setText(f"{self.username} WON! 🎉🥇")
            self.result_label.setStyleSheet("color: #11ff00;")
            self.vs_label.setStyleSheet("color: #11ff00;")
        elif result == "Lose":
            self.result_label.setText("COMPUTER WON! 🫵🏼🤣")
            self.result_label.setStyleSheet("color: red;")
            self.vs_label.setStyleSheet("color: red;")
        else:
            self.result_label.setText("😎 TIE!")
            self.result_label.setStyleSheet("color: white;")
            self.vs_label.setStyleSheet("color: white;")

        # Update scores
        score_you, score_bot = self.game.get_score()
        self.player_score_label.setText(f"{self.username}: {score_you}")
        self.computer_score_label.setText(f"Computer: {score_bot}")

    def reset_game(self):
        self.game.reset_score()
        self.result_label.setText("Scores reset! Let's play again.")
        self.vs_label.setStyleSheet("color: red;")
        self.player_score_label.setText(f"{self.username}: 0")
        self.computer_score_label.setText("Computer: 0")
        self.player_move_label.setText("🪨")
        self.computer_move_label.setText("📄")


    
    def exit_game(self):
        score_you, score_bot = self.game.get_score()
        if score_you > score_bot:
            winner_msg = f"🎉{self.username} Wins!\n\nFinal Score:\n{self.username}: {score_you}\nComputer: {score_bot}"
        elif score_bot > score_you:
            winner_msg = f"😢Computer Wins!\n\nFinal Score:\n{self.username}: {score_you}\nComputer: {score_bot}"
        else:
            winner_msg = f"😎It's a Tie!\n\nFinal Score:\n{self.username}: {score_you}\nComputer: {score_bot}"

        # Custom QMessageBox with matching style
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Game Over 🎮")
        msg_box.setText(winner_msg)
        msg_box.setIcon(QMessageBox.Information)

        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #1e1e2f;
                color: white;
                font-size: 16px;
                font-weight: bold;
                text-align: center;
            }
            QPushButton {
                background-color: #3a3a5c;
                color: white;
                border-radius: 8px;
                padding: 6px 18px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #5656a5;
            }
        """)

        msg_box.exec()
        self.close()

            
    def get_icon(self, move_name):
        icons = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}
        return icons.get(move_name, "❓")

    def apply_style(self):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#1e1e2f"))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)
        for btn in (self.rock_btn, self.paper_btn, self.scissor_btn, self.reset_btn, self.exit_btn):
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3a3a5c;
                    color: white;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #5656a5;
                }
            """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    name_page = NameInputPage()
    name_page.show()
    sys.exit(app.exec())
