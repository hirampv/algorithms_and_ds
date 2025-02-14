from data_structures import SinglyLinkedListNode

class Queue:
    def __init__(self, value):
        newNode = SinglyLinkedListNode(value)
        self.front = newNode
        self.rear  = newNode