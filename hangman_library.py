def maxWrongAnswersInput():
    while True:
        result = input('Choose the maximum number of wrong guesses: ')
        if not result.isnumeric():
            print('Invalid input')
        else:
            print('You have chosen the maximum number of wrong guesses to be:', result)
            return int(result)       
    
def yesOrNoInput(message):
    while True:
        print(message)
        answer = input('Answer with a Yes [y] or No [n]: ')
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            return True
        elif answer == 'n' or answer == 'no':
            return False
        else:
            print('I\'ll ask you again.')

def readMinimumWordLength(L):
    while True:
        length = input('Choose the minimum length of the hidden word: ')
        if not length.isnumeric():
            print('Invalid input')
        else:
            length = int(length)
            wrongInput = True
            for i in range(len(L)):
                if len(L[i]) >= length:
                    wrongInput = False
                    break
            if wrongInput:
                print('We don\'t know a word larger than', length, 'characters.')
            else:
                return length            

def createList(L, length):
    lengthList = len(L)
    exclude = []            
    print('\n')
    print('Loading...', end='')
                    
    for i in range(lengthList):
        if len(L[i]) < length:
            exclude.append(L[i])
    print('.....', end='')
    if len(exclude) != 0:                
        for i in range(len(exclude)):
            L.remove(exclude[i])
    print('......\n')
    return L

def hangman(word, hidden, maxWrongAnswers):
    wrongAnswers = 0
    visualAid = []
    if hidden:
        visualAid.append('_')
        correctAnswers = 0
    else:
        visualAid.append(word[0])
        correctAnswers = 1
    for i in range(1,len(word)):
        visualAid.append('_')
    while wrongAnswers <= maxWrongAnswers and correctAnswers < len(word):
        for i in range(len(word)):
            print(visualAid[i], end=' ')
        print('\n')
        if wrongAnswers != 0:
            print('You have given ', wrongAnswers, ' wrong answer(s) so far.')
        while True:
            char = input('Guess a character: ')
            if len(char) == 1 and char.isalpha():
                break
            else:
                print('Only one character. If you have found the word, keep writing one character at a time.')
        char = char.lower()
        guess = False
        sameGuess = False
        for i in range(len(word)):
            if char == word[i] and char != visualAid[i]:
                guess = True
                correctAnswers += 1
                visualAid.pop(i)
                visualAid.insert(i,word[i])
            elif char == visualAid[i] and i != 0:
                print('You have chosen again the character ' + char + '.')
                sameGuess = True
                break
        if not guess and not sameGuess:
            wrongAnswers +=1
            print('Wrong guess.')

    if correctAnswers == len(word):
        print('You won!')
    else:
        print('You lost. Try again with a different word.')
    print('The hidden word was ' + word + ' .\n')
            
