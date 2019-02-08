from random import choice

def hangman(L):
    wrongAnswers = 0
    correctAnswers = 1
    word = choice(L)
    visualAid = []
    visualAid.append(word[0])
    
    for i in range(1,len(word)):
        visualAid.append('_')
    print(visualAid)
    while wrongAnswers <= 6 and correctAnswers < len(word):
        if wrongAnswers != 0:
            print('You have given ', wrongAnswers, ' wrong answers so far.')
        doubleChar = True
        while doubleChar:
            char = input('Guess a character: ')
            if len(char) == 1:
                doubleChar = False
            else:
                print('Only one character. If you have found the word, keep writing one character at a time.')
        char = char.lower()
        guess = False
        for i in range(1, len(word)):
            if char == word[i] and char != visualAid[i]:
                guess = True
                correctAnswers += 1
                visualAid.pop(i)
                visualAid.insert(i,word[i])
            elif char == visualAid[i]:
                print('You have again the character ' + char + '.')
        if not guess:
            wrongAnswers +=1
            print('Wrong guess.')
        print(visualAid)
    if correctAnswers == len(word):
        print('You won!')
    else:
        print('You lost. Try another time.')
        print('The hidden word was ' + word + ' .')
            
            
print('*****************************************************************************')
print('********************************   HANGMAN   ********************************')
print('*****************************************************************************')
print('****************************   version: 0.9.1   *****************************')
print('*****************************************************************************')
print('********************  Developed by Nikos Amartolos **************************')
print('*****************************************************************************\n')
print('You have 6 attempts to find the word. Let\'s start the game!\n')

again = True
L = ['abandon', 'ability', 'able', 'abortion', 'about', 'above', 'abroad', 'absence', 'absolute', 'absolutely',
'absorb', 'abuse', 'academic', 'accept', 'access', 'accident', 'accompany', 'accomplish', 'according',
'account', 'accurate', 'accuse', 'achieve', 'achievement', 'acid', 'acknowledge', 'acquire', 'across', 'action', 'active',
'activist', 'activity', 'actor', 'actress', 'actual', 'actually', 'adapt', 'addition', 'additional', 'address', 'adequate',
'adjust', 'adjustment', 'administration', 'administrator', 'admire', 'admission', 'admit', 'adolescent', 'adopt', 'adult',
'advance', 'advanced', 'advantage', 'adventure', 'advertising', 'advice', 'advise', 'adviser', 'advocate', 'affair', 'affect',
'afford', 'afraid', 'afternoon', 'again', 'against', 'agency', 'agenda', 'agent', 'aggressive', 'agree', 'agreement', 'agricultural',
'ahead', 'aide', 'aircraft', 'airline', 'airport', 'album', 'alcohol', 'alive', 'alliance', 'allow', 'ally', 'almost', 'alone',
'along', 'already', 'alter', 'alternative', 'although', 'always', 'amazing', 'among', 'amount', 'analysis', 'analyst', 'analyze',
'ancient', 'anger', 'angle', 'angry', 'animal', 'anniversary', 'announce', 'annual', 'another', 'answer', 'anticipate', 'anxiety',
'anybody', 'anymore', 'anyone', 'anything', 'anyway', 'anywhere', 'apart', 'apartment', 'apparent', 'apparently', 'appeal', 'appear',
'appearance', 'apple', 'application', 'apply', 'appoint', 'appointment', 'appreciate', 'approach', 'appropriate', 'approval',
'approve', 'approximately', 'architect', 'area', 'argue', 'argument', 'arise', 'armed', 'army', 'around', 'arrange', 'arrangement',
'arrest', 'arrival', 'arrive', 'article', 'artist', 'artistic', 'aside', 'asleep', 'aspect', 'assault', 'assert', 'assess', 'assessment',
'asset', 'assign', 'assignment', 'assist', 'assistance', 'assistant', 'associate', 'association', 'assume','assumption', 'assure',
'athlete', 'athletic', 'atmosphere', 'attach', 'attack', 'attempt', 'attend', 'attention', 'attitude', 'attorney', 'attract', 'attractive',
'attribute', 'audience', 'author', 'authority', 'available', 'average', 'avoid', 'award', 'aware', 'awareness', 'away', 'awful', 'background',
'badly', 'balance', 'barely', 'barrel', 'barrier', 'baseball', 'basic', 'basically', 'basis', 'basket', 'basketball', 'bathroom',
'battery', 'battle', 'beach', 'bean', 'bear', 'beat', 'beautiful', 'beauty', 'because', 'become', 'bedroom', 'beer', 'before', 'begin',
'beginning', 'behavior', 'behind', 'being', 'belief', 'believe', 'bell', 'belong', 'below', 'belt', 'bench', 'bend', 'beneath', 'benefit',
'beside', 'besides', 'best', 'better', 'between', 'beyond', 'billion', 'bind', 'biological', 'birth', 'birthday', 'black', 'blade', 'blame',
'blanket', 'blind', 'block', 'blood', 'board', 'bombing', 'bond', 'border', 'born', 'borrow', 'bother', 'bottle', 'bottom', 'boundary',
'boyfriend', 'brain', 'branch', 'brand', 'bread', 'break', 'breakfast', 'breast', 'breath', 'breathe', 'brick', 'bridge', 'brief', 'briefly',
'bright', 'brilliant', 'bring', 'broad', 'broken', 'brother', 'brown', 'brush', 'buck', 'budget', 'build', 'building', 'bullet', 'bunch',
'burden', 'burn', 'bury', 'business', 'butter', 'button', 'cabin', 'cabinet', 'cable', 'cake', 'calculate', 'camera', 'campaign', 'campus',
'cancer', 'candidate', 'capability', 'capable', 'capacity', 'capital', 'captain', 'capture', 'carbon', 'career', 'careful', 'carefully',
'carrier', 'carry', 'case', 'cash', 'catch', 'category', 'cause', 'ceiling', 'celebrate', 'celebration', 'celebrity', 'cell', 'center',
'central', 'century', 'ceremony', 'certain', 'certainly', 'chain', 'chair', 'chairman', 'challenge', 'chamber', 'champion', 'championship',
'chance', 'change', 'changing', 'channel', 'chapter', 'character', 'characteristic', 'characterize', 'charge', 'charity', 'chart', 'chase',
'cheap', 'check', 'cheek', 'cheese', 'chemical', 'chest','chicken', 'chief', 'children', 'childhood', 'chocolate', 'choice', 'cholesterol'
'choose', 'church', 'cigarette', 'circle', 'circumstance', 'citizen', 'civil', 'civilian', 'claim', 'class', 'classic', 'classroom', 'clearly',
'client', 'climate', 'climb', 'clinic', 'clinical', 'closely', 'closer', 'clothes', 'clothing', 'cloud', 'cluster', 'coach', 'coalition', 'coast',
'coat', 'code', 'coffee', 'cognitive', 'collapse', 'colleague', 'collect', 'collection', 'collective', 'college', 'colonial', 'color', 'column',
'combination', 'combine', 'comedy', 'comfort', 'comfortable', 'command', 'commander', 'comment', 'commercial', 'commission', 'commit',
'commitment', 'committee', 'common', 'communicate', 'communication', 'community', 'company', 'compare', 'comparison', 'compete', 'competition',
'competitive', 'competitor', 'complain', 'complaint', 'complete', 'completely', 'complex', 'complicated', 'component', 'compose', 'composition',
'comprehensive', 'computer', 'concentrate', 'concentration', 'concept', 'concern', 'concerned', 'concert', 'conclude', 'conclusion', 'concrete',
'condition', 'conduct', 'conference', 'confidence', 'confident', 'confirm', 'conflict', 'confront', 'confusion', 'congressional', 'connect',
'connection', 'consciousness', 'consensus', 'consequence', 'conservative', 'consider', 'considerable', 'consideration', 'consist', 'consistent',
'constant', 'constantly', 'constitute', 'constitutional', 'construct', 'construction', 'consultant', 'consume', 'consumer', 'consumption', 'contact',
'contain', 'container', 'contemporary', 'content', 'contest', 'context', 'continue', 'continued', 'contract', 'contrast', 'contribute',
'contribution', 'control', 'controversial', 'controversy', 'convention', 'conventional', 'conversation', 'convert', 'conviction', 'convince',
'cookie', 'cooking', 'cooperation', 'corner', 'corporate', 'corporation', 'correct', 'correspondent', 'cotton', 'couch', 'could', 'council',
'counselor', 'count', 'counter', 'country', 'county', 'couple', 'courage', 'course', 'court', 'cousin', 'cover', 'coverage', 'crack', 'craft',
'crash', 'crazy', 'cream', 'create', 'creation', 'creative', 'creature', 'credit', 'criminal', 'crisis', 'criteria', 'critic', 'critical',
'criticism', 'criticize', 'crucial', 'cultural', 'culture', 'curious', 'current', 'currently', 'curriculum', 'custom', 'customer']

while again:
    wrong = True
    hangman(L)
    while wrong:
        print('Do you want to play an other game? ')
        play = input('Answer with a Yes [y] or No [n]: ')
        if play.lower() == 'y' or play.lower() == 'yes':
            again = True
            wrong = False
        elif play.lower() == 'n' or play.lower() == 'no':
            again = False
            wrong = False
            print('\n')
            print('We hope you will play again anothr time.\n')
            print('*****************************************************************************')
            print('********************************   HANGMAN   ********************************')
            print('*****************************************************************************')
        else:
            print('I\'ll ask you again.')

