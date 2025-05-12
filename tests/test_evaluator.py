import pytest
from poker_bot.cards import Card
from poker_bot.evaluator import HandEvaluator

def make_cards(strs):
    # convert strings to Card objects
    return [Card(int(s[:-1]) if s[:-1].isdigit() else {'A':14,'K':13,'Q':12,'J':11}[s[:-1]], s[-1])
            for s in strs]

@pytest.mark.parametrize("hand,expected", [
    # Royal flush
    (["10H","11H","12H","13H","14H","2C","3D"], ("royal_flush", 14)),
    # Straight flush
    (["5H","6H","7H","8H","9H","2C","3D"], ("straight_flush", 9)),
    # Four of a kind
    (["7C","7D","7H","7S","2H","3D","4C"], ("four_of_a_kind", 7)),
    # Full house
    (["6C","6D","6H","13S","13H","2D","3C"], ("full_house", (6, 13))),
    # Flush
    (["2S","5S","9S","11S","13S","3H","4D"], ("flush", [13,11,9,5,2])),
    # Straight
    (["8H","9D","10C","11S","12H","2C","3D"], ("straight", 12)),
    # Three of a kind
    (["4H","4D","4S","9C","12D","2C","3H"], ("three_of_a_kind", 4)),
    # Two pair
    (["11H","11D","3S","3C","8H","2D","4C"], ("two_pair", (11,3))),
    # One pair
    (["12H","12D","5S","8C","9H","2D","3C"], ("one_pair", (12, [9,8,5,3,2]))),
    # High card
    (["14H","2D","5S","8C","9H","3D","4C"], ("high_card", [14,9,8,5,4])),
])
def test_hand_ranks(hand, expected):
    cards = make_cards(hand)
    rank = HandEvaluator.evaluate(cards)
    assert rank == expected
