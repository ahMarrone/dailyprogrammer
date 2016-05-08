#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CHALLENGE LINK https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/


def is_valid_vector(n, v):
	valid = True
	for k in v:
		if k != n:
			valid = False
	return valid

def get_sums(v):
	sum_rows = [0]* len(v)
	sum_cols = [0]* len(v)
	sum_diagonals = [0,0]
	for i,row in enumerate(v):
		sum_diagonals[0] += v[i][i]
		sum_diagonals[1] += v[i][-(i+1)]
		for j,col in enumerate(row):
			sum_rows[i] += v[i][j]
			sum_cols[i] += v[j][i]
	return [sum_rows, sum_cols, sum_diagonals]

# Return True if m is a magis square.
# It may be better!
# Check te link
def is_magic_square(v):
	sums = get_sums(v)
	n = sums[0][0]
	print (is_valid_vector(n,sums[0]) and is_valid_vector(n,sums[1]) and is_valid_vector(n,sums[2]))
	
def main():
	is_magic_square([[8, 1, 6],[3, 5, 7],[4, 9, 2]])
	is_magic_square([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
	is_magic_square([[3, 5, 7], [8, 1, 6], [4, 9, 2]])
	is_magic_square([[8, 1, 6], [7, 5, 3], [4, 9, 2]])

if __name__ == '__main__':
	main()

