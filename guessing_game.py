
import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
   
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
    else:
        print(f"Sorry, you ran out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    guessing_game()