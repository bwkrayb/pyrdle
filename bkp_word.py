import string
import random
import enchant

d = enchant.Dict("en_US")

def chooseWord():
    stringLength = 5
    randomWord = ''
    i = 0
    while i < stringLength:
        randomChar = random.choice(string.ascii_letters).lower()
        randomWord = randomWord + randomChar
        i += 1
    return randomWord;
        
#randomChar = random.choice(string.ascii_letters).lower()
        

word = chooseWord()

print(word)
print(d.check(word))

while d.check(word) == False:
    word = chooseWord()
else:
    print(word)


#chooseWord()
