import random
import time


class Blackjack:
    """Class to simulate a blackjack game against a dealer."""
    
    def __init__(self):
        """Initialize the blackjack game with card deck and state."""
        self.suits = ("Club", "Spade", "Heart", "Diamond")
        self.ranks = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
            "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
        }
        self.player_deck = []
        self.dealer_deck = []
        self.player_value = 0
        self.dealer_value = 0
        self.current_game = 1
        self.total_games = 0

    def show_rules(self) -> None:
        """Prompt user about blackjack rules and display a resource if needed."""
        while True:
            choice = input("Do you know how to play blackjack? (y/n): ").lower()
            if choice == "n":
                print("Visit: https://www.venetianlasvegas.com/casino/table-games/how-to-play-blackjack.html")
                break
            elif choice == "y":
                break
            else:
                print("Please enter 'y' or 'n'!")
                time.sleep(1)

    def get_num_games(self) -> int:
        """Prompt user for the number of games to play with validation.
        
        Returns:
            int: Number of games.
        """
        while True:
            try:
                num_games = int(input("Enter the number of games you want to play: "))
                if num_games <= 0:
                    print("Please enter a positive number!")
                    time.sleep(1)
                    continue
                self.total_games = num_games
                return num_games
            except ValueError:
                print("Please enter a valid number!")
                time.sleep(1)

    def get_card(self) -> tuple[str, int]:
        """Draw a random card and return its description and value.
        
        Returns:
            tuple: Card description (e.g., "Ace of Spades") and its value.
        """
        rank = random.choice(list(self.ranks.keys()))
        suit = random.choice(self.suits)
        value = self.ranks[rank]
        return f"{rank} of {suit}s", value

    def determine_winner(self) -> None:
        """Determine and display the game outcome based on card values."""
        print("----------------------------------")
        print("\n")
        if self.player_value > 21:
            print("You Busted\nThe Dealer Won")
        elif self.dealer_value > 21:
            print("The Dealer Busted\nYou Won")
        elif self.player_value > self.dealer_value and self.player_value <= 21:
            print("You were closer to 21\nYou Won")
        elif self.dealer_value > self.player_value and self.dealer_value <= 21:
            print("The dealer was closer to 21\nThe Dealer Won")
        elif self.dealer_value == self.player_value and self.dealer_value <= 21:
            print("You both were equally close to 21\nThe game tied")
        
        self.player_deck.clear()
        self.dealer_deck.clear()
        self.current_game += 1
        time.sleep(1)
        print("\n")

    def dealer_ai(self) -> None:
        """Simulate dealer's actions based on card value and random chance."""
        while True:
            random_chance = random.randint(1, 100)
            if self.dealer_value >= 20:
                break
            elif self.dealer_value in [18, 19] and random_chance > 10:
                break
            elif self.dealer_value in [15, 16, 17] and random_chance > 30:
                break
            elif self.dealer_value in [12, 13, 14] and random_chance > 60:
                break
            else:
                card, value = self.get_card()
                if self.dealer_value >= 11:
                    self.ranks["Ace"] = 1
                else:
                    self.ranks["Ace"] = 11
                self.dealer_deck.append(card)
                self.dealer_value += value

    def play_round(self) -> None:
        """Play a single round of blackjack."""
        print("----------------------------------")
        print(f"Game {self.current_game} of {self.total_games}")
        print("----------------------------------")
        
        # Deal initial cards
        self.player_deck = []
        self.dealer_deck = []
        self.player_value = 0
        self.dealer_value = 0

        print("Your hand:")
        card, value = self.get_card()
        self.player_deck.append(card)
        self.player_value = value
        print(card)
        if self.player_value >= 11:
            self.ranks["Ace"] = 1
        else:
            self.ranks["Ace"] = 11
        card, value = self.get_card()
        self.player_deck.append(card)
        self.player_value += value
        print(card)
        print(f"Value of cards: {self.player_value}")
        
        if self.player_value == 21:
            self.determine_winner()
            return

        print("----------------------------------")
        print("Dealer's hand:")
        card, value = self.get_card()
        self.dealer_deck.append(card)
        self.dealer_value = value
        print("hidden")
        if self.dealer_value >= 11:
            self.ranks["Ace"] = 1
        else:
            self.ranks["Ace"] = 11
        card, value = self.get_card()
        self.dealer_deck.append(card)
        self.dealer_value += value
        print(card)

        if self.dealer_value == 21:
            print("----------------------------------")
            print("Dealer's deck:")
            for card in self.dealer_deck:
                print(card)
            self.determine_winner()
            return

        # Player's turn
        while True:
            print("----------------------------------")
            choice = input("Choose hit or stand: ").lower()
            if choice not in ["hit", "stand"]:
                print("Please enter 'hit' or 'stand'!")
                time.sleep(1)
                continue
            
            if choice == "hit":
                print("Your hand:")
                for card in self.player_deck:
                    print(card)
                if self.player_value >= 11:
                    self.ranks["Ace"] = 1
                else:
                    self.ranks["Ace"] = 11
                card, value = self.get_card()
                self.player_deck.append(card)
                self.player_value += value
                print(card)
                print(f"Value of cards: {self.player_value}")
                if self.player_value > 21:
                    self.determine_winner()
                    break
            else:  # stand
                print(f"The value of your cards was: {self.player_value}")
                print("----------------------------------")
                print("Dealer's deck:")
                for card in self.dealer_deck:
                    print(card)
                self.dealer_ai()
                print(f"The value of dealer's cards was: {self.dealer_value}")
                self.determine_winner()
                break

    def play(self) -> None:
        """Run the blackjack game loop for the specified number of games."""
        self.show_rules()
        self.get_num_games()
        while self.current_game <= self.total_games:
            self.play_round()
        print("Thanks for playing!")

def main():
    """Main function to start the blackjack game."""
    game = Blackjack()
    game.play()

if __name__ == "__main__":
    main()
