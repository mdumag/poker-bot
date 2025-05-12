# poker_bot/deck.py

import random
from poker_bot.cards import Card

class Deck:
    """
    standard deck
    """
    def __init__(self):
        # create each card
        self.cards = [Card(rank, suit)
                      for rank in range(2, 15)
                      for suit in ['S', 'H', 'D', 'C']]

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self, n: int) -> list[Card]:
        """
        remove and return top card
        """
        drawn = self.cards[:n]
        self.cards = self.cards[n:]
        return drawn
