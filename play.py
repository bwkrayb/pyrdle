from random_word import randomWord
from guess_word import guessWord

print("Welcome to pyrdle!")
print("To play:")
print("    Guess a 5 letter word. If a character matches ")
print("in the exact spot, there will be an X under that c")
print("haracter. If character is in the random word, but ")
print("not in that particular spot, there will be an / un")
print("der that character. If the letter does not match a")
print("t all, there will be nothing.")
print("")
print("To quit, type quit for any guess.")
print("")
print("Enter your 5 letter word.")
randomStr = randomWord()
#print(randomStr)

guessStr = guessWord(randomStr)

print(guessStr)

while guessStr != "You win!":
    if guessStr == "You lose.":
        break
    print("")
    print("Try again!")
    guessStr = guessWord(randomStr)
    print(guessStr)
    #print("answer: " + randomStr)


