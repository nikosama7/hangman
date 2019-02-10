from random import randint
import wordBank
import hangman_library as library
           
print('*****************************************************************************')
print('********************************   HANGMAN   ********************************')
print('*****************************************************************************')
print('****************************   version: 1.2.0   *****************************')
print('*****************************************************************************')
print('********************  Developed by Nikolaos Amartolos ***********************')
print('*****************************************************************************\n')

L = wordBank.wordBank()
length = library.readMinimumWordLength(L)
L = library.createList(L, length)

while True:    
    lengthList = len(L)
    if lengthList == 0:
        print('We don\'t know any other word with length bigger than', length)
        break
    message = 'Do you want the first character of the hidden word to be hidden?'
    hidden = library.yesOrNoInput(message)
    maxWrongAnswers = library.maxWrongAnswersInput()
    radomInt = randint(0, lengthList-1)
    word = L.pop(radomInt)
    print('\n')
    print('Let\'s start the game!\n')
    library.hangman(word, hidden, maxWrongAnswers)
    message = 'Do you want to play another game with the same minimum word length?'
    if not library.yesOrNoInput(message):
        break

print('\nWe hope you will play again anothr time.\n')
print('*****************************************************************************')
print('********************************   HANGMAN   ********************************')
print('*****************************************************************************')

