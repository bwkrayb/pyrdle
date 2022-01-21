def guessWord(randomWord):
    print('-----')
    guessedWord = input()
    if guessedWord == 'quit':
        print("The word was " + randomWord)
        resultString = "You lose."
        return resultString;
    else:
        while len(guessedWord) != 5:
            print("")
            print("You must choose a 5 letter word.")
            print("-----")
            guessedWord = input()
            if guessedWord == 'quit':
                guessedWord = "quit "
                break

        char1 = guessedWord[0]
        char2 = guessedWord[1]
        char3 = guessedWord[2]
        char4 = guessedWord[3]
        char5 = guessedWord[4]
        char1Result = ' '
        char2Result = ' '
        char3Result = ' '
        char4Result = ' '
        char5Result = ' '

        partMatch = '/'
        fullMatch = 'X'

        if char1 == randomWord[0]:
            char1Result = fullMatch
        elif char1 in randomWord:
            char1Result = partMatch

        if char2 == randomWord[1]:
            char2Result = fullMatch
        elif char2 in randomWord:
            char2Result = partMatch

        if char3 == randomWord[2]:
            char3Result = fullMatch
        elif char3 in randomWord:
            char3Result = partMatch

        if char4 == randomWord[3]:
            char4Result = fullMatch
        elif char4 in randomWord:
            char4Result = partMatch

        if char5 == randomWord[4]:
            char5Result = fullMatch
        elif char5 in randomWord:
            char5Result = partMatch

        resultString = char1Result + char2Result + char3Result + char4Result + char5Result
    
        if guessedWord == randomWord:
            resultString = "You win!" 

        return resultString;
