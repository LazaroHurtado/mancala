
class Node:
	def __init__(self, pit):
		self.pit = pit
		self.val = 4
		self.next = None

	def get_val(self):
		return self.val

	def add_val(self, num):
		self.val += num

	def pick_up(self):
		self.val = 0

	def set_next(self, next_node):
		self.next = next_node

	def get_next(self):
		return self.next

class LinkedList:
	def __init__(self, node):
		self.node = node

	def get_next(self):
		return self.node.next
