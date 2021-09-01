# In this kata you have to create all permutations of an input string and remove duplicates, if present.
# This means, you have to shuffle all letters from the input in all possible orders.
#
# Examples:
#
# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

import itertools


def permutations(string):
    permut = itertools.permutations(string)
    return sorted({''.join(v) for v in permut})
