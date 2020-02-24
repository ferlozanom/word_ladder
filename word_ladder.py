#!/bin/python3

from collections import deque
from copy import deepcopy

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
   word_ladder('stone','money')
    ```
   may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if start_word == end_word:
        return [start_word]

    with open(dictionary_file) as d:
        tot_d = d.readlines()
        dictionary = []
    for w in tot_d:
        dictionary.append(w.strip("\n"))
    print(dictionary)

    s = []
    s.append(start_word)
    
    q = deque()
    q.append(s)

    while len(q) > 0:
        first_stack = q.popleft()
        for word in dictionary:
            if _adjacent(first_stack[len(first_stack)-1],word):
                if word == end_word:
                    ladder = first_stack       
                    ladder.append(word)
                    return(ladder)
                s_copy = deepcopy(first_stack)
                s_copy.append(word)
                q.append(s_copy)
                dictionary.remove(word)

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if ladder == []:
        return False
    if ladder == None:
        return False

    for word1,word2 in zip(ladder,ladder[1:]):
        if not _adjacent(word1,word2):
            return False
    return True

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if word1 == word2:
        return False 

    dif_count = 0

    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                dif_count += 1
        
    if dif_count == 1:
        return True

    else:
        return False

