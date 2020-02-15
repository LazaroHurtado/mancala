from node import Node

class Mancala:
	def __init__(self):
		self.is_setup = False
		if not self.is_setup:
			self.set_up()
			self.is_setup = True
		self.show_board()

	def show_board(self):

		line_1 = '      |  B6 |  B5 |  B4 |  B3 |  B2 |  B1 |       '
		line_2_arr = ['B1','B2','B3','B4','B5','B6']
		line_2 = '      |'
		for i in range(6):
			current_pit = line_2_arr.pop()
			current_pit_val = str(self.pits_node[current_pit].get_val())
			if len(current_pit_val) == 1:
				line_2 += '  '+current_pit_val+'  |'
			else:
				line_2 += '  '+current_pit_val+' |'
		line_2 += '       '
		line_3 = '-------------------------------------'
		for i in ['P1','P2']:
			player_store = str(self.pits_node[i].get_val())
			if i == 'P1':
				if len(player_store) == 1:
					line_3 += ' '+player_store+'  P1'
				else:
					line_3 += ' '+player_store+' P1'
			else:
				if len(player_store) == 1:
					line_3 = ' '+player_store+'  P1' + line_3
				else:
					line_3 = ' '+player_store+' P1' + line_3
		line_4_arr = ['A6','A5','A4','A3','A2','A1']
		line_4 = '      |'
		for i in range(6):
			current_pit = line_4_arr.pop()
			current_pit_val = str(self.pits_node[current_pit].get_val())
			if len(current_pit_val) == 1:
				line_4 += '  '+current_pit_val+'  |'
			else:
				line_4 += '  '+current_pit_val+' |'
		line_4 += '       '
		line_5 = '      |  A1 |  A2 |  A3 |  A4 |  A5 |  A6 |       '
		print(line_1+'\n'+line_2+'\n'+line_3+'\n'+line_4+'\n'+line_5)

	def set_up(self):
		pits = ['B6','B5','B4','B3','B2','B1','P1','A6','A5','A4','A3','A2','A1','P2']
		self.pits_node = {}
		for i in pits:
			self.pits_node[i] = Node(i)
		last_pit = self.pits_node[pits[-1]]
		while len(pits) > 1:
			current_pit = pits.pop()
			current_pit_node = self.pits_node[current_pit]
			current_pit_node.set_next(self.pits_node[pits[-1]])
		self.pits_node[pits.pop()].set_next = last_pit
