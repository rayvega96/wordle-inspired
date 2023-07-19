from Templates.MainWindow import Ui_Wordle, Ui_GameEnded
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from random import randint

WORDLIST = [ 'aback',  'abase',  'abate',  'abaya',  'abbey',  'abbot',  'abets',  'abhor',  'abide',  'abode',  'abort',  'about',  'above',  'abuse',  'abuts',  'abyss',  'ached',  'aches',  'acids',  'acing',  'ackee',  'acorn',  'acres',  'acrid',  'acted',  'actin',  'actor',  'acute',  'adage',  'adapt',  'added',  'adder',  'addle',  'adept',  'adieu',  'adios',  'adits',  'adman',  'admin',  'admit',  'adobe',  'adobo',  'adopt',  'adore',  'adorn',  'adult',  'adzes',  'aegis',  'aeons',  'aerie',  'affix',  'afire',  'afoot',  'afore',  'after',  'again',  'agape',  'agate',  'agave',  'agent',  'aggro',  'agile',  'aging',  'aglow',  'agony',  'agora',  'agree',  'ahead',  'ahold',  'aided',  'aider',  'aides',  'ailed',  'aimed',  'aimer',  'aioli',  'aired',  'aisle',  'alarm',  'album',  'alder',  'aleph',  'alert',  'algae',  'algal',  'alias',  'alibi',  'alien',  'align',  'alike',  'alive',  'alkyd',  'alkyl',  'allay',  'alley',  'allot',  'allow',  'alloy',  'allyl',  'aloes',  'aloft',  'aloha',  'alone',  'along',  'aloof',  'aloud',  'alpha',  'altar',  'alter',  'altos',  'alums',  'amass',  'amaze',  'amber',  'ambit',  'amble',  'ambos',  'amend',  'amide',  'amine',  'amino',  'amiss',  'amity',  'amnio',  'among',  'amour',  'amped',  'ample',  'amply',  'amuse',  'ancho',  'angel',  'anger',  'angle',  'angry',  'angst',  'anima',  'anime',  'anion',  'anise',  'ankle',  'annas',  'annex',  'annoy',  'annul',  'anode',  'anole',  'antic',  'antis',  'antsy',  'anvil',  'aorta',  'apace',  'apart',  'aphid',  'apnea',  'apple',  'apply',  'apron',  'apses',  'apter',  'aptly',  'aquas',  'arbor',  'ardor',  'areal',  'areas',  'areca',  'arena',  'argon',  'argot',  'argue',  'argus',  'arias',  'arils',  'arise',  'armed',  'armor',  'aroma',  'arose',  'array',  'arrow',  'arses',  'arson',  'artsy',  'asana',  'ascot',  'ashen',  'ashes',  'aside',  'asked',  'asker',  'askew',  'aspen',  'aspic',  'assay',  'asses',  'asset',  'aster',  'astir',  'asura',  'atlas',  'atman',  'atoll',  'atoms',  'atone',  'atopy',  'attic',  'audio',  'audit',  'auger',  'aught',  'augur',  'aunts',  'aunty',  'aural',  'auras',  'autos',  'auxin',  'avail',  'avers',  'avert',  'avian',  'avoid',  'avows',  'await',  'awake',  'award',  'aware',  'awash',  'awful',  'awoke',  'axels',  'axial',  'axils',  'axing',  'axiom',  'axion',  'axles',  'axons',  'azide',  'azole',  'azure',  'babel',  'babes',  'babka',  'backs',  'bacon',  'baddy',  'badge',  'badly',  'bagel',  'baggy',  'bails',  'bairn',  'baits',  'baize',  'baked',  'baker',  'bakes',  'baldy',  'baled',  'baler',  'bales',  'balks',  'balky',  'balls',  'balms',  'balmy',  'balsa',  'banal',  'bands',  'bandy',  'banes',  'bangs',  'banjo',  'banks',  'barbs',  'bards',  'bared',  'barer',  'bares',  'barge',  'barks',  'barmy',  'barns',  'baron',  'barre',  'basal',  'based',  'baser',  'bases',  'basic',  'basil',  'basin',  'basis',  'basks',  'basso',  'bassy',  'baste',  'batch',  'bated',  'bathe',  'baths',  'batik',  'baton',  'batts',  'batty',  'bawdy',  'bawls',  'bayed',  'bayou',  'beach',  'beads',  'beady',  'beaks',  'beams',  'beamy',  'beans',  'beard',  'bears',  'beast',  'beats',  'beaus',  'beaut',  'beaux',  'bebop',  'becks',  'beech',  'beefs',  'beefy',  'beeps',  'beers',  'beery',  'beets',  'befit',  'began',  'beget',  'begin',  'begun',  'beige',  'being',  'belay',  'belch',  'belie',  'belle',  'bells',  'belly',  'below',  'belts',  'bench',  'bends',  'bendy',  'bento',  'bents',  'beret',  'bergs',  'berms',  'berry',  'berth',  'beryl',  'beset',  'bests',  'betas',  'betel',  'betta',  'bevel',  'bezel',  'bhaji',  'bible',  'bicep',  'biddy',  'bided',  'bides',  'bidet',  'bight',  'bigot',  'bijou',  'biked',  'biker',  'bikes',  'biles',  'bilge',  'bills',  'billy',  'bimbo',  'bindi',  'binds',  'binge',  'bingo',  'biome',  'biota',  'bipod',  'birch',  'birds',  'birth',  'bison',  'bitch',  'biter',  'bites',  'bitsy',  'bitty',  'black',  'blade',  'blame',  'bland',  'blank',  'blare',  'blase',  'blast',  'blaze',  'bleak',  'bleat',  'blebs',  'bleed',  'bleep',  'blend',  'bless',  'blimp',  'blind',  'bling',  'blini',  'blink',  'blips',  'bliss',  'blitz',  'bloat',  'blobs',  'block',  'blocs',  'blogs',  'bloke',  'blond',  'blood',  'bloom',  'bloop',  'blots',  'blown',  'blows',  'blued',  'blues',  'bluey',  'bluff',  'blunt',  'blurb',  'blurs',  'blurt',  'blush',  'board',  'boars',  'boast',  'boats',  'bobby',  'bocce',  'boche',  'boded',  'bodes',  'boffo',  'bogey',  'boggy',  'bogie',  'bogus',  'boils',  'bolas',  'boles',  'bolls',  'bolts',  'bolus',  'bombe',  'bombs',  'bonds',  'boned',  'boner',  'bones',  'boney',  'bongo',  'bongs',  'bonks',  'bonny',  'bonus',  'boobs',  'booby',  'booed',  'books',  'booms',  'boomy',  'boons',  'boors',  'boost',  'booth',  'boots',  'booty',  'booze',  'boozy',  'boppy',  'borax',  'bored',  'borer',  'bores',  'boric',  'borne',  'boron',  'bosom',  'boson',  'bossy',  'bosun',  'botch',  'bough',  'boule',  'bound',  'bouts',  'bowed',  'bowel',  'bower',  'bowls',  'boxed',  'boxer',  'boxes',  'boyar',  'boyos',  'bozos',  'brace',  'bract',  'brads',  'brags',  'braid',  'brain',  'brake',  'brand',  'brans',  'brash',  'brass',  'brats',  'brave',  'bravo',  'brawl',  'brawn',  'brays',  'braze',  'bread',  'break',  'bream',  'breed',  'brews',  'briar',  'bribe',  'brick',  'bride',  'brief',  'brier',  'brigs',  'brims',  'brine',  'bring',  'brink',  'briny',  'brisk',  'brits',  'broad',  'broch',  'broil',  'broke',  'brome',  'bronc',  'brood',  'brook',  'broom',  'broth',  'brown',  'brows',  'bruin',  'bruit',  'brunt',  'brush',  'brute',  'bubba',  'bucks',  'buddy',  'budge',  'buffs',  'buggy',  'bugle',  'build',  'built',  'bulbs',  'bulge',  'bulks',  'bulky',  'bulla',  'bulls',  'bully',  'bumps',  'bumpy',  'bunch',  'bunds',  'bundt',  'bunks',  'bunny',  'bunts',  'buoys',  'burbs',  'burgs',  'burka',  'burly',  'burns',  'burnt',  'burps',  'burqa',  'burro',  'burrs',  'bursa',  'burst',  'bused',  'buses',  'bushy',  'busts',  'busty',  'butch',  'butte',  'butts',  'buxom',  'buyer',  'buzzy',  'bylaw',  'byres',  'bytes',  'byway',  'cabal',  'cabby',  'caber',  'cabin',  'cable',  'cacao',  'cache',  'cacti',  'caddy',  'cadet',  'cadre',  'cafes',  'caged',  'cages',  'cagey',  'cairn',  'caked',  'cakes',  'cakey',  'calfs',  'calif',  'calla',  'calls',  'calms',  'calve',  'calyx',  'camel',  'cameo',  'campo',  'camps',  'campy',  'canal',  'candy',  'caned',  'canes',  'canid',  'canna',  'canny',  'canoe',  'canon',  'canto',  'caped',  'caper',  'capes',  'capon',  'capos',  'caput',  'carat',  'carbo',  'carbs',  'cards',  'cared',  'carer',  'cares',  'cargo',  'carob',  'carol',  'carom',  'carps',  'carry',  'carte',  'carts',  'carve',  'cased',  'cases',  'casks',  'caste',  'casts',  'catch',  'cater',  'catty',  'caulk',  'cause',  'caved',  'caver',  'caves',  'cavil',  'cease',  'cecal',  'cecum',  'cedar',  'ceded',  'cedes',  'ceili',  'celeb',  'cello',  'cells',  'celts',  'cents',  'chads',  'chafe',  'chaff',  'chain',  'chair',  'chalk',  'champ',  'chana',  'chant',  'chaos',  'chaps',  'chard',  'charm',  'chars',  'chart',  'chase',  'chasm',  'chats',  'cheap',  'cheat',  'check',  'cheek',  'cheep',  'cheer',  'chefs',  'chemo',  'chert',  'chess',  'chest',  'chews',  'chewy',  'chica',  'chick',  'chico',  'chide',  'chief',  'child',  'chile',  'chili',  'chill',  'chime',  'chimp',  'china',  'chine',  'ching',  'chino',  'chins',  'chips',  'chirp',  'chits',  'chive',  'chock',  'choir',  'choke',  'chomp',  'chops',  'chord',  'chore',  'chose',  'chows',  'chubs',  'chuck',  'chuff',  'chugs',  'chump',  'chums',  'chunk',  'churn',  'chute',  'cider',  'cigar',  'cinch',  'circa',  'cisco',  'cited',  'cites',  'civet',  'civic',  'civil',  'civvy',  'clack',  'clade',  'claim',  'clamp',  'clams',  'clang',  'clank',  'clans',  'claps',  'clash',  'clasp',  'class',  'clave',  'claws',  'clays',  'clean',  'clear',  'cleat',  'clefs',  'cleft',  'clerk',  'click',  'cliff',  'climb',  'clime',  'cline',  'cling',  'clink',  'clips',  'cloak',  'clock',  'clods',  'clogs',  'clomp',  'clone',  'close',  'cloth',  'clots',  'cloud',  'clout',  'clove',  'clown',  'clubs',  'cluck',  'clued',  'clues',  'clump',  'clung',  'clunk',  'coach',  'coals',  'coast',  'coati',  'coats',  'cobia',  'cobra',  'cocci',  'cocks',  'cocky',  'cocoa',  'codas',  'codec',  'coded',  'coder',  'codes',  'codex',  'codon',  'coeds',  'cohos',  'coifs',  'coils',  'coins',  'cokes',  'colas',  'colds',  'coles',  'colic',  'colin',  'colon',  'color',  'colts',  'comas',  'combo',  'combs',  'comer',  'comes',  'comet',  'comfy',  'comic',  'comma',  'commo',  'compo',  'comps',  'comte',  'conch',  'condo',  'coned',  'cones',  'conga',  'congo',  'conic',  'conks',  'cooed',  'cooks',  'cools',  'coops',  'coopt',  'coped',  'copes',  'copra',  'copse',  'coral',  'cords',  'cored',  'corer',  'cores',  'corgi',  'corks',  'corky',  'corms',  'corns',  'cornu',  'corny',  'corps',  'costs',  'cotta',  'couch',  'cough',  'could',  'count',  'coupe',  'coups',  'court',  'coven',  'cover',  'coves',  'covet',  'covey',  'cowed',  'cower',  'cowls',  'coyly',  'crabs',  'crack',  'craft',  'crags',  'cramp',  'crams',  'crane',  'crank',  'crape',  'craps',  'crash',  'crass',  'crate',  'crave',  'crawl',  'craws',  'craze',  'crazy',  'creak',  'cream',  'credo',  'creed',  'creek',  'creel',  'creep',  'creme',  'crepe',  'crept',  'cress',  'crest',  'crews',  'cribs',  'crick',  'cried',  'crier',  'cries',  'crime',  'crimp',  'crisp',  'crits',  'croak',  'crock',  'crocs',  'croft',  'crone',  'crony',  'crook',  'croon',  'crops',  'cross',  'croup',  'crowd',  'crown',  'crows',  'crude',  'cruel',  'cruet',  'crumb',  'cruse',  'crush',  'crust',  'crypt',  'cubby',  'cubed',  'cubes',  'cubic',  'cubit',  'cuddy',  'cuffs',  'culls',  'culpa',  'cults',  'cumin',  'cupid',  'cuppa',  'curbs',  'curds',  'cured',  'cures',  'curia',  'curio',  'curls',  'curly',  'curry',  'curse',  'curve',  'curvy',  'cushy',  'cusps',  'cuter',  'cutie',  'cutis',  'cutup',  'cycad',  'cycle',  'cyclo',  'cynic',  'cysts',  'czars',  'dacha',  'daddy',  'dados',  'daffy',  'daily',  'dairy',  'daisy',  'dales',  'dames',  'damns',  'damps',  'dance',  'dandy',  'dared',  'dares',  'darks',  'darns',  'darts',  'dashi',  'dated',  'dater',  'dates',  'datum',  'daubs',  'daunt',  'davit',  'dawns',  'dazed',  'deals',  'dealt',  'deans',  'dears',  'deary',  'death',  'debit',  'debts',  'debug',  'debut',  'decaf',  'decal',  'decay',  'decks',  'decor',  'decoy',  'decry',  'deeds',  'deems',  'deeps',  'deers',  'defer',  'deify',  'deign',  'deism',  'deist',  'deity',  'dekes',  'delay',  'delft',  'delis',  'dells',  'delta',  'delve',  'demon',  'demos',  'demur',  'denim',  'dense',  'dents',  'depot',  'depth',  'derby',  'desks',  'deter',  'detox',  'deuce',  'devil',  'dewar',  'dhikr',  'dhows',  'dials',  'diary',  'diced',  'dices',  'dicey',  'dicky',  'dicta',  'diets',  'digit',  'diked',  'dikes',  'dills',  'dilly',  'dimer',  'dimes',  'dimly',  'dinar',  'dined',  'diner',  'dines',  'dingo',  'dings',  'dingy',  'dinks',  'dinky',  'dinos',  'diode',  'dippy',  'direr',  'dirge',  'dirty',  'disco',  'discs',  'dishy',  'disks',  'ditch',  'ditsy',  'ditto',  'ditty',  'ditzy',  'divan',  'divas',  'dived',  'diver',  'dives',  'divot',  'divvy',  'dizzy',  'docks',  'dodge',  'dodgy',  'dodos',  'doers',  'doffs',  'doges',  'doggy',  'dogma',  'doing',  'doled',  'doles',  'dolls',  'dolly',  'dolor',  'dolts',  'domed',  'domes',  'donee',  'dongs',  'donna',  'donor',  'donut',  'dooms',  'doomy',  'doors',  'doozy',  'doped',  'dopes',  'dopey',  'dorks',  'dorky',  'dorms',  'dosas',  'dosed',  'doses',  'doted',  'dotes',  'dotty',  'doubt',  'dough',  'doula',  'douse',  'doves',  'dowdy',  'dowel',  'dower',  'downs',  'downy',  'dowry',  'dowse',  'doyen',  'dozed',  'dozen',  'dozer',  'dozes',  'drabs',  'draft',  'drags',  'drain',  'drake',  'drama',  'drams',  'drank',  'drape',  'drawl',  'drawn',  'draws',  'drays',  'dread',  'dream',  'dreck',  'dregs',  'dress',  'dribs',  'dried',  'drier',  'dries',  'drift',  'drill',  'drily',  'drink',  'drips',  'drive',  'droid',  'droll',  'drone',  'drool',  'droop',  'drops',  'dross',  'drove',  'drown',  'drugs',  'druid',  'drums',  'drunk',  'drupe',  'dryad',  'dryer',  'dryly',  'duals',  'ducal',  'ducat',  'duchy',  'ducks',  'ducky',  'ducts',  'dudes',  'duels',  'duets',  'duffs',  'dukes',  'dulls',  'dully',  'dulse',  'dumbo',  'dummy',  'dumps',  'dumpy',  'dunce',  'dunes',  'dunks',  'duomo',  'duped',  'dupes',  'dural',  'durum',  'dusks',  'dusky',  'dusts',  'dusty',  'dutch',  'duvet',  'dwarf',  'dweeb',  'dwell',  'dwelt',  'dyads',  'dyers',  'dying',  'dykes',  'eager',  'eagle',  'eared',  'earls',  'early',  'earns',  'earth',  'eased',  'easel',  'easer',  'eases',  'eaten',  'eater',  'eaves',  'ebbed',  'ebony',  'ebook',  'echos',  'eclat',  'edema',  'edged',  'edger',  'edges',  'edict',  'edify',  'edits',  'eejit',  'eerie',  'egged',  'egret',  'eider',  'eidos',  'eight',  'eject',  'ejido',  'eland',  'elbow',  'elder',  'elect',  'elegy',  'elide',  'elite',  'elope',  'elude',  'elute',  'elven',  'elves',  'email',  'embed',  'ember',  'emcee',  'emery',  'emirs',  'emits',  'emote',  'empty',  'enact',  'ended',  'endow',  'enema',  'enemy',  'enjoy',  'ennui',  'enoki',  'enrol',  'ensue',  'enter',  'entry',  'envoy',  'eosin',  'epics',  'epoch',  'epoxy',  'equal',  'equip',  'erase',  'erect',  'ergot',  'erode',  'erred',  'error',  'erupt',  'essay',  'ether',  'ethic',  'ethos',  'ethyl',  'etude',  'euros',  'evade',  'evens',  'event',  'every',  'evict',  'evils',  'evoke',  'ewers',  'exact',  'exalt',  'exams',  'excel',  'execs',  'exert',  'exile',  'exist',  'exits',  'expat',  'expel',  'expos',  'extol',  'extra',  'exude',  'exult',  'exurb',  'eying',  'eyrie',  'fable',  'faced',  'facer',  'faces',  'facet',  'facia',  'facts',  'faded',  'fader',  'fades',  'faery',  'fails',  'faint',  'fairs',  'fairy',  'faith',  'faked',  'faker',  'fakes',  'fakie',  'fakir',  'falls',  'famed',  'fancy',  'fangs',  'fanny',  'farce',  'fared',  'fares',  'farms',  'farts',  'fasts',  'fatal',  'fated',  'fates',  'fatso',  'fatty',  'fatwa',  'fault',  'fauna',  'fauns',  'favas',  'faves',  'favor',  'fawns',  'faxed',  'faxes',  'fazed',  'fazes',  'fears',  'feast',  'feats',  'fecal',  'feces',  'feeds',  'feels',  'feign',  'feint',  'fella',  'fells',  'felon',  'felts',  'femme',  'femur',  'fence',  'fends',  'feral',  'feria',  'ferns',  'ferny',  'ferry',  'fests',  'fetal',  'fetch',  'feted',  'fetes',  'fetid',  'fetus',  'feuds',  'fever',  'fewer',  'fiats',  'fiber',  'fibre',  'fiche',  'ficus',  'fiefs',  'field',  'fiend',  'fiery',  'fifes',  'fifth',  'fifty',  'fight',  'filch',  'filed',  'filer',  'files',  'filet',  'fills',  'filly',  'films',  'filmy',  'filth',  'final',  'finca',  'finch',  'finds',  'fined',  'finer',  'fines',  'finis',  'finks',  'fiord',  'fired',  'fires',  'firms',  'first',  'fishy',  'fists',  'fitly',  'fiver',  'fives',  'fixed',  'fixer',  'fixes',  'fizzy',  'fjord',  'flack',  'flags',  'flail',  'flair',  'flake',  'flaky',  'flame',  'flank',  'flans',  'flaps',  'flare',  'flash',  'flask',  'flats',  'flaws',  'flays',  'fleas',  'fleck',  'flees',  'fleet',  'flesh',  'flick',  'flier',  'flies',  'fling',  'float',  'flood',  'floor',  'flour',  'flown',  'flows',  'fluid',  'flyer',  'focal',  'focus',  'folks',  'fonts',  'foods',  'force',  'forms',  'forth',  'forty',  'forum',  'found',  'frame',  'fraud',  'fresh',  'fried',  'fries',  'front',  'frost',  'fruit',  'fuels',  'fully',  'funds',  'funny',  'gains',  'games',  'gamma',  'gases',  'gates',  'gauge',  'gears',  'genes',  'genre',  'ghost',  'giant',  'gifts',  'girls',  'given',  'gives',  'gland',  'glass',  'globe',  'glory',  'gloss',  'glove',  'glued',  'goals',  'goats',  'going',  'goods',  'grace',  'grade',  'grain',  'grams',  'grand',  'grant',  'grape',  'graph',  'grasp',  'grass',  'grave',  'great',  'greek',  'green',  'greet',  'grief',  'grill',  'grind',  'grips',  'gross',  'group',  'grove',  'grown',  'grows',  'guard',  'guess',  'guest',  'guide',  'guild',  'guilt',  'habit',  'hairs',  'halls',  'hands',  'handy',  'hangs',  'happy',  'harsh',  'hated',  'hates',  'haven',  'hawks',  'heads',  'heard',  'heart',  'heavy',  'hedge',  'heels',  'hello',  'helps',  'hence',  'herbs',  'highs',  'hills',  'hints',  'hired',  'hobby',  'holds',  'holes',  'holly',  'homes',  'honey',  'honor',  'hooks',  'hoped',  'hopes',  'horns',  'horse',  'hosts',  'hotel',  'hours',  'house',  'hover',  'human',  'humor',  'hurts',  'icons',  'ideal',  'ideas',  'idiot',  'image',  'imply',  'inbox',  'incur',  'index',  'indie',  'inner',  'input',  'intro',  'issue',  'items',  'inert',  'infer',  'infix',  'infos',  'infra',  'ingan',  'ingle',  'ingot',  'inion',  'inked',  'inker',  'inkle',  'inlay',  'inlet',  'inned',  'inner',  'innie',  'innit',  'inorb',  'input',  'inrun',  'insee',  'inset',  'inspo',  'intel',  'inter',  'intis',  'intra',  'intro',  'inula',  'inure',  'inurn',  'invar',  'inver',  'inwit',  'iodic',  'iodin',  'ionic',  'ioras',  'iotas',  'ippon',  'irade',  'iring',  'irked',  'iroko',  'irons',  'irony',  'isbas',  'ishes',  'isled',  'isles',  'islet',  'isnae',  'idler',  'idles',  'idlis',  'idola',  'idols',  'idyll',  'idyls',  'iftar',  'igapo',  'igged',  'igloo',  'iglus',  'ignis',  'ihram',  'ikans',  'ikats',  'ikons',  'ileac',  'ileal',  'ileum',  'ileus',  'iliac',  'iliad',  'ilial',  'ilium',  'iller',  'illth',  'image',  'imago',  'imams',  'imari',  'imaum',  'imbar',  'imbos',  'imbue',  'imide',  'imido',  'imids',  'imine',  'imino',  'imlis',  'immew',  'immit',  'immix',  'imped',  'impel',  'impis',  'imply',  'impot',  'impro',  'imshi',  'imshy',  'inane',  'inapt',  'inarm',  'inbox',  'inbye',  'incas',  'incel',  'incog',  'incur',  'incus',  'incut',  'index',  'india',  'indie',  'indol',  'indri',  'indue',  'inept',  'issei',  'issue',  'istle',  'itchy',  'items',  'ivied',  'ivies',  'ivory',  'ixias',  'ixnay',  'ixora',  'ixtle',  'izard',  'izars',  'izzat',  'jeans',  'jelly',  'jewel',  'joins',  'joint',  'jokes',  'judge',  'juice',  'juicy',  'jumps',  'jabot',  'jacal',  'jacks',  'jacky',  'jaded',  'jades',  'jager',  'jaggy',  'jails',  'jakes',  'jalap',  'jalee',  'jalor',  'jalur',  'jambe',  'jambs',  'jammy',  'janes',  'janky',  'japan',  'japed',  'japer',  'japes',  'jarls',  'jasey',  'jaspe',  'jatis',  'jatos',  'jaunt',  'jaups',  'jawan',  'jawed',  'jazzy',  'jeans',  'jebel',  'jedis',  'jeers',  'jefes',  'jehad',  'jello',  'jells',  'jelly',  'jemmy',  'jenny',  'keeps',  'kicks',  'kills',  'kinda',  'kinds',  'kings',  'knees',  'knife',  'knock',  'knots',  'known',  'knows',  'keeps',  'kills',  'kench',  'kilos',  'knelt',  'koala',  'knead',  'kayak',  'kevel',  'knack',  'knoll',  'kooky',  'kicks',  'kaput',  'khaki',  'knees',  'knock',  'krill',  'kudos',  'kempt',  'kiosk',  'knell',  'knife',  'krait',  'kites',  'keeve',  'kiddy',  'kneel',  'knobs',  'knurl',  'kaama',  'kabab',  'kabar',  'kabob',  'kacha',  'kacks',  'kadai',  'kades',  'kadis',  'kails',  'kaims',  'kaing',  'kains',  'kajal',  'kakas',  'kakis',  'kalam',  'kalas',  'kales',  'kalif',  'kalis',  'kalpa',  'kalua',  'kanae',  'kanal',  'kanas',  'kanat',  'kandy',  'kaneh',  'kanes',  'karns',  'karoo',  'karos',  'karri',  'karst',  'karsy',  'karts',  'karzy',  'kasha',  'katal',  'katas',  'katis',  'katti',  'kerry',  'kesar',  'kests',  'ketas',  'ketch',  'ketol',  'kevil',  'kexes',  'keyed',  'keyer',  'kibbe',  'kibbi',  'kibei',  'kibes',  'kibla',  'kicky',  'kiddo',  'kidel',  'kidge',  'kiefs',  'kiers',  'kieve',  'kiley',  'kilig',  'kilps',  'kilts',  'kilty',  'kinda',  'kinds',  'kindy',  'kines',  'kings',  'kingy',  'label',  'labor',  'lacks',  'lakes',  'lamps',  'lands',  'lanes',  'large',  'laser',  'lasts',  'later',  'laugh',  'layer',  'leads',  'leaks',  'learn',  'lease',  'least',  'leave',  'legal',  'lemon',  'level',  'lever',  'light',  'liked',  'likes',  'limbs',  'limit',  'lined',  'linen',  'liner',  'lines',  'links',  'lions',  'lists',  'lived',  'liver',  'lives',  'loads',  'loans',  'lobby',  'local',  'locks',  'lodge',  'logic',  'logos',  'looks',  'loops',  'loose',  'lords',  'loses',  'loved',  'lover',  'loves',  'lower',  'loyal',  'lucky',  'lunar',  'lunch',  'lungs',  'lying',  'lacey',  'lacis',  'lacka',  'lacks',  'laddu',  'laddy',  'laded',  'ladee',  'laden',  'lader',  'ladle',  'ladoo',  'lairs',  'lairy',  'laith',  'laity',  'laked',  'laker',  'lakes',  'lance',  'lanch',  'lande',  'lands',  'laned',  'lanes',  'lanky',  'lants',  'lapas',  'lapel',  'lapin',  'lapis',  'lapje',  'lappa',  'lappy',  'lapse',  'larch',  'lards',  'lardy',  'laree',  'larva',  'lased',  'laser',  'lases',  'lassi',  'lasso',  'lassy',  'lasts',  'latah',  'latch',  'later',  'leany',  'leaps',  'leapt',  'learn',  'lears',  'leary',  'lease',  'leash',  'least',  'leats',  'leave',  'leavy',  'leaze',  'leben',  'leccy',  'leche',  'ledes',  'leeps',  'leers',  'leery',  'leese',  'leets',  'leeze',  'lefte',  'lefts',  'lefty',  'legal',  'leger',  'leges',  'legge',  'leggo',  'macro',  'magic',  'major',  'maker',  'makes',  'males',  'maple',  'march',  'marks',  'marry',  'masks',  'match',  'mates',  'maths',  'matte',  'maybe',  'mayor',  'meals',  'means',  'meant',  'meats',  'medal',  'media',  'meets',  'melee',  'menus',  'mercy',  'merge',  'merit',  'merry',  'messy',  'metal',  'meter',  'metro',  'micro',  'midst',  'might',  'miles',  'minds',  'mines',  'minor',  'minus',  'mixed',  'mixer',  'mixes',  'model',  'modem',  'modes',  'moist',  'money',  'month',  'moral',  'motor',  'mount',  'mouse',  'mouth',  'moved',  'moves',  'movie',  'music',  'myths',  'nails',  'naked',  'named',  'names',  'nasal',  'nasty',  'naval',  'needs',  'nerve',  'never',  'newer',  'newly',  'nexus',  'nicer',  'niche',  'night',  'ninja',  'ninth',  'noble',  'nodes',  'noise',  'noisy',  'norms',  'north',  'notch',  'noted',  'notes',  'novel',  'nurse',  'nylon',  'oasis',  'occur',  'ocean',  'offer',  'often',  'older',  'olive',  'omega',  'onion',  'onset',  'opens',  'opera',  'opted',  'optic',  'orbit',  'order',  'organ',  'other',  'ought',  'ounce',  'outer',  'owned',  'owner',  'oxide',  'ocker',  'ocote',  'ocrea',  'octad',  'octal',  'octan',  'octas',  'octet',  'octic',  'octli',  'octyl',  'oculi',  'odahs',  'odals',  'odder',  'oddly',  'odeon',  'odeum',  'odist',  'odium',  'odoom',  'odors',  'odour',  'odsos',  'odums',  'odyle',  'odyls',  'oecus',  'ofays',  'offal',  'offed',  'offer',  'oflag',  'often',  'ofuro',  'ogams',  'ogees',  'oggin',  'ogham',  'ogive',  'ogled',  'ogler',  'ogles',  'ogmic',  'ogres',  'ohelo',  'ohias',  'ohing',  'ohmic',  'oicks',  'oidia',  'oiled',  'oiler',  'oints',  'oiran',  'ojime',  'okapi',  'okays',  'okehs',  'okies',  'oking',  'packs',  'pages',  'pains',  'paint',  'pairs',  'panel',  'panic',  'pants',  'paper',  'parks',  'parts',  'party',  'pasta',  'paste',  'patch',  'paths',  'patio',  'pause',  'peace',  'peach',  'peaks',  'pearl',  'pedal',  'peers',  'penis',  'penny',  'perks',  'pests',  'petty',  'phase',  'phone',  'photo',  'piano',  'picks',  'piece',  'piles',  'pills',  'pilot',  'pinch',  'pipes',  'pitch',  'pixel',  'pizza',  'place',  'plain',  'plane',  'plans',  'plant',  'plate',  'plays',  'plaza',  'plots',  'plugs',  'poems',  'point',  'poker',  'polar',  'poles',  'polls',  'pools',  'porch',  'pores',  'ports',  'posed',  'poses',  'posts',  'pouch',  'pound',  'power',  'press',  'price',  'pride',  'prime',  'print',  'prior',  'prize',  'probe',  'promo',  'prone',  'proof',  'props',  'proud',  'prove',  'proxy',  'psalm',  'pulls',  'pulse',  'pumps',  'punch',  'pupil',  'puppy',  'purse',  'queen',  'query',  'quest',  'queue',  'quick',  'quiet',  'quilt',  'quite',  'quote',  'qadis',  'qaids',  'qajaq',  'qanat',  'qapik',  'qibla',  'qilas',  'qipao',  'qophs',  'qorma',  'quabs',  'quack',  'quads',  'quaff',  'quags',  'quail',  'quair',  'quais',  'quake',  'quaky',  'quale',  'qualm',  'qualy',  'quank',  'quant',  'quare',  'quark',  'quarl',  'quart',  'quash',  'queek',  'queem',  'queen',  'queer',  'quell',  'queme',  'quena',  'quern',  'query',  'queso',  'quest',  'quete',  'queue',  'queyn',  'queys',  'queyu',  'quibs',  'quich',  'races',  'racks',  'radar',  'radio',  'rails',  'rainy',  'raise',  'rally',  'ranch',  'range',  'ranks',  'rapid',  'rated',  'rates',  'ratio',  'razor',  'reach',  'react',  'reads',  'ready',  'realm',  'rebel',  'refer',  'reign',  'relax',  'relay',  'renal',  'renew',  'reply',  'reset',  'resin',  'retro',  'rider',  'rides',  'ridge',  'rifle',  'right',  'rigid',  'rings',  'rinse',  'risen',  'rises',  'risks',  'risky',  'rival',  'river',  'roads',  'robot',  'rocks',  'rocky',  'rogue',  'roles',  'rolls',  'roman',  'rooms',  'roots',  'ropes',  'roses',  'rough',  'round',  'route',  'royal',  'rugby',  'ruins',  'ruled',  'ruler',  'rules',  'rural',  'rakee',  'raker',  'rakes',  'rakhi',  'rakia',  'rakis',  'rakki',  'raksi',  'rakus',  'rales',  'ralli',  'rally',  'ralph',  'ramal',  'ramee',  'ramen',  'rames',  'ramet',  'ramie',  'ramin',  'ramis',  'rammy',  'ramon',  'ramps',  'ramus',  'ranas',  'rance',  'ranch',  'rando',  'rands',  'randy',  'ranee',  'ranes',  'ranga',  'range',  'rangi',  'rangy',  'ranid',  'ranis',  'ranke',  'ranks',  'sadly',  'safer',  'salad',  'sales',  'salon',  'sandy',  'satin',  'sauce',  'saved',  'saves',  'scale',  'scalp',  'scans',  'scare',  'scarf',  'scary',  'scene',  'scent',  'scoop',  'scope',  'score',  'scout',  'scrap',  'screw',  'seals',  'seams',  'seats',  'seeds',  'seeks',  'seems',  'sells',  'sends',  'sense',  'serum',  'serve',  'setup',  'seven',  'sewer',  'shade',  'shaft',  'shake',  'shall',  'shame',  'shape',  'share',  'shark',  'sharp',  'sheep',  'sheer',  'sheet',  'shelf',  'shell',  'shift',  'shine',  'shiny',  'ships',  'shirt',  'shock',  'shoes',  'shook',  'shoot',  'shops',  'shore',  'short',  'shots',  'shown',  'shows',  'sides',  'siege',  'sight',  'sigma',  'signs',  'silly',  'since',  'sites',  'sixth',  'sized',  'sizes',  'skies',  'skill',  'skins',  'skirt',  'skull',  'slate',  'slave',  'sleek',  'sleep',  'slept',  'slice',  'slide',  'slope',  'slots',  'small',  'smart',  'smell',  'smile',  'smoke',  'snack',  'snake',  'sneak',  'socks',  'soils',  'solar',  'solid',  'solve',  'songs',  'sonic',  'sorry',  'sorts',  'souls',  'sound',  'south',  'space',  'spare',  'spark',  'speak',  'specs',  'speed',  'spell',  'spend',  'spent',  'sperm',  'spice',  'spicy',  'spike',  'spine',  'spite',  'split',  'spoke',  'spoon',  'sport',  'spots',  'spray',  'spurs',  'squad',  'stack',  'staff',  'stage',  'stain',  'stake',  'stamp',  'stand',  'stark',  'stars',  'start',  'state',  'stats',  'stays',  'steak',  'steal',  'steam',  'steel',  'steep',  'steer',  'stems',  'steps',  'stick',  'stiff',  'still',  'stock',  'stole',  'stone',  'stood',  'stool',  'stops',  'store',  'storm',  'story',  'stove',  'strap',  'straw',  'strip',  'stuck',  'study',  'stuff',  'style',  'sucks',  'sugar',  'suite',  'suits',  'sunny',  'super',  'surge',  'sushi',  'swear',  'sweat',  'sweet',  'swept',  'swift',  'swing',  'swiss',  'sword',  'syrup',  'table',  'taken',  'takes',  'tales',  'talks',  'tanks',  'tapes',  'tasks',  'taste',  'tasty',  'taxes',  'teach',  'teams',  'tears',  'teens',  'teeth',  'tells',  'tempo',  'tends',  'tenth',  'tents',  'terms',  'tests',  'texts',  'thank',  'theft',  'their',  'theme',  'there',  'these',  'thick',  'thief',  'thigh',  'thing',  'think',  'third',  'those',  'three',  'threw',  'throw',  'thumb',  'tiger',  'tight',  'tiles',  'timer',  'times',  'tired',  'tires',  'title',  'toast',  'today',  'token',  'tones',  'tools',  'tooth',  'topic',  'torch',  'total',  'touch',  'tough',  'tours',  'towel',  'tower',  'towns',  'toxic',  'trace',  'track',  'tract',  'trade',  'trail',  'train',  'trait',  'trans',  'traps',  'trash',  'treat',  'trees',  'trend',  'trial',  'tribe',  'trick',  'tried',  'tries',  'trips',  'trout',  'truck',  'truly',  'trump',  'trunk',  'trust',  'truth',  'tubes',  'tumor',  'tuned',  'tunes',  'turbo',  'turns',  'tutor',  'tweet',  'twice',  'twins',  'twist',  'types',  'tyres',  'ultra',  'uncle',  'under',  'union',  'unite',  'units',  'unity',  'until',  'upper',  'upset',  'urban',  'urged',  'urine',  'usage',  'users',  'using',  'usual',  'unsaw',  'unsay',  'unsee',  'unset',  'unsew',  'unsub',  'untag',  'untax',  'untie',  'until',  'unwed',  'unwet',  'unwit',  'unwon',  'unzip',  'upbow',  'upbye',  'updos',  'updry',  'upend',  'upjet',  'uplay',  'upled',  'uplit',  'upped',  'upper',  'upran',  'uprun',  'upsee',  'upset',  'upsey',  'upter',  'uptie',  'uraei',  'urali',  'uraos',  'urare',  'urari',  'urase',  'urate',  'urban',  'urbex',  'urbia',  'urdee',  'ureal',  'ureas',  'uredo',  'ureic',  'ureid',  'urena',  'urged',  'urger',  'urges',  'urial',  'urine',  'vague',  'valid',  'value',  'valve',  'vapor',  'vault',  'vegan',  'veins',  'vents',  'venue',  'verse',  'video',  'views',  'villa',  'vinyl',  'viral',  'virus',  'visas',  'visit',  'vital',  'vivid',  'vocal',  'vodka',  'voice',  'volts',  'voted',  'voter',  'votes',  'verbs',  'verde',  'verge',  'verra',  'verre',  'verry',  'versa',  'verse',  'verso',  'verst',  'verte',  'verts',  'vertu',  'verve',  'vespa',  'vesta',  'vests',  'vetch',  'veuve',  'veves',  'vexed',  'vexer',  'vexes',  'vexil',  'vezir',  'vials',  'viand',  'vibed',  'vibes',  'vibex',  'vibey',  'vicar',  'vices',  'vichy',  'vicus',  'wages',  'wagon',  'waist',  'walks',  'walls',  'wants',  'warns',  'waste',  'watch',  'water',  'watts',  'waves',  'wears',  'weeds',  'weeks',  'weigh',  'weird',  'wells',  'welsh',  'whale',  'wheat',  'wheel',  'where',  'which',  'while',  'white',  'whole',  'whose',  'wider',  'widow',  'width',  'winds',  'wines',  'wings',  'wiped',  'wired',  'wires',  'witch',  'wives',  'woman',  'women',  'woods',  'words',  'works',  'world',  'worms',  'worry',  'worse',  'worst',  'worth',  'would',  'wound',  'wrath',  'wrist',  'write',  'wrong',  'wrote',  'waacs',  'wacke',  'wacko',  'wacks',  'wacky',  'wadds',  'waddy',  'waded',  'wader',  'wades',  'wadis',  'wafer',  'waffs',  'wafts',  'waged',  'wager',  'wages',  'wagga',  'wagon',  'wahoo',  'waide',  'waifs',  'wails',  'wains',  'wairs',  'waist',  'waits',  'waive',  'wakas',  'waked',  'waken',  'waker',  'wakes',  'wakfs',  'waldo',  'walds',  'waled',  'waler',  'wales',  'walis',  'walks',  'walla',  'walls',  'wally',  'walty',  'waltz',  'wamed',  'wames',  'wamus',  'wands',  'wanes',  'waney',  'wangs',  'wanks',  'wanky',  'wanle',  'wanly',  'wanna',  'wants',  'wanty',  'wanze',  'waqfs',  'warbs',  'xebec',  'xenia',  'xenic',  'xenon',  'xeric',  'xerox',  'xerus',  'xoana',  'xrays',  'xylan',  'xylem',  'xylic',  'xylol',  'xylyl',  'xysti',  'xysts',  'yacht',  'yards',  'years',  'yeast',  'yield',  'young',  'yours',  'youth',  'yummy',  'yacca',  'yacht',  'yacka',  'yacks',  'yadda',  'yadim',  'yaffs',  'yager',  'yagis',  'yagna',  'yahoo',  'yajes',  'yajna',  'yakka',  'yakow',  'yales',  'yamen',  'yampa',  'yampy',  'yamun',  'yandy',  'yangs',  'yanks',  'yapok',  'yapon',  'yapps',  'yappy',  'yarak',  'yarco',  'yards',  'yarer',  'yarfa',  'yarks',  'yarns',  'yarra',  'yarrs',  'yarta',  'yarto',  'yasss',  'yates',  'yatra',  'yauds',  'yauld',  'yaups',  'yawed',  'yawey',  'yawls',  'yawns',  'zones',  'zebra',  'zests',  'zesty',  'zetas',  'zorse',  'zouks',  'zowee',  'zowie',  'zacks',  'zaddy',  'zafus',  'zaida',  'zaide',  'zaidy',  'zaire',  'zakah',  'zakat',  'zamac',  'zamak',  'zaman',  'zambo',  'zamia',  'zamis',  'zanja',  'zante',  'zanza',  'zanze',  'zappy',  'zarda',  'zarfs',  'zaris',  'zatar',  'zatis',  'zawns',  'zaxes',  'zayde',  'zerks',  'zeros',  'zests',  'zesty',  'zetas',  'zexes',  'zezes',  'zhlob',  'zhlub',  'zhomo',  'zhush',  'zhuzh',  'zibet',  'ziffs',  'zigan',  'zikrs',  'zilas',  'zilch',  'zilla',  'zills',  'zimbi',  'zimbs',  'zinco',  'zincs',  'zincy',  'zineb',  'zines',  'zings',  'zingy',  'zinke',  'zinky',  'zinos',  'zippo',  'zippy',  'ziram',  'zitis',  'zitti',  'zitty',  'zizel',  'zizit',  'zlote',  'zloty',  'zoaea',  'zobos',  'zobus',  'zocco',  'zoeae',  'zoeal']

class MainWindow(QtWidgets.QMainWindow, Ui_Wordle, Ui_GameEnded):
    def __init__(self, *args, obj=None, **kwargs,):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Wordle")

        self.wordlist = WORDLIST
        self.hidden_word = self.wordlist[randint(0, len(self.wordlist)-1)].upper()
     

        self.row_1 = [self.element_11, self.element_12, self.element_13, self.element_14, self.element_15]
        self.row_2 = [self.element_21, self.element_22, self.element_23, self.element_24, self.element_25]
        self.row_3 = [self.element_31, self.element_32, self.element_33, self.element_34, self.element_35]
        self.row_4 = [self.element_41, self.element_42, self.element_43, self.element_44, self.element_45]
        self.row_5 = [self.element_51, self.element_52, self.element_53, self.element_54, self.element_55]
        self.row_6 = [self.element_61, self.element_62, self.element_63, self.element_64, self.element_65]
        self.rows = [self.row_1, self.row_2, self.row_3, self.row_4, self.row_5, self.row_6]

        self.actual_row = 1
        self.actualString = ''

        self.green_letters = set()

        self.playable = True

        self.wordlist_Button.clicked.connect(self.customWordlist)
        self.startButton.clicked.connect(self.newGame)

        if self.playable:

            
            self.A_pushButton.clicked.connect(lambda: self.addChar('A'))
            self.B_pushButton.clicked.connect(lambda: self.addChar('B'))
            self.C_pushButton.clicked.connect(lambda: self.addChar('C'))
            self.D_pushButton.clicked.connect(lambda: self.addChar('D'))
            self.E_pushButton.clicked.connect(lambda: self.addChar('E'))
            self.F_pushButton.clicked.connect(lambda: self.addChar('F'))
            self.G_pushButton.clicked.connect(lambda: self.addChar('G'))
            self.H_pushButton.clicked.connect(lambda: self.addChar('H'))
            self.I_pushButton.clicked.connect(lambda: self.addChar('I'))
            self.J_pushButton.clicked.connect(lambda: self.addChar('J'))
            self.K_pushButton.clicked.connect(lambda: self.addChar('K'))
            self.L_pushButton.clicked.connect(lambda: self.addChar('L'))
            self.M_pushButton.clicked.connect(lambda: self.addChar('M'))
            self.N_pushButton.clicked.connect(lambda: self.addChar('N'))
            self.O_pushButton.clicked.connect(lambda: self.addChar('O'))
            self.P_pushButton.clicked.connect(lambda: self.addChar('P'))
            self.Q_pushButton.clicked.connect(lambda: self.addChar('Q'))
            self.R_pushButton.clicked.connect(lambda: self.addChar('R'))
            self.S_pushButton.clicked.connect(lambda: self.addChar('S'))
            self.T_pushButton.clicked.connect(lambda: self.addChar('T'))
            self.U_pushButton.clicked.connect(lambda: self.addChar('U'))
            self.V_pushButton.clicked.connect(lambda: self.addChar('V'))
            self.W_pushButton.clicked.connect(lambda: self.addChar('W'))
            self.X_pushButton.clicked.connect(lambda: self.addChar('X'))
            self.Y_pushButton.clicked.connect(lambda: self.addChar('Y'))
            self.Z_pushButton.clicked.connect(lambda: self.addChar('Z'))
            self.ENTER_pushButton.clicked.connect(self.checkString)
            self.DELETE_pushButton.clicked.connect(self.delChar)
            

        self.keyboard = {
            'A': self.A_pushButton,
            'B': self.B_pushButton,
            'C': self.C_pushButton,
            'D': self.D_pushButton,
            'E': self.E_pushButton,
            'F': self.F_pushButton,
            'G': self.G_pushButton,
            'H': self.H_pushButton,
            'I': self.I_pushButton,
            'J': self.J_pushButton,
            'K': self.K_pushButton,
            'L': self.L_pushButton,
            'M': self.M_pushButton,
            'N': self.N_pushButton,
            'O': self.O_pushButton,
            'P': self.P_pushButton,
            'Q': self.Q_pushButton,
            'R': self.R_pushButton,
            'S': self.S_pushButton,
            'T': self.T_pushButton,
            'U': self.U_pushButton,
            'V': self.V_pushButton,
            'W': self.W_pushButton,
            'X': self.X_pushButton,
            'Y': self.Y_pushButton,
            'Z': self.Z_pushButton
        }


    # method to start a new game
    def newGame(self):

        print(self.wordlist)

        # reset the rows and the keyboard
        for row in self.rows:
            for char in row:
                char.setText('')
                char.setStyleSheet("border: 2px solid rgb(58,58,60);\ncolor: white;\n")
        
        for key in self.keyboard.keys():
            self.keyboard.get(key).setStyleSheet("border: 2px solid rgb(58,58,60);\nbackground-color: rgb(81,83,84);\ncolor: white;")

        self.playable = True
        self.actual_row = 1
        self.actualString = ''
        self.hidden_word = self.wordlist[randint(0, len(self.wordlist)-1)].upper()

        print(self.hidden_word)

    
    # method to load a custom wordlist
    def customWordlist(self):

        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Seleziona una wordlist", "", "File (*.txt)")

        if file_path:
            
            with open(file_path, 'r', encoding='utf-8') as f:
                self.wordlist = f.readlines()
                self.wordlist = [x.rstrip() for x in self.wordlist]

            self.newGame()

    # create a dialog window showing the hidden word and asking for a new game
    def gameEnded(self):

        self.playable = False
        dialog = QtWidgets.QDialog(self)
        ui_dialog = Ui_GameEnded()
        ui_dialog.setupUi(dialog)
        dialog.setWindowTitle("Game Ended")
        ui_dialog.hiddenWord.setText(self.hidden_word)
        ui_dialog.playAgain_Button.clicked.connect(self.newGame)
        ui_dialog.playAgain_Button.clicked.connect(dialog.close)
        dialog.exec_()




    # method to check if the word chosen is correct, enabled when pressing ENTER
    def checkString(self):

        print(self.actualString)

        if len(self.actualString) == 5 and self.playable:

            if self.actualString.lower() in self.wordlist:

                self.colorChars()
                self.actual_row += 1

                if self.actual_row > 6:
                    self.gameEnded()
                else:
                    self.getActualString()
            
            else:
                # color the char's border in red if not in wordlist
                for element in self.rows[self.actual_row-1]:
                    element.setStyleSheet("border: 2px solid red;\ncolor: white;\nbackground-color: rgb(58,58,60)")


    


        
    def colorChars(self):

        chars = list(self.hidden_word)

        for i in range(len(self.rows[self.actual_row-1])):

            actual_char = self.rows[self.actual_row-1][i].text()

            if actual_char in chars:

                # imposto ad arancione la lettera della riga
                self.rows[self.actual_row-1][i].setStyleSheet("border: 2px solid rgb(181,112,59);\ncolor: white;\nbackground-color: rgb(181,112,59)")

                # se la corrispondente lettera della tastiera non e' gia' verde, la coloro di arancione
                if actual_char not in self.green_letters:
                    self.keyboard.get(actual_char).setStyleSheet("border: 2px solid rgb(181,112,59);\ncolor: white;\nbackground-color: rgb(181,112,59)")

            if actual_char in chars[i]:

                # imposto a verde la lettera della riga
                self.rows[self.actual_row-1][i].setStyleSheet("border: 2px solid rgb(83,141,78);\ncolor: white;\nbackground-color: rgb(83,141,78)")
                # imposto a verde la lettera della tastiera
                self.keyboard.get(actual_char).setStyleSheet("border: 2px solid rgb(83,141,78);\ncolor: white;\nbackground-color: rgb(83,141,78)")
                # aggiungo la lettera alla lista delle lettere corrette
                self.green_letters.add(actual_char)
            
            if actual_char not in chars:
                self.keyboard.get(actual_char).setStyleSheet("border: 2px solid rgb(58,58,60);\ncolor: white;\nbackground-color: rgb(58,58,60)")


        # se la parola inserita e' quella corretta:
        if self.actualString == self.hidden_word:
            # il gioco e' terminato
            self.playable = False
        



        
        
    
    def getActualString(self):

        if self.playable:
         
            self.actualString = self.rows[self.actual_row - 1][0].text() + \
                                self.rows[self.actual_row - 1][1].text() + \
                                self.rows[self.actual_row - 1][2].text() + \
                                self.rows[self.actual_row - 1][3].text() + \
                                self.rows[self.actual_row - 1][4].text()


    def addChar(self, char):

        if not len(self.actualString) == 5 and self.playable:
            nextPos = len(self.actualString)
            self.rows[self.actual_row - 1][nextPos].setText(char)
            self.getActualString()

    def delChar(self):

        if not len(self.actualString) == 0 and self.playable:
            nextPos = len(self.actualString)
            self.rows[self.actual_row - 1][nextPos-1].setText('')
            self.rows[self.actual_row - 1][nextPos-1].setStyleSheet("border: 2px solid rgb(58,58,60);\ncolor: white;\n")
            self.getActualString()


    def keyPressEvent(self, event):

        if self.playable:

            if event.key() == Qt.Key_A:
                self.addChar('A')

            elif event.key() == Qt.Key_B:
                self.addChar('B')

            elif event.key() == Qt.Key_C:
                self.addChar('C')

            elif event.key() == Qt.Key_D:
                self.addChar('D')

            elif event.key() == Qt.Key_E:
                self.addChar('E')

            elif event.key() == Qt.Key_F:
                self.addChar('F')

            elif event.key() == Qt.Key_G:
                self.addChar('G')

            elif event.key() == Qt.Key_H:
                self.addChar('H')

            elif event.key() == Qt.Key_I:
                self.addChar('I')

            elif event.key() == Qt.Key_J:
                self.addChar('J')

            elif event.key() == Qt.Key_K:
                self.addChar('K')

            elif event.key() == Qt.Key_L:
                self.addChar('L')

            elif event.key() == Qt.Key_M:
                self.addChar('M')

            elif event.key() == Qt.Key_N:
                self.addChar('N')

            elif event.key() == Qt.Key_O:
                self.addChar('O')

            elif event.key() == Qt.Key_P:
                self.addChar('P')

            elif event.key() == Qt.Key_Q:
                self.addChar('Q')

            elif event.key() == Qt.Key_R:
                self.addChar('R')

            elif event.key() == Qt.Key_S:
                self.addChar('S')

            elif event.key() == Qt.Key_T:
                self.addChar('T')

            elif event.key() == Qt.Key_U:
                self.addChar('U')

            elif event.key() == Qt.Key_V:
                self.addChar('V')

            elif event.key() == Qt.Key_W:
                self.addChar('W')

            elif event.key() == Qt.Key_X:
                self.addChar('X')

            elif event.key() == Qt.Key_Y:
                self.addChar('Y')

            elif event.key() == Qt.Key_Z:
                self.addChar('Z')      
            
            elif event.key() == Qt.Key_Backspace:
                self.delChar()

            elif event.key() == Qt.Key_Return:
                self.checkString()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

