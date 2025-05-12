import pytest
from poker_bot.deck import Deck
from poker_bot.cards import Card

def test_deck_initial_count():
    deck = Deck()
    assert len(deck.cards) == 52

def test_deck_draw_reduces_cards():
    deck = Deck()
    deck.shuffle()
    drawn = deck.draw(5)
    assert isinstance(drawn, list)
    assert len(drawn) == 5
    assert len(deck.cards) == 47

def test_drawn_cards_are_card_instances():
    deck = Deck()
    drawn = deck.draw(3)
    assert all(isinstance(c, Card) for c in drawn)
