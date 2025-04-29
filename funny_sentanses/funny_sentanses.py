name = ['Lee', 'Bob', 'Nina']
verb = ['rides', 'buys', 'kicks']
noun = ['a lion', 'a plane', 'a bicycle']

from random import randint
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked
print (pick(name), pick(verb), pick(noun), end = '.\n')
