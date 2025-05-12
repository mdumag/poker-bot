import pytest
from poker_bot.cards import Card

def test_card_repr():
    card = Card(14, 'S')
    assert repr(card) == "14S"

def test_card_attributes():
    card = Card(10, 'H')
    assert card.rank == 10
    assert card.suit == 'H'
