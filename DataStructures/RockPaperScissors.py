import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What is your choice? Type 0 for Rock 1 for Paper 2 for scissors\n"))
print(f"Your choice:{user_choice}")

computer_choice = random.randint(0, 2)
print(f"Computer choice:{computer_choice}")

if user_choice >= 3:
    print("Invalid number You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("Its a draw!")
