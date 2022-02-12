import random
import string

print("H A N G M A N")
words = ('python', 'java', 'kotlin', 'javascript')


while True:
    play = None
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        play = True
        attempts = 0
        word = random.choice(words)
        cover = '-' * len(word)
        guesses = set()
        print()
    elif menu == 'exit':
        play = False
        break
    while play and attempts < 8:
        print(cover)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should input a single letter\n")
            continue
        if guess not in string.ascii_lowercase:
            print("Please enter a lowercase English letter\n")
            continue
        if guess in guesses:
            print("You've already guessed this letter\n")
            continue
        guesses.add(guess)
        if guess in word:
            idx = word.index(guess)
            cover = cover[:idx] + guess + cover[idx + 1:]
            if cover == word:
                print(f"\n{word}")
                print("You guessed the word!")
                print("You survived!\n")
                break
            print()
            continue
        else:
            attempts += 1
            if attempts == 8:
                print("That letter doesn't appear in the word")
                print("You lost!\n")
                break
            else:
                print("That letter doesn't appear in the word\n")

