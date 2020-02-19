from node import Node

class Mancala:
	def __init__(self):
		self.is_setup = False
		if not self.is_setup:
			self.set_up()
			self.is_setup = True
		self.show_board()

	def show_board(self):

		line_1 = '       |  B6 |  B5 |  B4 |  B3 |  B2 |  B1 |       '
		line_2_arr = ['B1','B2','B3','B4','B5','B6']
		line_2 = '       |'
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
					line_3 += '  '+player_store+' P1'
				else:
					line_3 += '  '+player_store+' P1'
			else:
				if len(player_store) == 1:
					line_3 = ' P2 '+player_store+'  '+line_3
				else:
					line_3 = ' P2 '+player_store+' '+line_3
		line_4_arr = ['A6','A5','A4','A3','A2','A1']
		line_4 = '       |'
		for i in range(6):
			current_pit = line_4_arr.pop()
			current_pit_val = str(self.pits_node[current_pit].get_val())
			if len(current_pit_val) == 1:
				line_4 += '  '+current_pit_val+'  |'
			else:
				line_4 += '  '+current_pit_val+' |'
		line_4 += '       '
		line_5 = '       |  A1 |  A2 |  A3 |  A4 |  A5 |  A6 |       '
		print('\n'+line_1+'\n'+line_2+'\n'+line_3+'\n'+line_4+'\n'+line_5)

	def set_up(self):
		pits = ['B6','B5','B4','B3','B2','B1','P1','A6','A5','A4','A3','A2','A1','P2']
		self.pits_node = {}
		for i in pits:
			if i in ['P1','P2']:
				self.pits_node[i] = Node(i, 0)
			else:
				self.pits_node[i] = Node(i, 4)
		last_pit = self.pits_node[pits[-1]]
		while len(pits) > 1:
			current_pit = pits.pop()
			current_pit_node = self.pits_node[current_pit]
			current_pit_node.set_next(self.pits_node[pits[-1]])
		self.pits_node[pits.pop()].set_next(last_pit)

	def player_pit(self, pit, player):
		stores = ['P1','P2']
		show_message = False
		if player == 'A':
			not_store = 'P2'
			store = 'P1'
		else:
			not_store = 'P1'
			store = 'P2'
		pit_value = self.pits_node[pit].get_val()
		current_pit = pit
		current_pit_node = self.pits_node[pit]
		current_pit_node.add_val(-pit_value)
		next_pit = current_pit_node.get_next()
		for i in range(pit_value):
			if next_pit.get_pit() == not_store:
				next_pit = next_pit.get_next()
			if i == pit_value-1 and next_pit.get_val() == 0 and next_pit.get_pit()[0] == pit[0]:
				if pit[0] == 'A':
					pit_across = 'B' + str(6-(int(next_pit.get_pit()[1])-1))
				else:
					pit_across = 'A' + str(6-(int(next_pit.get_pit()[1])-1))
				pit_across_val = self.pits_node[pit_across].get_val()
				self.pits_node[pit_across].add_val(-pit_across_val)
				self.pits_node[store].add_val(1+pit_across_val)
				show_message = True
				message = '>> Your last chip landed on an empty pit!\n>> You take '+next_pit.get_pit()+' and '+pit_across
			else:
				next_pit.add_val(1)
			if i != pit_value-1:
				next_pit = next_pit.get_next()
		if show_message:
			self.show_board()
			print(message)
		else:
			self.show_board()
		if next_pit.get_pit() in stores and next_pit.get_pit() != not_store:
			print('>> You landed in your store, go again!')
			return True
		return False
