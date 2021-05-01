# first main python file for project_flashcards
from collections import namedtuple
import random

Card = namedtuple('flashcard','front back category language')

Deck=list ()
Deck.append(Card(front='push', language='git', back='empujar', category='command'))
Deck.append(Card(front='select', language='SQL', back='seleccionar', category='clause'))
Deck.append(Card(front='dict', language='python', back='dictionario', category='function'))
Deck.append(Card(front='pwd', language='linux', back='present working directory', category='command'))
Deck.append(Card(front=':w', language='vim', back='guardar', category='command'))
Deck.append(Card(front=':q', language='vim', back='salir', category='command'))
Deck.append(Card(front='namedtuple', back='basic object',category='object', language = 'python'))
Deck.append(Card(front= 'print', back='imprimir',category='function', language = 'python'))

user_input = ''

while user_input != 'exit' :
	test_card = random.choice(Deck)
	print('welcome to project_flashcards')
	print('front of Card:')
	print(test_card.front)
	input('press enter to reveal back of Card')
	print(test_card.back)
	user_input = input ('type exit and press enter to end this program. type anything else for another Card')

