
class Node:
    def __init__(self, pit, value=4):
        self.pit = pit
        self.val = value
        self.next = None

    def add_val(self, num):
        self.val += num
