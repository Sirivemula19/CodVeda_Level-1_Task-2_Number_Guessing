import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("🎯 Guess the number between 1 and 100. You have 7 tries.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: "))
        except ValueError:
            print("⚠️ Enter a valid number.")
            continue

        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
            return
        elif guess < number:
            print("Too low.")
        else:
            print("Too high.")

    print(f"❌ Out of attempts! The number was {number}.")

play_game()
