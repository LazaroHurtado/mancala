from node import Node

class GameLogic:
    def __init__(self, player_mapping):
        self.all_pits = ["A1","A2","A3","A4","A5","A6","P1",
                         "B1","B2","B3","B4","B5","B6","P2"]
        self.pit_nodes = self.set_nodes()
        self.player_mapping = player_mapping

    def show_board(self):
        first_line = ""
        second_line = ""

        p2_store = self.pit_nodes["P2"]
        p1_store = self.pit_nodes["P1"]
        if p2_store.val < 10:
            p2_val = "0" + str(p2_store.val)
        else:
            p2_val = str(p2_store.val)
        if p1_store.val < 10:
            p1_val = "0" + str(p1_store.val)
        else:
            p1_val = str(p1_store.val)
        third_line = "P2 "+ p2_val + " " + "-"*29 + " " + p1_val + " P1"

        fourth_line = " "*7
        fifth_line = " "*7
        for i in range(len(self.all_pits)-1):
            pit = self.all_pits[i]
            pit_node = self.pit_nodes[pit]
            next_pit = self.all_pits[i+1]

            letter = pit[0]
            next_letter = next_pit[0]

            if letter == "B":
                first_line = pit + first_line
                if pit_node.val < 10:
                    second_line = "0" + str(pit_node.val) + second_line
                else:
                    second_line = str(pit_node.val) + second_line
            elif letter == "A":
                fifth_line += pit
                if pit_node.val < 10:
                    fourth_line += "0" + str(pit_node.val)
                else:
                    fourth_line += str(pit_node.val)
            else:
                continue

            if next_letter == "B":
                first_line = " | " + first_line
                second_line = " | " + second_line
            elif next_letter == "A":
                fourth_line += " | "
                fifth_line += " | "
        first_line = "\n" + " "*7 + first_line + "\n"
        second_line = " "*7 + second_line + "\n"
        third_line += "\n"
        fourth_line += "\n"
        fifth_line += "\n"

        full_board = first_line+second_line+third_line+fourth_line+fifth_line
        print(full_board)

    def set_nodes(self):
        node_mapping = {}
        current_node = None
        for pit in self.all_pits:
            pit_letter = pit[0]
            if pit_letter == "P":
                node = Node(pit, 0)
            else:
                node = Node(pit)

            if current_node:
                current_node.next = node
            node_mapping[pit] = node
            current_node = node

        first_pit = self.all_pits[0]
        first_node = node_mapping[first_pit]
        current_node.next = first_node

        return node_mapping

    def valid_pit(self, player, pit):
        pit = pit.upper()
        correct_letter = self.player_mapping[player]
        pit_letter = pit[0]
        if pit_letter == correct_letter and pit in set(self.all_pits):
            return True
        return False

    def move(self, player, pit):
        pit_node = self.pit_nodes[pit]
        pit_val = pit_node.val

        current_node = pit_node
        for i in range(pit_val):
            node = current_node.next
            node.add_val(1)
            current_node = node

        pit_node.add_val(-pit_val)

        player_letter = self.player_mapping[player]
        if player_letter == "A":
            player_store = "P1"
        else:
            player_store = "P2"

        last_pit = current_node.pit
        last_pit_letter = last_pit[0]
        if last_pit_letter == player_letter and current_node.val == 1:
            return self.take_across(player, last_pit)
        return last_pit == player_store

    def take_across(self, player, pit):
        current_pit_num = pit[1]
        opposite_pit_num = abs(7-int(current_pit_num))

        player_letter = self.player_mapping[player]
        if player_letter == "A":
            opposite_pit_letter = "B"
            store = "P1"
        else:
            opposite_pit_letter = "A"
            store = "P2"

        current_pit_node = self.pit_nodes[pit]
        opposite_pit = opposite_pit_letter + str(opposite_pit_num)
        opposite_pit_node = self.pit_nodes[opposite_pit]
        opposite_pit_val = opposite_pit_node.val

        current_pit_node.add_val(-1)
        opposite_pit_node.add_val(-opposite_pit_val)

        store_node = self.pit_nodes[store]
        store_node.add_val(1+opposite_pit_val)
        return False

    def game_ended(self, p1, p2):
        p1_pits = 0
        p2_pits = 0

        p1_store = self.pit_nodes["P1"]
        p2_store = self.pit_nodes["P2"]

        for pit, node in self.pit_nodes.items():
            pit_letter = pit[0]
            if pit_letter == "A":
                p1_pits += node.val
            elif pit_letter == "B":
                p2_pits += node.val

        if p1_pits == 0 or p2_pits == 0:
            return self.end_game(p1, p2, p1_pits, p1_store.val, p2_pits, p2_store.val)
        return False

    def end_game(self, p1, p2, p1_pits, p1_store, p2_pits, p2_store):
        p1_total = p1_pits + p1_store
        p2_total = p2_pits + p2_store

        print(f"{p1} has {p1_total}")
        print(f"{p2} has {p2_total}")

        if p1_total > p2_total:
            print(f"The winner is {p1}")
        else:
            print(f"The winner is {p2}")
        return True
