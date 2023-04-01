import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card = Card('Hearts', 1)
        self.card1 = Card('Hearts', 5)
        self.card2 = Card('Hearts', 7)
        self.cards = [self.card, self.card1, self.card2]
        
    def test_check_for_ace(self):
        answer = CardGame.check_for_ace(self, self.card)
        self.assertEqual(True, answer)

    def test_highest_card(self):
        card1 = Card("Hearts", 10)
        card2 = Card("Spades", 5)
        answer = CardGame.highest_card(self, card1, card2)
        self.assertEqual(card1, answer)

    def test_cards_total(self):
        answer = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 13", answer)
