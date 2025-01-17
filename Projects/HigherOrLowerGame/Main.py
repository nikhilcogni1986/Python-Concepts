# Higher or Lower game
# A celebrity is compared with another one on instagram who has more followers
# Create a data.py file with list of dictionaries and import the same in main file
# dictionary data should have the following key value pairs name, follower count, description, country
# import art logo, data file, and random module

import random

from art import logo
from art import vs
from data import data_list

print(logo)
score = 0


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers_cnt, b_followers_cnt):
    """ Validate the maximum followers between A and B"""
    if a_followers_cnt > b_followers_cnt:
        return user_guess == 'a'
    else:
        return user_guess == 'b'


account_b = random.choice(data_list)
game_should_continue = True

while game_should_continue:
    # Generate random account from game data
    account_a = account_b
    account_b = random.choice(data_list)
    if account_a == account_b:
        account_b = random.choice(data_list)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # Ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B' ").lower()
    print("\n * 20")
    print(logo)

    # get the followers account
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    # check the followers
    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    # Give the feedback to users
    if is_correct:
        score += 1
        print(f"You are correct, Current Score is: {score}")
    else:
        print(f"Sorry you are wrong! Final score: {score}")
        game_should_continue = False
