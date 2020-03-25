# node class
class Node:
    def __init__(self, pit, val):
        # pit string
        self.pit = pit
        # pit value
        self.val = val
        # next pit in counter clockwise direction
        self.next = None

    # get value of pit
    def get_val(self):
        return self.val

    # add to pit value
    def add_val(self, num):
        self.val += num

    # set pit value to 0
    def pick_up(self):
        self.val = 0

    # get pit string
    def get_pit(self):
        return self.pit

# circular linked list class
class CircularLinkedList:
    def __init__(self):
        # last pit
        self.tail = None

    # add pit to CLL
    def set_next(self, node):
        # if there is no tail set tail to pass node
        if not self.tail:
            self.tail = node
            # set tail node to point to itself
            self.tail.next = node
            return
        # get current tail
        cur = self.tail
        # set new node to point to what tail was pointing
        node.next = cur.next
        # set tail to point to new node
        cur.next = node
        # set tail to new node
        self.tail = node
