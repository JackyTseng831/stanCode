"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the input number
	:return: the largest digit in the number
	"""
	if n < 0:  # negative number
		m = n * -1
		return find_largest_digit(m)  # m is a positive number now
	else:  # positive number
		if n < 10:  # Base case!
			n = int(n)
			return n
		elif n % 100 > 0 and n % 10 > 0:
			if (n % 10) * 10 >= n % 100:  # units digit > tens digit
				m = (n - n % 100) / 10 + n % 10
				return find_largest_digit(m)
			else:  # units digit < tens digit
				m = (n - (n % 10)) / 10
				return find_largest_digit(m)


if __name__ == '__main__':
	main()
