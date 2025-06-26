import random 
# Welcome
print("Welcome to number guessing game")
print("you will be guessing a number between 1-100")
# Generating a guessing number
secret_number = random.randint(1,100)
max_attempts = 10
attempt = 0
# Game loop
while attempt < max_attempts:
    try:
        attempt += 1
        # User input 
        guess = int(input(f"\nAttempt {attempt} of {max_attempts}: Enter your guess between 1-100:"))
        # check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You have guessed correctly in {attempt} tries.")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print('Too high')
    except ValueError:
        print ("Please enter a valid number")
        
# User could not guess the number 
if guess != secret_number:
    print(f"Sorry! Your attempts are finished. The secret number is {secret_number}. Try again!")
    