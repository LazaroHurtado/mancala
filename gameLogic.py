from node import Node
from node import CircularLinkedList

# main class
class Mancala:
    def __init__(self):
        # all pits on the board
        self.pits = ["A1", "A2", "A3", "A4", "A5", "A6", "P1", "B1", "B2", "B3", "B4", "B5", "B6", "P2"]
        # dictionary to hold pits and their node
        self.pit_nodes = {}
        # turn pits into a node
        self.create_nodes()
        # linked list variable
        self.my_list = CircularLinkedList()
        # create linked list for all the nodes
        self.create_linked_list()
        # show current board state
        self.show_board()

    # show board method
    def show_board(self):
        # show all the B pits
        line_1 = "\n      B6 | B5 | B4 | B3 | B2 | B1       \n"
        # second which is incomplete for now
        line_2 = "      "
        # all B pits
        B_pits = ["B6", "B5", "B4", "B3", "B2", "B1"]
        # get each B pit
        for pit in B_pits:
            # find the node of the B pit
            pit_node = self.pit_nodes[pit]
            # get the value of the B pit
            pit_val = pit_node.get_val()
            # if the value is greater than 9 add the value to line 2
            if pit_val > 9:
                line_2 += str(pit_val)
            # else add the value to line 2 with a leading 0
            else:
                line_2 += "0"+str(pit_val)
            # if we aren't at the last pit add a '|' as a seperator
            if pit != B_pits[-1]:
                line_2 += " | "
            # else add spaces and a line break
            else:
                line_2 += "      \n"
        # get the node for player two's store
        P2_node = self.pit_nodes["P2"]
        # get player two's store value
        P2_val = P2_node.get_val()
        # get the node for player one's store
        P1_node = self.pit_nodes["P1"]
        # get the player one's store value
        P1_val = P1_node.get_val()
        # if player one's store value is less than 9 add the value with a leading 0
        # else add the full value
        player_one_line = " "+(str(P1_val) if P1_val > 9 else "0"+str(P1_val))+" P1\n"
        # if player two's store value is less than 9 add the value with a leading 0
        # else add the full value
        player_two_line = "P2 "+ (str(P2_val) if P2_val > 9 else "0"+str(P2_val))+" "
        # create line 3 with the player store values and 27 '-' as seperatores
        line_3 = player_two_line+("-"*27)+player_one_line
        # fourth line which is incomplete for now
        line_4 = "      "
        # all A pits
        A_pits = ["A1", "A2", "A3", "A4", "A5", "A6"]
        # get each A pit
        for pit in A_pits:
            # find the node of the A pit
            node = self.pit_nodes[pit]
            # get the value of the A pit
            val = node.get_val()
            # if the value is greater than 9 add the value to line 4
            if val > 9:
                line_4 += str(val)
            # else add the value to line 4 with a leading 0
            else:
                line_4 += "0"+str(val)
            # if we aren't at the last pit add a '|' as a seperator
            if pit != A_pits[-1]:
                line_4 += " | "
            # else add spaces and a line break
            else:
                line_4 += "      \n"
        # show all the A pits
        line_5 = "      A1 | A2 | A3 | A4 | A5 | A6      \n"
        # print all the lines to show the board
        print(line_1+line_2+line_3+line_4+line_5)

    # create node for pits
    def create_nodes(self):
        # iterate over all the possible pits
        for pit in self.pits:
            # check if the current pit is a store
            if pit == "P1" or pit == "P2":
                # if the pit is a store create a node for it with 0 as value
                current_pit = Node(pit, 0)
            # else create a node of the pit with a value of 4
            else:
                current_pit = Node(pit, 4)
            # add pit node to dictionary
            self.pit_nodes[pit] = current_pit

    # create linked list for pits
    def create_linked_list(self):
        # iterate over all possible pits
        for pit in self.pits:
            # get node of the pit
            node = self.pit_nodes[pit]
            # since pits are in order create the linked list wiht the node
            self.my_list.set_next(node)

    # play choosen pit
    def player_pit(self, pit, player):
        # get node of choosen pit
        node = self.pit_nodes[pit]
        # get value of choosen pit
        val = node.get_val()
        # set pit value to 0
        node.pick_up()
        # get the next pit in the linked list
        cur = node.next
        # variable to hold all the pits we reach
        to_add = []
        # track opponent store so we can skip it if we see it
        opponent_store = "P2" if player == "A" else "P1"

        # iterate for how many stones we found in the pit
        for i in range(val):
            # if the current pit we are seeing isn't the opponent's store
            # add the pit to the array
            if cur.get_pit() != opponent_store:
                to_add.append(cur)
            # get the next pit in the linked list
            cur = cur.next
        # add to all the pits we saw
        self.add_pits(to_add)

        # get the last pit we saw, which is in a node object
        final = to_add[-1]
        # turn the node object into pit string
        final_pit = final.get_pit()
        # check if the last pit we saw landed on players store
        go_again = self.go_again(final_pit)
        # check if the last pit we saw landed on an empty pit
        self.take_across(final, player)

        # show the new board with updated values
        self.show_board()
        # return whether or not the player landed on his store
        return go_again

    # add to all pit in passed array
    def add_pits(self, pit_arr):
        # iterate over array and add '1' to each pit
        for pit in pit_arr:
            pit.add_val(1)

    # check if passed pit is valid for the passed player
    def valid_pit(self, pit, player):
        # if the pit passed is not in all valid pit array then move is not valid.
        # if the letter of the pit does not match the letter of player then move is
        # not valid
        if pit not in self.pits or pit[0] != player:
            return False
        # get node of pit
        node = self.pit_nodes[pit]
        # get value of pit
        val = node.get_val()
        # if the value of the pit is greater than 0 the move is valid, else not
        return val > 0

    # check if last pit touched is a store
    def go_again(self, last):
        # return whether or not the last pit touched is a store
        return last[0] == "P"

    # if last pit touched is empty and on the players side take all stones on
    # the opposite side
    def take_across(self, last, player):
        # if the value of last pit is not one, because we already added a stone
        # to it, then it was not empty so we do not take across.
        # if the last pit's letter is not the player's letter then we do not
        # take across
        if last.get_val() != 1 or last.get_pit()[0] != player:
            return
        # statement to alert the players of the move
        print(">> You landed on an empty pit!")

        # get opponent's letter
        opponent = "B" if player == "A" else "A"
        # since last is a node get its pit string
        last_pit = last.get_pit()
        # get pit position of the last pit seen
        last_pos = int(last_pit[1])
        # get the pit across from the last pit
        across_pos = 7 - last_pos
        # get the pit string of the pit across using opponent letter and pit position
        across_pit = opponent+str(across_pos)
        # statement to alert the players of the move
        print(f">> You collect the stones on pit {across_pit} and {last_pit}")

        # get node of the pit across
        across_node = self.pit_nodes[across_pit]
        # get value of the pit across
        across_val = across_node.get_val()
        # set the value of the pit across to 0
        across_node.pick_up()
        # set the value of the last pit we touched to 0
        last.pick_up()

        # get the store of the player
        store_pit = "P1" if player == "A" else "P2"
        # get the player store's node
        store_node = self.pit_nodes[store_pit]
        # add to the store the value of the last pit and across pit
        store_node.add_val(across_val+1)
        return
