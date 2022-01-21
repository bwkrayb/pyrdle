import string
import random
import enchant

def randomWord():
    d = enchant.Dict("en_US")
    randomWord = ''
    stringLength = 5
    i = 0
    while i < stringLength:
        randomChar = random.choice(string.ascii_letters).lower()
        randomWord = randomWord + randomChar
        i += 1
    while d.check(randomWord) == False:
        randomWord = ''
        i = 0
        while i < stringLength:
            randomChar = random.choice(string.ascii_letters).lower()
            randomWord = randomWord + randomChar
            i += 1
    return randomWord;
        
