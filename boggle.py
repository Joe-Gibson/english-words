# -*- coding: utf-8 -*-
"""
Created on Wed May 29 23:05:40 2024

@author: Admin
"""

import random
import string    
import numpy as np

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    # english_words = load_words()
    # demo print
    # print('fate' in english_words)

    no_letters = 5
    grid = np.zeros(5, 5)
    
    for i in range(0, no_letters):
        for j in range(0, no_letters):
            grid[i, j] = random.choice(string.ascii_lowercase) 
    