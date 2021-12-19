"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

all_word = []
ans = []


def main():
	"""
	TODO:
	"""
	read_dictionary()
	row_lst = []  # row_lst is to record the entered letter
	for a in range(4):
		row = str(input(str(a + 1) + ' row of letters: '))
		row = row.lower()
		letter_list = row.split()
		switch = False
		if len(letter_list) != 4:
			switch = True
		else:
			for b in range(4):
				if len(letter_list[b]) != 1:
					switch = True
		if switch is True:
			print('Illegal format')
			break
		row_lst.append(letter_list)
	start = time.time()
	####################
	for i in range(4):
		for j in range(4):
			curr_lst = [4 * i + j]  # the place of the first letter
			boggle_helper(row_lst, row_lst[i][j], i, j, curr_lst)
	print('There are', len(ans), 'words in total.')
	###################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle_helper(row_lst, string, i, j, curr_lst):
	global all_word
	global ans
	if len(string) >= 4:  # base case!
		if string in all_word and string not in ans:
			print('Found', '"'+string+'"')
			ans.append(string)
			for x in range(-1, 2, 1):  # to check if there is word in dictionary that longer than 4 letters
				for y in range(-1, 2, 1):
					if x != 0 or y != 0:
						if 0 <= i + x < 4 and 0 <= j + y < 4:
							i += x
							j += y
							next_letter = row_lst[i][j]
							new_string = string+next_letter
							if new_string in all_word and new_string not in ans:
								print('Found', '"'+new_string+'"')
								ans.append(new_string)
							else:
								i -= x
								j -= y

	else:
		switch = False
		for m in range(-1, 2, 1):
			for n in range(-1, 2, 1):
				if m != 0 or n != 0:
					if 0 <= i+m < 4 and 0 <= j+n < 4:
						if has_prefix(string) is True:
							i += m
							j += n
							if 4 * i + j not in curr_lst:  # to make sure it would not add old letter place that has been choose
								next_letter = row_lst[i][j]
								string = string+next_letter
								curr_lst.append(4 * i + j)
								boggle_helper(row_lst, string, i, j, curr_lst)
								i -= m
								j -= n
								string = string[:(len(string)-1)]
								curr_lst.pop()
							else:
								i -= m
								j -= n
						else:
							switch = True  # if has_prefix is False means that it is not in dictionary
							break
			if switch is True:
				break


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global all_word
	with open(FILE, 'r') as f:
		for line in f:
			place = len(line) - 1
			word = line[:place]
			if len(word) >= 4:
				all_word.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global all_word
	for o in range(len(all_word)):
		word = all_word[o]
		boolean = word.startswith(sub_s)
		if boolean is True:
			return True



if __name__ == '__main__':
	main()
