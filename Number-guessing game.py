import random
import time

lowest_num = 1
highest_num = 100
max_guesses = 7

total_wins = 0
total_losses = 0

is_playing = True

while is_playing:
    answer = random.randint(lowest_num, highest_num)
    guesses = 0
    is_running = True
    start_time = time.time()

    print("\nPython Number Guessing Game")
    print("Select a number between", lowest_num, "and", highest_num)
    print("You have", max_guesses, "guesses!")

    while is_running:

        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)

            if guess < lowest_num or guess > highest_num:
                print("That number is out of range")
                print("Please select a number between", lowest_num, "and", highest_num)

            else:
                guesses += 1
                remaining_guesses = max_guesses - guesses

                if guess < answer:
                    print("Too low! Try again!")

                elif guess > answer:
                    print("Too high! Try again!")

                else:
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print("CORRECT! The answer was", answer)
                    print("Number of guesses:", guesses)
                    print("Time taken:", round(elapsed_time, 2), "seconds")
                    total_wins += 1
                    is_running = False

                if remaining_guesses > 0 and is_running:
                    print("You have", remaining_guesses, "guesses left.\n")

                if guesses >= max_guesses and guess != answer:
                    print("You ran out of guesses!")
                    print("The correct answer was", answer)
                    total_losses += 1
                    is_running = False

        else:
            print("Invalid guess")
            print("Please select a number between", lowest_num, "and", highest_num)

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        is_playing = False

print("\n--- Game Over ---")
print("Wins:", total_wins)
print("Losses:", total_losses)
