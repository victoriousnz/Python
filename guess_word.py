#WORK IN PROGRESS
#TODO:
#Figure out how to make 'status' retain previous guesses in the correct position

import random

def get_word():
    """Returns random word."""
    words = ['Charlie', 'Woodstock', 'Snoopy', 'Lucy', 'Linus',
             'Schroeder', 'Patty', 'Sally', 'Marcie']
    return random.choice(words).upper()

def check(word, guesses):
    """Creates and returns string representation of word
    displaying asterisks for letters not yet guessed."""
    status = "" # Current status of guess
    last_guess = guesses[-1]
    matches = 0 # Number of occurrences of last_guess in word
    #print("You guessed", last_guess)

    matches = word.count(last_guess)
      
    if matches != 0:
        print("The word has {} {}'s.".format(matches,last_guess))
        i = 0
        while i < len(word):
            if last_guess == word[i]:
                status += last_guess
            else:
                status += "*"
            i += 1
    else:
        print("Sorry, that appears 0 times.")
        status += "*" * len(word)

    print("You've made {} guesses and gotten {}".format(len(guesses),status))

    # Loop through word checking if each letter is in guesses
    #  If it is, append the letter to status
    #  If it is not, append an asterisk (*) to status
    # Also, each time a letter in word matches the last guess,
    #  increment matches by 1.

    # Write a condition that outputs one of the following when
    #  the user's last guess was "A":
    #   'The word has 2 "A"s.' (where 2 is the number of matches)
    #   'The word has one "A".'
    #   'Sorry. The word has no "A"s.'

    return status

def main():
    word = get_word() # The random word
    print("The word is:", word)
    n = len(word) # The number of letters in the random word
    guesses = [] # The list of guesses made so far
    guessed = False
    #print('The word contains {} letters.'.format(n))

    while not guessed:
        guess = input("Guess a letter or a {}-letter word: ".format(n))
        guess = guess.upper()
        n2 = len(guess)
        if guess == word:
            guessed = True
            print("You got it!")
        else:
            if n2 == 1:
                guesses.append(guess)
                print("Checking...")
                if guesses.count(guess) == 1:
                    check(word,guesses)
                else:
                    print("You already guessed '{}'.".format(guess))
            else:
                print("Invalid entry.")

        # Write an if condition to complete this loop.
        # You must set guessed to True if the word is guessed.
        # Things to be looking for:
        #  - Did the user already guess this guess?
        #  - Is the user guessing the whole word?
        #     - If so, is it correct?
        #  - Is the user guessing a single letter?
        #     - If so, you'll need your check() function.
        #  - Is the user's guess invalid (the wrong length)?
        #
        # Also, don't forget to keep track of the valid guesses.

    #print('{} is it! It took {} tries.'.format(word, len(guesses)))

main()
