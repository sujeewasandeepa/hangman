import random

diagrams = ["""
        __________
        |         |
        |
        |
        |
        |
""", """

        __________
        |         |
        |         0
        |
        |
        |
""", """

        __________
        |         |
        |         0
        |         |
        |
        |
""", """
        __________
        |         |
        |         0
        |       / |
        |
        |       
""", """
        __________
        |         |
        |         0
        |       / | \\
        |
        |  
""", """

        __________
        |         |
        |         0
        |       / | \\
        |       /
        |
""", """
        __________
        |         |
        |         0
        |       / | \\
        |       /   \\
        |
"""]
words = ["acres", "adult", "advice", "arrangement", "attempt", "August", "Autumn", "border", "breeze", "brick", "calm",
         "canal", "Casey", "cast", "chose", "claws", "coach", "constantly", "contrast", "cookies", "customs", "damage",
         "Danny", "deeply", "depth", "discussion", "doll", "donkey"]


def letter_in_word(word, input_, list_):
    for l in range(len(word)):
        if word[l] == input_:
            list_[l] = input_
            i = l
            while i < len(word):
                if word[i] == input_:
                    list_[i] = input_
                i += 1
            return True
    return False


def play_again():
    response = input("do you wanna play again?")
    while not response.isalpha():
        response = input("do you wanna play again?").lower()

    while not (response == 'n' or response == 'y'):
        response = input("do you wanna play again?").lower()

    if response == 'n':
        exit(0)
    elif response == 'y':
        play_game()


guessed_letters = []


def play_game():
    secret_word = random.choice(words).lower()
    spaces = ["_" for x in range(len(secret_word))]

    print(diagrams[0])
    print(' '.join(spaces))

    guess_count = 0
    while guess_count <= 5:
        if "_" not in spaces:
            print("YEPEEE!!!!..You guessed the correct word")
            play_again()

        letter = input("enter a letter: ")[0]
        # error checking
        while not (letter.isalpha() or letter.islower()):
            letter = input("enter a letter: ")

        while letter in spaces:
            print("That letter is already inserted")
            letter = input("enter a letter: ")

        # checking if the user enters the same letter again
        while letter in guessed_letters:
            print("you have already guessed that letter")
            letter = input("enter a letter: ")

        if letter_in_word(secret_word, letter, spaces):
            print(diagrams[guess_count])
            print(' '.join(spaces))
        else:
            guess_count += 1
            guessed_letters.append(letter)
            if guess_count == 6:
                print(diagrams[guess_count])
                print("OH NOO!!..You ran out of guesses")
                print(f"The secret word was {secret_word}")
                play_again()

            print(diagrams[guess_count])
            print(' '.join(spaces))


play_game()
