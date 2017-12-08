# from Words_list import words_list
import random

# create a hangman game for 1st project:
# find length of words in list, use that as range upper limit, select a random number /
# use that number to select an index value to generate a random word from the list
# assign that word to a variable and loop through to search for user_guess
# assign a body part to each wrong user_guess,6 total
# display answers and running body part total

list = ["blue", "pink", "green", "aqua", "silver", "puce", "orange"]
user_guess = []  # empty list to hold user input
CORRECT_LETTERS = []  # counter
WRONG_LETTERS = []  # counter


def main():
    intro()  # call the function

    # guess the answer now? points!
    # display total of letters in word, in postion


def intro():
    print("Hello, let's play Hangman...")
    print("****************************")
    # call the function to return a word
    secret_word = get_word()  # function for computer word
    print(secret_word)  # show for testing
    guess = get_user_letters(secret_word)  # function to get player word
    check_for_letter(guess, secret_word)  # function for comparing


def get_user_letters(n):
    string = ""
    inputs = num_letters_in_secret_word(n)  # determine how many times to ask for a letter

    index = 0  # initialize count
    while index < inputs:
        letter = input("Enter a letter: ")  # get input
        # user_guess.append(letter) #add letter to list
        string = string + letter
        index += 1
    return string


def get_word():
    list_length = len(list)
    word_index = random.randint(0, list_length)
    # print("there are",list_length, "word choices.") #testing
    # print("index value", word_index, "holds the secret word.") #testing
    print()
    # store the word at the random index value, to play the game
    secret_word = list[word_index - 1]
    # print(secret_word)
    blanks = num_letters_in_secret_word(secret_word)
    print("The word has", blanks, "letters.")
    print()
    return secret_word


def num_letters_in_secret_word(n):
    # get the length to use for range
    number = len(n)
    return number


# pass user letters and secret word to compare
def check_for_letter(l, word):
    # check for letters and fill in the correct spot in the word
    print("Ok, searching for...", l)
    print("Yours: ", l)
    print("Computers: ", word)
    if l == word:
        print("it's a match!")
        print
    else:
        print("boo")
        print()

    again = input("Again? y/n: ")

    if again == "y":
        secret_word = get_word()
        get_user_letters(secret_word)

    else:
        print("Goodbye")

        ####need to compare charactersat each index position.


main()

# Project 1 Capstone
# Sonja Hayden

# from Words_list import words_list
import random

# create a hangman game for 1st project:
# find length of words in list, use that as range upper limit, select a random number /
# use that number to select an index value to generate a random word from the list
# assign that word to a variable and loop through to search for user_guess
# assign a body part to each wrong user_guess,6 total
# display answers and running body part total

list = ["blue", "pink", "green", "aqua", "silver", "puce", "orange"]
user_guess = []  # empty list to hold user input
CORRECT_LETTERS = []  # emptylist
WRONG_LETTERS = []  # counter


def main():
    x = intro()  # call the function
    # print(x)
    print()
    # guess the answer now? points!
    # display total of letters in word, in postion


def intro():
    print("Hello, let's play Hangman...")
    print("****************************")
    # call the function to return a word
    secret_word = get_word()  # function for computer word
    print(secret_word)  # show for testing
    guess = get_user_letters(secret_word)  # function to get player word
    # validate_input()
    # check_for_letter(guess, secret_word)       #function for comparing
    # return (secret_word, guess)

    result1, result2 = compare_user_letter(guess, secret_word)
    print("These letters are correct: ", result1)
    print("these letters are wrong: ", result2)
    again = input("Again? y/n: ")
    if again == "y":
        secret_word = get_word()
        get_user_letters(secret_word)
        again = input("Again? y/n: ")
    else:
        print("Goodbye")


# get user input to compare to the secret word
def get_user_letters(n):
    string = ""
    inputs = num_letters_in_secret_word(n)  # determine how many times to ask for a letter
    index = 0  # initialize counter
    while index < inputs:  # get input for as long as the secret word
        letter = input("Enter a letter: ")  # get input
        string = string + letter
        index += 1
    return string


def get_word():
    list_length = len(list)
    word_index = random.randint(0, list_length)
    # print("there are",list_length, "word choices.") #testing
    # print("index value", word_index, "holds the secret word.") #testing
    print()
    # store the word from random index value, to play the game
    secret_word = list[word_index - 1]
    # print(secret_word)
    blanks = num_letters_in_secret_word(secret_word)
    print("The word has", blanks, "letters.")
    print()
    return secret_word


def num_letters_in_secret_word(n):
    # get the length to use for range
    number = len(n)
    return number


# def validate_input():

def compare_user_letter(x, z):
    for ch in x:
        if ch in z:
            # print(ch)
            CORRECT_LETTERS.append(ch)
        else:
            WRONG_LETTERS.append(ch)
    return CORRECT_LETTERS, WRONG_LETTERS


# pass user letters and secret word to compare
def check_for_letter(l, word):
    # check for letters and fill in the correct spot in the word
    print("Ok, searching for...", l)
    print("Yours: ", l)
    print("Computers: ", word)
    if l == word:
        print("it's a match!")
        print
    else:
        print("boo")
        print()

    again = input("Again? y/n: ")

    if again == "y":
        secret_word = get_word()
        get_user_letters(secret_word)

    else:
        print("Goodbye")

        ####need to compare charactersat each index position.


main()
