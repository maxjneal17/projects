import random
import math

lower_range = int(input("Enter the lower limit of the range of numbers: "))
upper_range = int(input("Enter the upper limit of the range of numbers: "))

random_num = random.randint(lower_range, upper_range)
guess_count = 0

min_guess = int(round(math.log((upper_range - lower_range + 1), 2)))

print("You've only got " + str(min_guess) + " chances to guess the integer!")
guess = 0                 
while guess != random_num:        
    guess = int(input("Guess a number: "))
    guess_count = guess_count + 1
    if guess > random_num:
        print("Try Again! You guessed too large.")
    elif guess < random_num:
        print("Try Again! You guessed too small.")
    elif guess < lower_range or guess > upper_range:
        print("Your guess is out of range. Try again.")  
    elif guess == random_num and (guess_count == min_guess or guess_count < min_guess):
        print("Congrats! Total Number of Guesses = " + str(guess_count))
    elif guess == random_num and guess_count > min_guess:
        print("You did not guess in the minimum amount of guesses.")
    
