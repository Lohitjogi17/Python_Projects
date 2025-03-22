# Anagrams Game: Build a Scrambled Word Game using Python

import random

words=["ironman","thor","hawkeye","wanda","vision"]

word = random.choice(words)

jumble= "".join(random.sample(word,len(word)))
chances = 3

print("~"*33)
print("~~~~~Avengers Jumble Bumble ~~~~~")
print("~"*33)


while chances!=0:
    print("the word is",jumble)

    guess = input("enter your guessed word").lower()

    if guess == word:
        print("Correct Guess!!")
        print("You won")
        print()
        break

    else:
        chances -= 1
        print("Incorrect Guess!!")
        print("Remaining chances are",chances)
        print()
else:
    print("all your chances are exhausted")
    print("you loose")
    print("the correct word is",word)

print("thank you for playing")
    
        
        





