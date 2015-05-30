#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sin título.py
#  
#  Copyright 2015 Agustin <Agustin@AGUSTIN-NBK>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


# CHALLENGE LINK http://www.reddit.com/r/dailyprogrammer/comments/35l5eo/20150511_challenge_214_easy_calculating_the/
import sys
from math import sqrt, pow


def main():
	numbers = [int(x) for x in sys.argv[1:]]
	variance = sum([ pow(k - (sum(numbers) / len(numbers)),2) for k in numbers]) / len(numbers)
	deviation = sqrt(variance)
	print "Standard deviation is: " + str(deviation)

if __name__ == '__main__':
	main()

