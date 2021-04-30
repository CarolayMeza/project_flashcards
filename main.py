# first main python file for project_flashcards
from collections import namedtuple
import random

Card = namedtuple('flashcard','front back category language')

Deck=list ()
Deck.append(Card(front='dict', back='dicionario',category='objeto', language = 'python'))
Deck.append(Card(front='namedtuple', back='basic object',category='objeto', language = 'python'))
Deck.append(Card(front= 'print', back='imprimir',category='funcion', language = 'python'))

print(random.choice(Deck))