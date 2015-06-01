#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sin título.py
#  
#  Copyright 2015 Agustin Hernan Marrone <agustinhmarrone@gmail.com>
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

# challenge link http://www.reddit.com/r/dailyprogrammer/comments/35s2ds/20150513_challenge_214_intermediate_pile_of_paper/
import numpy as np

canvasSize = (10,20) # row, cols
canvas = np.zeros(canvasSize)

sheets = [			
	[1, 5, 5, 10, 3],	# color, cornerX, cornerY, width, height
	[2, 0, 0, 7, 7]
]
	
	
def drawSheets():
	for sheet in sheets:
		for j in range(sheet[4]): # sheet row's iterator
			for k in range(sheet[3]): # sheet col's iterator
				canvas[sheet[2]+j][sheet[1]+k] = sheet[0] 


def getCanvasAreas():
	areas = {}
	for row in range(canvasSize[0]):
		for col in range(canvasSize[1]):
			key = int(canvas[row][col])
			areas[key]  = areas.get(key, 0) + 1
	return areas

def main():
	
	drawSheets()
	print getCanvasAreas()
	

if __name__ == '__main__':
	main()

