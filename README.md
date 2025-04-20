Blackjack Game

Overview

This console-based Blackjack game, written in Python, offers a classic casino-style experience where players compete against a dealer to reach a card value as close to 21 as possible without busting. The game features a clean interface, robust input validation, and an AI-driven dealer that makes strategic decisions based on card values and randomized probabilities.

Features





Authentic Blackjack Gameplay: Follows standard rules with hit/stand options, aces valued at 1 or 11, and automatic bust detection.



Intelligent Dealer AI: The dealer uses a probabilistic strategy, deciding to hit or stand based on card values and random chance thresholds.



Multi-Round Support: Players can specify the number of games to play in a single session.



Clear User Interface: Console output displays player and dealer hands, card values, and game results in an easy-to-read format.



Robust Input Validation: Ensures reliable handling of user inputs to prevent crashes from invalid entries.



Beginner-Friendly Rules Prompt: Offers a link to Blackjack rules for players unfamiliar with the game.

Installation

Prerequisites





Python 3.x installed on your system.

Steps





Clone the Repository:

git clone https://github.com/AtharvSharma09/Blackjack.git



Navigate to the Project Directory:

cd blackjack



Run the Game:

python blackjack.py

Usage





Launch the game using the command above.



Answer whether you know Blackjack rules (y/n). If "n", a link to rules is provided.



Specify the number of games you want to play.



For each round:





View your initial two cards and the dealer's visible card.



Choose to "hit" (draw another card) or "stand" (keep your current hand).



The dealer plays automatically, and the winner is determined based on card values.



Continue until all specified games are played.

Code Structure





File: blackjack.py



Main Class: Blackjack



Key Methods:





get_card(): Draws a random card with appropriate value (e.g., Ace as 1 or 11).



dealer_ai(): Implements the dealer's decision-making logic using value-based thresholds and randomization.



play_round(): Manages a single round, including card dealing and player/dealer turns.



determine_winner(): Evaluates and displays the outcome (win, loss, or tie).

Future Enhancements





Develop a graphical user interface (GUI) using Pygame or Tkinter for a more immersive experience.



Introduce a betting system to add strategic depth.



Implement score tracking and persistence (e.g., using SQLite) to save high scores.



Create a web-based version with Flask or Django for online accessibility.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing

Contributions are welcome! To contribute:





Fork the repository.



Create a new branch (git checkout -b feature/your-feature).



Make your changes and commit (git commit -m "Add your feature").



Push to the branch (git push origin feature/your-feature).



Open a pull request.

