from node import Node
from node import LinkedList

class Mancala:
    def __init__(self):
        # All pits on the board
        self.pits = ["A1", "A2", "A3", "A4", "A5", "A6", "P1", "B1", "B2", "B3", "B4", "B5", "B6", "P2"]
        # Dictionary to hold pits and their node
        self.pit_nodes = {}
        # Turn pits into a node
        self.create_nodes()
        self.my_list = LinkedList()
        self.create_linked_list()
        self.show_board()

    def show_board(self):
        line_1 = "\n      B6 | B5 | B4 | B3 | B2 | B1       \n"
        line_2 = "      "
        B_pits = ["B6", "B5", "B4", "B3", "B2", "B1"]

        for pit in B_pits:
            pit_node = self.pit_nodes[pit]
            pit_val = pit_node.get_val()
            if pit_val > 9:
                line_2 += str(pit_val)
            else:
                line_2 += "0"+str(pit_val)
            if pit != B_pits[-1]:
                line_2 += " | "
            else:
                line_2 += "      \n"

        P2_node = self.pit_nodes["P2"]
        P2_val = P2_node.get_val()
        P1_node = self.pit_nodes["P1"]
        P1_val = P1_node.get_val()
        line_3 = "P2 "+ (str(P2_val) if P2_val > 9 else "0"+str(P2_val))+" --------------------------- "+(str(P1_val) if P1_val > 9 else "0"+str(P1_val))+" P1\n"
        line_4 = "      "
        A_pits = ["A1", "A2", "A3", "A4", "A5", "A6"]

        for pit in A_pits:
            node = self.pit_nodes[pit]
            val = node.get_val()
            if val > 9:
                line_4 += str(val)
            else:
                line_4 += "0"+str(val)
            if pit != A_pits[-1]:
                line_4 += " | "
            else:
                line_4 += "      \n"

        line_5 = "      A1 | A2 | A3 | A4 | A5 | A6      \n"
        print(line_1+line_2+line_3+line_4+line_5)

    def create_nodes(self):
        for pit in self.pits:
            if pit == "P1" or pit == "P2":
                current_pit = Node(pit, 0)
            else:
                current_pit = Node(pit, 4)
            self.pit_nodes[pit] = current_pit

    def create_linked_list(self):
        for pit in self.pits:
            node = self.pit_nodes[pit]
            self.my_list.set_next(node)

    def player_pit(self, pit, player):
        node = self.pit_nodes[pit]
        val = node.get_val()
        node.pick_up()
        cur = node.next
        to_add = []

        for i in range(val):
            to_add.append(cur)
            cur = cur.next
        self.add_pits(to_add)

        final = to_add[-1]
        final_pit = final.get_pit()
        player_pits = [("1", "A"), ("2", "B")]

        if final_pit in ["P1", "P2"]:
            if (final_pit[1], player) in player_pits:
                self.show_board()
                return True
        self.show_board()
        return False

    def add_pits(self, pit_arr):
        for pit in pit_arr:
            pit.add_val(1)

    def valid_pit(self, pit, player):
        if pit not in self.pits or pit[0] != player:
            return False
        node = self.pit_nodes[pit]
        val = node.get_val()
        return val > 0
