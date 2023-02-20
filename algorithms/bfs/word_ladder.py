"""
Given two words (begin_word and end_word), and a dictionary's word list,
find the length of shortest transformation sequence
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
begin_word = "hit"
end_word = "cog"
word_list = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return -1 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""


def ladder_length(begin_word, end_word, word_list):
    """
    Bidirectional BFS!!!
    :type begin_word: str
    :type end_word: str
    :type word_list: Set[str]
    :rtype: int
    """

    """
    Manual branch coverage flags
    """
    flags = [False for i in range(9)]

    if len(begin_word) != len(end_word):
        flags[0] = True
        print_flags(flags)
        return -1   # not possible

    if begin_word == end_word:
        flags[1] = True
        print_flags(flags)
        return 0

    # when only differ by 1 character
    if sum(c1 != c2 for c1, c2 in zip(begin_word, end_word)) == 1:
        flags[2] = True
        print_flags(flags)
        return 1

    begin_set = set()
    end_set = set()
    begin_set.add(begin_word)
    end_set.add(end_word)
    result = 2
    while begin_set and end_set:
        flags[3] = True

        if len(begin_set) > len(end_set):
            flags[4] = True
            begin_set, end_set = end_set, begin_set

        next_begin_set = set()
        for word in begin_set:
            flags[5] = True
            for ladder_word in word_range(word):
                flags[6] = True
                if ladder_word in end_set:
                    flags[7] = True
                    print_flags(flags)
                    return result
                if ladder_word in word_list:
                    flags[8] = True
                    next_begin_set.add(ladder_word)
                    word_list.remove(ladder_word)
        begin_set = next_begin_set
        result += 1
        # print(begin_set)
        # print(result)
    print_flags(flags)
    return -1

def print_flags(flags):
    coverage = 0
    for i in range(len(flags)):
        if flags[i]:
            coverage += 1
    cov_ratio = coverage / len(flags)
    print("Branch cov: ", cov_ratio)

def word_range(word):
    for ind in range(len(word)):
        temp = word[ind]
        for c in [chr(x) for x in range(ord('a'), ord('z') + 1)]:
            if c != temp:
                yield word[:ind] + c + word[ind + 1:]
