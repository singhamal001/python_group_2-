class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # head is default NULL
    def __init__(self):
        self.head = None

    # Checks if stack is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):

        if self.head == None:
            self.head = Node(data)

        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):

        if self.isempty():
            return None

        else:
            # Removes the head node and makes
            # the preceding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data