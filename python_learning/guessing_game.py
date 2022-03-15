#! /usr/bin/python3

secret = "3"
guess = ""
guess_count = 0
guess_limit = 5 #how many times we can try
out_of_guesses = False #boolean, whether the user is out of guesses - if its true, then we are out of guesses


while guess != secret and not(out_of_guesses): #i want to keep going through the loop until guess is not equal to secret and we are not out of guesses
    if guess_count < guess_limit:
         guess = input("Try to guess the number between 1 - 10, you have 5 tries:")
         guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Unfortunately you ran out of guesses.")
elif guess_count == 1:
    print("Congratulations, you guessed a secret number: " + str(secret)+ " ! And it took only " + str(guess_count) + " guess.") 
else:
    print("Congratulations, you guessed a secret number: " + str(secret)+ " ! And it took only " + str(guess_count) + " guesses.") 
    

