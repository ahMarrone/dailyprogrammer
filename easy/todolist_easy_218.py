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


# challenge link http://www.reddit.com/r/dailyprogrammer/comments/39ws1x/20150615_challenge_218_easy_todo_list_part_1/

class TodoList:
	
	def __init__(self):
		self.todoList = []
	
	def addItem(self,item):
		self.todoList.append(item)
		
	def removeItem(self,item):
		if item in self.todoList:
			self.todoList.remove(item)
		
	def printList(self):
		print "--- TODO LIST ---"
		for idx, val in enumerate(self.todoList,start=1):
			print str(idx) +  ": " + val
		print "\n"


def main():
	todo = TodoList()
	todo.addItem("Tarea 1")
	todo.addItem("Tarea 2")
	todo.addItem("Tarea 3")
	todo.printList()
	todo.removeItem("Tarea 2")
	todo.printList()
	

if __name__ == '__main__':
	main()

