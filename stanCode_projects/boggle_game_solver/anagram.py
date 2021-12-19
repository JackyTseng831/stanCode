"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


all_word = []
ans = []


def main():
    """
    This program is to find the anagrams
    """
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    word = str(input('Find anagrams for: '))
    start = time.time()
    find_anagrams(word)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global all_word
    with open(FILE, 'r') as f:
        for line in f:
            place = len(line) - 2
            word = line[:place]
            all_word.append(word)


def find_anagrams(s):
    """
    :param s: the word input of user
    :return: the result of list of anagrams
    """
    global all_word
    global ans
    number_lst = []
    for i in range(len(s)):
        number_lst.append(i)
    print('Searching...')
    anagrams_helper(s, number_lst, [], '', len(s))
    print(ans)


def anagrams_helper(s, number_lst, current_lst, current_string, length):
    global all_word
    global ans
    if len(current_lst) == length:  # Base case!
        if current_string in all_word and current_string not in ans:
            ans.append(current_string)
            print('Found: ', current_string)
            print('Searching...')
    else:
        for num in number_lst:
            if num in current_lst:
                pass
            else:
                if has_prefix(current_string) is True:
                    current_lst.append(num)
                    current_string += s[num]
                    anagrams_helper(s, number_lst, current_lst, current_string, length)
                    place = len(current_string) - 1
                    current_string = current_string[:place]
                    current_lst.pop()
                else:
                    break


def has_prefix(sub_s):
    """
    :param sub_s: the pre-check word made by recursion
    :return: True or False (the pre-check word is in the beginning of one word in dictionary)
    """
    global all_word
    for i in range(len(all_word)):
        word = all_word[i]
        boolean = word.startswith(sub_s)
        if boolean is True:
            return True


if __name__ == '__main__':
    main()
