"""
File: hangman.py
Name: Jacky
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    We will find if certain letter is in the word, the user will only have N_turns wrong times to guess the letter,
    and if it's right, the letter will shows in the word; otherwise, the times to guess will decrease.
    """
    n = N_TURNS  # n times to guess
    ans = ""
    o = b = str(random_word())  # define certain random_word to o and b
    for i in range(len(b)):
        ans += "-"
    while True:
        if n == 0:  # if all times are used(n=0), the loop will break.
            break
        if n > 0:
            print("The word looks like: " + ans)
            print("You have " + str(n) + " guesses left.")
            a = input("Your guess: ")  # a is the letter that user guess
            if len(a) == 1:
                if a.isalpha():  # check if the guess(a) is one letter and is alphabet
                    a = a.upper()
                    if b.find(a) != (-1):  # if the letter is in the word
                        p = 0
                        o = b  # recover certain random_word to o
                        while o.find(a) != (-1):  # check if a is in o
                            m = o.find(a)  # the site that a in o(o might be shortened)
                            q = p + m  # the real site in this certain random_word
                            ans1 = ""
                            for j in range(len(b)):  # renew ans by ans1
                                if q == j:  # the real site of a in certain random_word will be turned into a
                                    ans1 += a
                                elif ans[j].isalpha():  # if the letter in ans was alphabet already, keep the alphabet
                                    ans1 += ans[j]
                                elif not ans[j].isalpha():  # otherwise, we add - to ans1
                                    ans1 += "-"
                            ans = ans1  # renew ans1 to ans
                            o = o[(m + 1):]  # check the part after the site we find guess of in certain random_word
                            p = m + 1  # p used to record the first site of o
                        print("You are correct!")
                        if ans.isalpha():  # break when all the letters are guessed in certain random_word
                            break
                    else:
                        n -= 1  # if the guess is not in word, times decrease.
                        print("There is no " + a.upper() + "'s in the word")
                else:
                    print("Illegal format.")  # wrong guess format
            else:
                print("Illegal format.")  # wrong guess format
    if ans.isalpha():  # if there are still times to be used(n>0)
        print("You win!!")
        print("The word was: " + b)
    if n == 0:  # if all times are used(n=0)
        print("You are completely hung:(")
        print("The word was: " + b)






def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
