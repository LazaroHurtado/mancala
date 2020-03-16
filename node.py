
class Node:
    def __init__(self, pit, val):
        self.pit = pit
        self.val = val
        self.next = None

    def get_val(self):
        return self.val

    def add_val(self, num):
        self.val += num

    def pick_up(self):
        self.val = 0

    def get_pit(self):
        return self.pit

class LinkedList:
    def __init__(self):
        self.tail = None

    def set_next(self, node):
        if not self.tail:
            self.tail = node
            self.tail.next = node
            return
        cur = self.tail
        node.next = cur.next
        cur.next = node
        self.tail = node
