#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CHALLENGE LINK https://www.reddit.com/r/dailyprogrammer/comments/46zm8m/20160222_challenge_255_easy_playing_with_light/

# N -> number of bulbs
# m -> lights toogles
def start_game(n, v):
	bulbs_state = [False] * n
	print bulbs_state
	for run in v:
		ranges = sorted(int(x) for x in run)
		for i in range(ranges[0],ranges[1]+1):
			bulbs_state[i] = not bulbs_state[i]
	print sum(bulbs_state)
	
def main():
	start_game(10,[[3, 6],[0, 4],[7, 3],[9, 9]])

if __name__ == '__main__':
	main()
