# poker_bot/cards.py

class Card:

    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.rank}{self.suit}"