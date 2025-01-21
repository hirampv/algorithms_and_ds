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

'''
    Class definition for a singly linked list
    The class contains two elements:
        head: a pointer to the first element
        tail: a pointer to the last element
        We could also include an integer for the list's length or size, but it would not
        contrubute much to the list's performance or usability
'''
class SinglyLinkedList:
    def __init__(self, data):
        new_node = SinglyLinkedListNode(data)
        self.head = new_node
        self.tail = new_node

    def print(self):
        tmp = self.head
        print_str = ""
        while tmp:
            print_str += str(tmp.data) + " -> "
            tmp = tmp.next
        print_str += "None"
        print(print_str)

    def append(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        
        # By having a tail pointer to the last element on the list
        # We improve the append function's perfomrance from O(n) to O(1)
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
