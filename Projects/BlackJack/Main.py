import random


def deal_card():
    """ Returns a random card from the deck"""
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


user_cards = []
computer_cards = []

""" Create a for loop which runs twice to allocate 2 cards to each user"""
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(cards):
    """ Calculate the sum for the cards present as part of list"""
    return sum(cards)

