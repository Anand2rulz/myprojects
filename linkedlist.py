class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertendlf(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def deletion_e(self):
        if not self.head:
            print("no elements in linkedlist")
            return
        last_ind = self.length_l() - 1
        if last_ind == 0:
            self.head = None
            return
        temp = self.head
        for i in range(last_ind - 1):
            temp = temp.next
        temp.next = None

    def deletion_pos(self, pos):
        if pos > self.length_l() or pos <= 0:
            print("invalid position")
            return
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(1, pos - 1):
            temp = temp.next
        temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end="-->")
            temp = temp.next
        print("None")

    def length_l(self):
        length = 0
        temp = self.head
        while temp:
            temp = temp.next
            length += 1
        return length

# Test
a = Linkedlist()
a.insertendlf(30)
a.insertendlf(20)
a.insertendlf(10)
a.display()
a.deletion_pos(2)
a.display()

