'''
    Class definition for the node of a singly linked list
    The node contains two elements:
        data: any information contained within the node
        next: pointer/reference to the next node on the list
'''
class SinglyLinkedListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None