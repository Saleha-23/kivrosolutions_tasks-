import random
def number_guessing_game():
    secret_number = random.randint(1, 10)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
   
            if guess == secret_number:
                print("Correct! You guessed the number.")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()