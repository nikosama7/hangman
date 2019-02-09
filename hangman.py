from random import randint

def hangman(word, hidden):
    wrongAnswers = 0
    correctAnswers = 1
    visualAid = []
    if hidden:
        visualAid.append('_')
    else:
        visualAid.append(word[0])
    for i in range(1,len(word)):
        visualAid.append('_')
    while wrongAnswers <= 6 and correctAnswers < len(word):
        for i in range(len(word)):
            print(visualAid[i], end=' ')
        print('\n')
        if wrongAnswers != 0:
            print('You have given ', wrongAnswers, ' wrong answers so far.')
        doubleChar = True
        notChar = True
        while doubleChar or notChar:
            char = input('Guess a character: ')
            if len(char) == 1 and char.isalpha():
                doubleChar = False
                notChar = False
            else:
                print('Only one character. If you have found the word, keep writing one character at a time.')
        char = char.lower()
        guess = False
        sameGuess = False
        for i in range(1, len(word)):
            if char == word[i] and char != visualAid[i]:
                guess = True
                correctAnswers += 1
                visualAid.pop(i)
                visualAid.insert(i,word[i])
            elif char == visualAid[i]:
                print('You have chosen again the character ' + char + '.')
                sameGuess = True
                break
        if not guess and not sameGuess:
            wrongAnswers +=1
            print('Wrong guess.')

    if correctAnswers == len(word):
        print('You won!\n')
    else:
        print('You lost. Try another time.')
        print('The hidden word was ' + word + ' .\n')
            
            
print('*****************************************************************************')
print('********************************   HANGMAN   ********************************')
print('*****************************************************************************')
print('****************************   version: 1.1.0   *****************************')
print('*****************************************************************************')
print('********************  Developed by Nikos Amartolos **************************')
print('*****************************************************************************\n')

wrongInput = True
again = True

L = ['abandon', 'ability', 'able', 'abortion', 'about', 'above', 'abroad', 'absence', 'absolute', 'absolutely', 'absorb', 'abuse', 'academic', 'accept', 'access',
'accident', 'accompany', 'accomplish', 'according', 'account', 'accurate', 'accuse', 'achieve', 'achievement', 'acid', 'acknowledge', 'acquire', 'across', 'action',
'active', 'activist', 'activity', 'actor', 'actress', 'actual', 'actually', 'adapt', 'addition', 'additional', 'address', 'adequate',
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
'cheap', 'check', 'cheek', 'cheese', 'chemical', 'chest','chicken', 'chief', 'children', 'childhood', 'chocolate', 'choice', 'cholesterol',
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
'criticism', 'criticize', 'crucial', 'cultural', 'culture', 'curious', 'current', 'currently', 'curriculum', 'custom', 'customer', 'daily',
'damage', 'dance', 'danger', 'dangerous', 'dare', 'darkness', 'daughter', 'deal', 'dealer', 'dear', 'death', 'debate', 'debt', 'decade', 'decide',
'decision', 'deck', 'declare', 'decline', 'decrease', 'deep', 'deeply', 'deer', 'defeat', 'defend', 'defendant', 'defense', 'defensive', 'deficit',
'define', 'definitely', 'definition', 'degree', 'delay', 'deliver', 'delivery', 'demand', 'democracy', 'democratic', 'demonstrate', 'demonstration',
'department', 'depend', 'dependent', 'depending', 'depict', 'depression', 'depth', 'deputy', 'derive', 'describe', 'description', 'desert', 'deserve',
'design', 'designer', 'desire', 'desperate', 'despite', 'destroy', 'destruction', 'detail', 'detailed', 'detect', 'determine', 'develop', 'development',
'device', 'devote', 'dialogue', 'differ', 'difference', 'different', 'differently', 'difficult', 'difficulty', 'digital', 'dimension', 'dining', 'dinner',
'direct', 'direction', 'directly', 'director', 'dirty', 'disability', 'disagree', 'disappear', 'disaster', 'discipline', 'discourse', 'discover',
'discovery', 'discrimination', 'discuss', 'discussion', 'disease', 'dish', 'dismiss', 'disorder', 'display', 'dispute', 'distance', 'distant', 'distinct',
'distinction', 'distinguish', 'distribute', 'distribution', 'district', 'diverse', 'diversity', 'divide', 'division', 'divorce', 'doctor', 'document',
'domestic', 'dominant', 'dominate', 'double', 'doubt', 'downtown', 'dozen', 'draft', 'drag', 'drama', 'dramatic', 'dramatically', 'draw', 'drawing', 'dream',
'dress', 'drink', 'drive', 'driver', 'drop', 'drug', 'during', 'dust', 'duty', 'each', 'eager', 'early', 'earn', 'earnings', 'earth', 'ease', 'easily',
'east', 'eastern', 'economic', 'economics', 'economist', 'economy', 'edge', 'edition', 'editor', 'educate', 'education', 'educational', 'educator', 'effect',
'effective', 'effectively', 'efficiency', 'efficient', 'effort', 'either', 'elderly', 'elect', 'election', 'electric', 'electricity', 'electronic', 'element',
'elementary', 'eliminate', 'elite', 'elsewhere', 'embrace', 'emerge', 'emergency', 'emission', 'emotion', 'emotional', 'emphasis', 'emphasize', 'employ',
'employee', 'employer', 'employment', 'empty', 'enable', 'encounter', 'encourage', 'enemy', 'energy', 'enforcement', 'engage', 'engine', 'engineer',
'engineering', 'enhance', 'enjoy', 'enormous', 'enough', 'ensure', 'enter', 'enterprise', 'entertainment', 'entire', 'entirely', 'entrance', 'entry',
'environment', 'environmental', 'episode', 'equal', 'equally', 'equipment', 'error', 'escape', 'especially', 'essay', 'essential', 'essentially', 'establish',
'establishment', 'estate', 'estimate', 'ethics', 'ethnic', 'evaluate', 'evaluation', 'even', 'evening', 'event', 'eventually', 'every', 'everybody', 'everyday',
'everyone', 'everything', 'everywhere', 'evidence', 'evolution', 'evolve', 'exact', 'exactly', 'examination', 'examine', 'example', 'exceed', 'excellent',
'except', 'exception', 'exchange', 'exciting', 'executive', 'exercise', 'exhibit', 'exhibition', 'exist', 'existence', 'existing', 'expand', 'expansion', 'expect',
'expectation', 'expense', 'expensive', 'experience', 'experiment', 'expert', 'explain', 'explanation', 'explode', 'explore', 'explosion', 'expose', 'exposure',
'express', 'expression', 'extend', 'extension', 'extensive', 'extent', 'external', 'extra', 'extraordinary', 'extreme', 'extremely', 'fabric', 'facility', 'fact',
'factor', 'factory', 'faculty', 'failure', 'fairly', 'faith', 'false', 'familiar', 'family', 'famous', 'fantasy', 'farmer', 'fashion', 'fate', 'father', 'fault',
'favor', 'favourite', 'fear', 'feature', 'federal', 'feed', 'feel', 'feeling', 'fellow', 'female', 'fence', 'fiber', 'fiction', 'field', 'fight', 'fighter',
'fighting', 'figure', 'file', 'final', 'finally', 'finance', 'financial', 'finding', 'finger', 'finish', 'fire', 'fishing', 'fitness', 'flame', 'flat', 'flavor',
'flee', 'flesh', 'flight', 'float', 'floor', 'flower', 'focus', 'folk', 'follow', 'following', 'football', 'force', 'foreign', 'forest', 'forever', 'forget', 'form',
'formal', 'formation', 'former', 'formula', 'fortune', 'forward', 'found', 'foundation', 'founder', 'frame', 'framework', 'free', 'freedom', 'freeze', 'frequency',
'frequent', 'frequently', 'fresh', 'friend', 'friendly', 'friendship', 'front', 'fruit', 'frustration', 'fuel', 'fully', 'function', 'fund', 'fundamental',
'funding', 'funeral', 'funny', 'furniture', 'furthermore', 'future', 'gain', 'galaxy', 'gallery', 'game', 'gang', 'garage', 'garden', 'garlic', 'gate', 'gather',
'gaze', 'gear', 'gender', 'gene', 'general', 'generally', 'generate', 'generation', 'genetic', 'gentleman', 'gently', 'gesture', 'ghost', 'giant', 'gift', 'gifted',
'girlfriend', 'give', 'glad', 'glance', 'glass', 'global', 'glove', 'golden', 'golf', 'government', 'governor', 'grab', 'grade', 'gradually', 'graduate', 'grain'
'grand', 'grandfather', 'grandmother', 'grant', 'grass', 'grave', 'great', 'greatest', 'grocery', 'ground', 'group', 'grow', 'growing', 'growth', 'guarantee',
'guard', 'guess', 'guest', 'guide', 'guideline', 'guilty', 'habit', 'habitat', 'hall', 'hand', 'handful', 'handle', 'hang', 'happen', 'happy', 'hard', 'hardly', 'hate',
'head', 'headline', 'headquarters', 'health', 'healthy', 'hearing', 'heart', 'heat', 'heaven', 'heavily', 'heavy', 'heel', 'height', 'helicopter', 'helpful',
'heritage', 'hero', 'hide', 'high', 'highlight', 'highly', 'highway', 'hill', 'historian', 'historic', 'historical', 'history', 'hold', 'hole', 'holiday', 'home',
'homeless', 'honest', 'honey', 'honor', 'hope', 'horizon', 'horror', 'horse', 'hospital', 'host', 'hotel', 'house', 'household', 'housing', 'however', 'huge', 'human',
'humor', 'hundred', 'hungry', 'hunter', 'hunting', 'hurt', 'husband', 'hypothesis', 'ideal', 'identification', 'identify', 'identity', 'ignore', 'illegal', 'illness',
'illustrate', 'image', 'imagination', 'imagine', 'immediate', 'immediately', 'immigrant', 'immigration', 'impact', 'implement', 'implication', 'imply', 'importance',
'important', 'impose', 'impossible', 'impress', 'impression', 'impressive', 'improve', 'improvement', 'incentive', 'incident', 'include', 'including', 'income',
'incorporate', 'increase', 'increased', 'increasing', 'increasingly', 'incredible', 'indeed', 'independence', 'independent', 'index', 'indicate', 'indication',
'individual', 'industrial', 'industry', 'infant', 'infection', 'inflation', 'influence', 'inform', 'information', 'ingredient', 'initial', 'initially', 'initiative',
'injury', 'inner', 'innocent', 'inquiry', 'inside', 'insight', 'insist', 'inspire', 'install', 'instance', 'instead', 'institution', 'institutional', 'instruction',
'instructor', 'instrument', 'insurance', 'intellectual', 'intelligence', 'intend', 'intense', 'intensity', 'intention', 'interaction', 'interest', 'interested',
'interesting', 'internal', 'international', 'Internet', 'interpret', 'interpretation', 'intervention', 'interview', 'introduce', 'introduction', 'invasion', 'invest',
'investigate', 'investigation', 'investigator', 'investment', 'investor', 'invite', 'involve', 'involved', 'involvement', 'iron', 'island', 'issue', 'item', 'jacket',
'jail', 'joint', 'joke', 'journal', 'journalist', 'journey', 'judge', 'judgment', 'juice', 'jump', 'junior', 'jury', 'justice', 'justify', 'keep', 'kick', 'killer',
'killing', 'king', 'kiss', 'kitchen', 'knee', 'knife', 'knock', 'knowledge', 'label', 'labor', 'laboratory', 'lack', 'landscape', 'language', 'large', 'largely',
'latter', 'laugh', 'launch', 'lawn', 'lawsuit', 'lawyer', 'layer', 'leader', 'leadership', 'leading', 'leaf', 'league', 'lean', 'learn', 'learning', 'least', 'leather',
'leave', 'legacy', 'legal', 'legend', 'legislation', 'legitimate', 'lemon', 'length', 'lesson', 'letter', 'level', 'liberal', 'library', 'license', 'lifestyle',
'lifetime', 'lift', 'light', 'likely', 'limit', 'limitation', 'limited', 'line', 'link', 'listen', 'literally', 'literary', 'literature', 'little', 'living', 'load',
'loan', 'local', 'locate', 'location', 'loose', 'lose', 'loss', 'lost', 'loud', 'lovely', 'lover', 'luckily', 'lucky', 'lunch', 'lung', 'machine', 'magazine', 'main',
'mainly', 'maintain', 'maintenance', 'major', 'majority', 'maker', 'manage', 'management', 'manager', 'manner', 'manufacturer', 'manufacturing', 'margin', 'marketing',
'marriage', 'married', 'marry', 'mask', 'mass', 'massive', 'master', 'match', 'material', 'matter', 'mayor', 'meal', 'meaning', 'meanwhile', 'measure', 'measurement',
'meat', 'mechanism', 'media', 'medical', 'medication', 'medicine', 'medium', 'meeting', 'member', 'membership', 'memory', 'mental', 'mention', 'merely', 'mess',
'message', 'metal', 'method', 'middle', 'military', 'milk', 'million', 'mind', 'mine', 'minister', 'minor', 'minority', 'minute', 'miracle', 'mirror', 'miss', 'missile',
'mission', 'mistake', 'mixture', 'mode', 'model', 'moderate', 'modern', 'modest', 'moment', 'money', 'monitor', 'month', 'mood', 'moral', 'moreover', 'morning',
'mortgage' , 'mostly', 'mother', 'motion', 'motivation', 'motor', 'mount', 'mountain', 'mouse', 'mouth', 'movement', 'multiple', 'murder', 'muscle', 'museum', 'musical',
'musician', 'mutual', 'mystery', 'myth', 'naked', 'name', 'narrative', 'narrow', 'nation', 'national', 'native', 'natural', 'naturally', 'nature', 'near', 'nearby',
'nearly', 'necessarily', 'necessary', 'neck', 'need', 'negative', 'negotiate', 'negotiation', 'neighbor', 'neighborhood', 'neither', 'nerve', 'nervous', 'network',
'nevertheless', 'newly', 'newspaper', 'night', 'nobody', 'noise', 'nomination', 'nonetheless', 'normal', 'normally', 'north', 'northern', 'nose', 'nothing', 'notice',
'notion', 'novel', 'nowhere', 'nuclear', 'number', 'numerous', 'nurse', 'object', 'objective', 'obligation', 'observation', 'observe', 'observer', 'obtain', 'obvious',
'obviously', 'occasion', 'occasionally', 'occupation', 'occupy', 'occur', 'ocean', 'odds', 'offense', 'offensive', 'offer', 'office', 'officer', 'official', 'often',
'ongoing', 'onion', 'online', 'opening', 'operate', 'operating', 'operation', 'operator', 'opinion', 'opponent', 'opportunity', 'oppose', 'opposite', 'opposition',
'option', 'order', 'ordinary', 'organic', 'organization', 'organize', 'orientation', 'origin', 'original', 'originally', 'other', 'otherwise', 'ought', 'outcome',
'outside', 'oven', 'overall', 'overcome', 'overlook', 'package', 'page', 'painful', 'paint', 'painter', 'painting', 'pair', 'pale', 'panel', 'paper', 'parent',
'parking', 'participant', 'participate', 'participation', 'particular', 'particularly', 'partly', 'partner', 'partnership', 'party', 'passage', 'passenger', 'passion',
'patch', 'path', 'patient', 'pattern', 'pause', 'payment', 'peace', 'peak', 'peer', 'penalty', 'people', 'pepper', 'perceive', 'percentage', 'perception', 'perfect',
'perfectly', 'perform', 'performance', 'perhaps', 'period', 'permanent', 'permission', 'permit', 'person', 'personal', 'personality', 'personally', 'personnel',
'perspective', 'persuade', 'phase', 'phenomenon', 'philosophy', 'photograph', 'photographer', 'phrase', 'physical', 'physically', 'physician', 'piano', 'picture',
'piece', 'pile', 'pilot', 'pine', 'pitch', 'place', 'planet', 'planning', 'plant', 'plastic', 'plate', 'platform', 'play', 'player', 'please', 'pleasure', 'plenty',
'pocket', 'poem', 'poetry', 'point', 'pole', 'police', 'policy', 'political', 'politically', 'politician', 'politics', 'pollution', 'popular', 'population', 'porch',
'portion', 'portrait', 'portray', 'pose', 'position', 'positive', 'possess', 'possibility', 'possible', 'possibly', 'potato', 'potential', 'potentially', 'pound',
'pour', 'poverty', 'powder', 'power', 'powerful', 'practical', 'practice', 'pray', 'prayer', 'precisely', 'predict', 'prefer', 'preference', 'pregnancy', 'pregnant',
'preparation', 'prepare', 'prescription', 'presence', 'present', 'presentation', 'preserve', 'president', 'presidential', 'press', 'pressure', 'pretend', 'pretty',
'prevent', 'previous', 'previously', 'price', 'pride', 'priest', 'primarily', 'primary', 'prime', 'principal', 'principle', 'print', 'prior', 'priority', 'prison',
'prisoner', 'privacy', 'private', 'probably', 'problem', 'procedure', 'proceed', 'process', 'produce', 'producer', 'product', 'production', 'profession', 'professional',
'professor', 'profile', 'profit', 'program', 'progress', 'project', 'prominent', 'promise', 'promote', 'prompt', 'proof', 'proper', 'properly', 'property', 'proportion',
'proposal', 'propose', 'proposed', 'prosecutor', 'prospect', 'protect', 'protection', 'protein', 'protest', 'proud', 'prove', 'provide', 'provider', 'province',
'provision', 'psychological', 'psychologist', 'psychology', 'public', 'publication', 'publicly', 'publish', 'publisher', 'punishment', 'purchase', 'pure', 'purpose',
'pursue', 'qualify', 'quality', 'quarter', 'quarterback', 'question', 'quick', 'quickly', 'quiet', 'quietly', 'quite', 'quote', 'racial', 'radical', 'radio', 'rail',
'raise', 'range', 'rank', 'rapid', 'rapidly', 'rarely', 'rate', 'rather', 'rating', 'ratio', 'reach', 'react', 'reaction', 'reader', 'reading', 'ready', 'real',
'reality', 'realize', 'really', 'reason', 'reasonable', 'recall', 'receive', 'recent', 'recently', 'recipe', 'recognition', 'recognize', 'recommend', 'recommendation',
'record', 'recording', 'recover', 'recovery', 'recruit', 'reduce', 'reduction', 'refer', 'reference', 'reflect', 'reflection', 'reform', 'refugee', 'refuse', 'regard',
'regarding', 'regardless', 'regime', 'region', 'regional', 'register', 'regular', 'regularly', 'regulate', 'regulation', 'reinforce', 'reject', 'relate', 'relation',
'relationship', 'relative', 'relatively', 'relax', 'release', 'relevant', 'relief', 'religion', 'religious', 'rely', 'remain', 'remaining', 'remarkable', 'remember',
'remind', 'remote', 'remove', 'repeat', 'repeatedly', 'replace', 'reply', 'report', 'reporter', 'represent', 'representation', 'representative', 'reputation',
'request', 'require', 'requirement', 'research', 'researcher', 'resemble', 'reservation', 'resident', 'resist', 'resistance', 'resolution', 'resolve', 'resort',
'resource', 'respect', 'respond', 'respondent', 'response', 'responsibility', 'responsible', 'restaurant', 'restore', 'restriction', 'result', 'retain', 'retire',
'retirement', 'return', 'reveal', 'revenue', 'review', 'revolution', 'rhythm', 'rifle', 'right', 'river', 'romantic', 'root', 'rope', 'rough', 'roughly', 'round',
'route', 'routine', 'running', 'rural', 'sacred', 'safety', 'sake', 'salad', 'salary', 'sample', 'sanction', 'sand', 'satellite', 'satisfaction', 'satisfy', 'sauce',
'saving', 'scale', 'scandal', 'scared', 'scenario', 'scene', 'schedule', 'scheme', 'scholar', 'scholarship', 'school', 'science', 'scientific', 'scientist', 'scope',
'score', 'scream', 'screen', 'script', 'search', 'season', 'seat', 'secret', 'secretary', 'section', 'sector', 'secure', 'security', 'seed', 'seek', 'seem', 'segment',
'seize', 'select', 'selection', 'senator', 'send', 'senior', 'sense', 'sensitive', 'sentence', 'separate', 'sequence', 'series', 'serious', 'seriously', 'serve',
'service', 'session', 'setting', 'settle', 'settlement', 'several', 'severe', 'sexual', 'shade', 'shadow', 'shake', 'shape', 'share', 'sharp', 'sheet', 'shelf',
'shell', 'shelter', 'shift', 'shine', 'ship', 'shirt', 'shock', 'shoot', 'shooting', 'shopping', 'shore', 'short', 'shortly', 'shot', 'shoulder', 'shout', 'show',
'shower', 'shrug', 'sick', 'side', 'sigh', 'sight', 'sign', 'signal', 'significance', 'significant', 'significantly', 'silence', 'silent', 'silver', 'similar',
'similarly', 'simple', 'simply', 'singer', 'single', 'situation', 'slave', 'sleep', 'slice', 'slide', 'slight', 'slightly', 'slip', 'slow', 'slowly', 'small', 'smart',
'smell', 'smile', 'smoke', 'smooth', 'snap', 'soccer', 'social', 'society', 'software', 'soil', 'solar', 'soldier', 'solid', 'solution', 'somebody', 'somehow',
'someone', 'something', 'sometimes', 'somewhat', 'somewhere', 'sophisticated', 'sorry', 'sort', 'soul', 'sound', 'soup', 'source', 'south', 'southern', 'space', 'speak',
'speaker', 'special', 'specialist', 'species', 'specific', 'specifically', 'speech', 'speed', 'spend', 'spending', 'spin', 'spirit', 'spiritual', 'split',
'spokesman', 'sport', 'spot', 'spread', 'spring', 'square', 'squeeze', 'stability', 'stable', 'staff', 'stage', 'stair', 'stake', 'stand', 'standard', 'standing',
'star', 'stare', 'start', 'state', 'statement', 'station', 'statistics', 'status', 'stay', 'steady', 'steal', 'steel', 'step', 'stick', 'still', 'stir', 'stock',
'stomach', 'stone', 'stop', 'storage', 'store', 'storm', 'story', 'straight', 'strange', 'stranger', 'strategic', 'strategy', 'stream', 'street', 'strength',
'strengthen', 'stress', 'stretch', 'strike', 'string', 'strip', 'stroke', 'strong', 'strongly', 'structure', 'struggle', 'student', 'studio', 'study', 'stuff', 'stupid',
'style', 'subject', 'submit', 'subsequent', 'substance', 'substantial', 'succeed', 'success', 'successful', 'successfully', 'sudden', 'suddenly', 'suffer', 'sufficient',
'sugar', 'suggest', 'suggestion', 'suicide', 'suit', 'summer', 'summit', 'supply', 'support', 'supporter', 'suppose', 'supposed', 'surely', 'surface', 'surgery',
'surprise', 'surprised', 'surprising', 'surprisingly', 'surround', 'survey', 'survival', 'survive', 'survivor', 'suspect', 'sustain', 'swear', 'sweep', 'sweet', 'swing',
'switch', 'symbol', 'symptom', 'system', 'table', 'tablespoon', 'tactic', 'tail', 'tale', 'talent', 'tank', 'tape', 'target', 'task', 'taste', 'taxpayer', 'teach',
'teacher', 'teaching', 'team', 'tear', 'teaspoon', 'technical', 'technique', 'technology', 'teenager', 'telephone', 'telescope', 'television', 'temperature', 'temporary',
'tendency', 'tennis', 'tension', 'tent', 'term', 'terms', 'terrible', 'territory', 'terror', 'terrorism', 'terrorist', 'testify', 'testimony', 'testing', 'theater',
'theory', 'therapy', 'there', 'therefore', 'thick', 'thing', 'thinking', 'those', 'though', 'thought', 'thousand', 'threat', 'threaten', 'three', 'throat', 'through',
'throughout', 'throw', 'ticket', 'tight', 'tiny', 'tired', 'tissue', 'title', 'tobacco', 'today', 'together', 'tomato', 'tomorrow', 'tongue', 'tonight', 'tooth',
'topic', 'toss', 'total', 'totally', 'touch', 'tough', 'tourist', 'tournament', 'toward', 'towards', 'tower', 'trace', 'track', 'trade', 'tradition', 'traditional',
'traffic', 'tragedy', 'trail', 'train', 'training', 'transfer', 'transform', 'transformation', 'transition', 'translate', 'transportation', 'travel', 'treatment',
'treaty', 'tremendous', 'trend', 'trial', 'tribe', 'trick', 'trip', 'troop', 'trouble', 'truck', 'truly', 'trust', 'truth', 'tunnel', 'type', 'typical', 'typically',
'ugly', 'ultimate', 'ultimately', 'unable', 'uncle', 'under', 'undergo', 'understand', 'understanding', 'unfortunately', 'uniform', 'union', 'unique', 'universal',
'universe', 'university', 'unknown', 'unlike', 'unlikely', 'until', 'unusual', 'urban', 'urge', 'useful', 'user', 'usual', 'usually', 'utility', 'vacation', 'valley',
'valuable', 'value', 'variable', 'variation', 'variety', 'various', 'vary', 'vast', 'vegetable', 'vehicle', 'venture', 'version', 'versus', 'vessel', 'veteran',
'victim', 'victory', 'video', 'viewer', 'village', 'violate', 'violation', 'violence', 'violent', 'virtually', 'virtue', 'virus', 'visible', 'vision', 'visit',
'visitor', 'visual', 'vital', 'voice', 'volume', 'volunteer', 'voter', 'vulnerable', 'wage', 'wake', 'wander', 'warning', 'wash', 'waste', 'watch', 'water', 'weak',
'wealth', 'wealthy', 'weapon', 'wear', 'weather', 'wedding', 'weekend', 'weekly', 'weigh', 'weight', 'welcome', 'welfare', 'western', 'whatever', 'wheel', 'whenever',
'whereas', 'whether', 'whisper', 'widely', 'widespread', 'wild', 'willing', 'window', 'wine', 'wing', 'winner', 'winter', 'wipe', 'wire', 'wisdom', 'wise', 'withdraw',
'witness', 'woman', 'wonder', 'wonderful', 'wooden', 'worker', 'working', 'workshop', 'world', 'worried', 'worry', 'worth', 'wound', 'wrap', 'write', 'writer', 'writing',
'wrong', 'yell', 'yesterday', 'yield', 'young', 'youth', 'zone', 'accoutrements', 'acumen', 'anomalistic', 'bellwether', 'callipygian', 'circumlocution', 'concupiscent',
'conviviality', 'coruscant', 'cuddlesome', 'cupidity', 'cynosure', 'ebullient', 'equanimity', 'excogitate', 'gasconading', 'idiosyncratic', 'luminescent', 'magnanimous',
'nidificate', 'osculator', 'parsimonious', 'penultimate', 'perfidiousness', 'perspicacious', 'proficuous', 'remunerative', 'saxicolous', 'sesquipedalian', 'superabundant',
'unencumbered', 'unparagoned', 'usufruct', 'winebibber', 'zoology', 'zenith', 'yammer', 'wring']

lengthList = len(L)
exclude = []
print('You have 6 attempts to find the word.\n') 
while wrongInput:
    length = input('Firstly, choose the minimum length of the hidden word: ')   #     Let\'s start the game!\n')
    if not length.isnumeric():
        print('Invalid input')
    else:
        length = int(length)
        if length <= 0:
            print('Invalid word length')
        else:
            for i in range(lengthList):
                if len(L[i]) >= length:
                    wrongInput = False
                    break
            if wrongInput:
                print('We don\'t know a word larger than', length, 'characters.') 
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

while True:
    print('Do you want the first character of the hidden word to be hidden?')
    firstLetter = input('Answer with a Yes [y] or No [n]: ')
    firstLetter = firstLetter.lower()
    if firstLetter == 'y' or firstLetter == 'yes':
        hidden = True
        break
    elif firstLetter == 'n' or firstLetter == 'no':
        hidden = False
        break
    else:
        print('I\'ll ask you again.')

print('\n')
print('Let\'s start the game!\n')

while again:
    wrong = True
    lengthList = len(L)
    radomInt = randint(0, lengthList-1)
    word = L.pop(radomInt)
    hangman(word, hidden)
    while wrong:
        print('Do you want to play an other game?')
        play = input('Answer with a Yes [y] or No [n]: ')
        play = play.lower()
        if play == 'y' or play == 'yes':
            again = True
            wrong = False
        elif play == 'n' or play == 'no':
            again = False
            wrong = False
            print('We hope you will play again anothr time.\n')
            print('*****************************************************************************')
            print('********************************   HANGMAN   ********************************')
            print('*****************************************************************************')
        else:
            print('I\'ll ask you again.')



