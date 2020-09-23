print('hello')


'''
This prograpm will play the game hangman with the user. 
You need to have the random_word library installed. 
'''

from random_word import RandomWords
r = RandomWords()
word = r.get_random_word(hasDictionaryDef = 'true')
word = word.lower
space = list(word)
dash = []
dash.extend(word)

