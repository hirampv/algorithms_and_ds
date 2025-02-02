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
        self.length = 1

    def print(self):
        tmp = self.head
        print_str = ""
        while tmp:
            print_str += str(tmp.data) + " -> "
            tmp = tmp.next
        print_str += "None"
        print(print_str)

    # append() inserts a new node at the end of the list
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

        self.length += 1

    # prepend() inserts a new node at the beginning of the list
    def prepend(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    # pop() method: removes the last element from the list and returns it
    def pop(self):
        if self.head is None:
            return None
        
        if self.head is self.tail:
            node_to_pop = self.head
            self.head = None
            self.tail = None
            return node_to_pop
        
        tmp = self.head
        while tmp.next is not self.tail:
            tmp = tmp.next

        node_to_pop = self.tail
        self.tail = tmp
        tmp.next = None
        self.length -= 1
        return node_to_pop
    
    # pop_first() method: removes the first element from the list and returns it
    def pop_first(self):
        if self.head is None or self.head is self.tail:
            return self.pop()

        node_to_pop = self.head
        self.head = self.head.next
        node_to_pop.next = None
        self.length -= 1
        return node_to_pop
    
    # remove(n) method: removes and returns the nth node from the list
    def remove(self, n):
        if n == 0:
            return self.pop_first()

        tmp = SinglyLinkedListNode(0)
        tmp.next = self.head
        for _ in range(n):
            if not tmp.next:
                print("index out of bounds")
                return None
            tmp = tmp.next
        node_to_remove = tmp.next

        tmp.next = node_to_remove.next
        node_to_remove.next = None
        self.length -= 1
        return node_to_remove
        
    
    def get_length(self):
        '''
        length = 0
        tmp = self.head
        while tmp:
            tmp = tmp.next
            length += 1
        '''
        return self.length




