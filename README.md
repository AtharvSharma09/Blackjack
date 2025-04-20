# Blackjack
##Overview

This is a console-based Blackjack game implemented in Python. The game simulates a classic casino-style Blackjack experience where players compete against a dealer to get as close to 21 as possible without going over. It features a simple yet engaging interface, robust input validation, and an AI-driven dealer that makes decisions based on card values and random chance.

##Features





Realistic Gameplay: Supports standard Blackjack rules, including hit/stand choices, aces valued at 1 or 11, and automatic bust detection.



Dealer AI: The dealer follows a probabilistic strategy, deciding to hit or stand based on card values and random thresholds.



Multi-Round Play: Allows players to specify the number of games to play in a session.



User-Friendly Interface: Clear console output displays player and dealer hands, card values, and game outcomes.



Input Validation: Ensures robust handling of user inputs, preventing crashes from invalid entries.



Rules Prompt: Offers a link to Blackjack rules for new players.

##How to Run





Prerequisites: Ensure Python 3.x is installed on your system.



Clone the Repository:

git clone https://github.com/yourusername/blackjack.git



Navigate to the Project Directory:

cd blackjack



##Run the Game:

python blackjack.py



Follow the on-screen prompts to play, including whether you know the rules, the number of games, and hit/stand choices.

##Code Structure





blackjack.py: The main script containing the Blackjack class, which handles game logic, card dealing, dealer AI, and user interaction.



##Key methods:





get_card(): Draws random cards with appropriate values.



dealer_ai(): Implements the dealer's decision-making logic.



play_round(): Manages a single round of gameplay.



determine_winner(): Evaluates and displays the game outcome.

##Potential Improvements





Add a graphical user interface (GUI) using Pygame or Tkinter for a more engaging experience.



Implement a betting system to enhance gameplay realism.



Add score tracking and persistence to save high scores across sessions.



Create a web-based version using Flask or Django for online play.

##License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For questions or suggestions, feel free to open an issue or contact Atharv Sharma at atharvsharmatgu@gmail.com.



This project was built to demonstrate Python programming skills, including object-oriented programming, randomization, and game logic. Enjoy playing, and good luck at the table!
