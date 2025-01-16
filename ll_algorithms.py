from data_structures import SinglyLinkedListNode

'''
    There are several ways to work with linked lists, the most common being:
        - Create a LinkedList class containing a head pointer (to a ll_node), and the methods to operate it
        - Use a simple head pointer to a node and create external functions to work with a list
'''

# Print the contents of a singly linked list
def sll_print(ll_head):
    values = []
    tmp = ll_head
    while tmp:
        values.append(str(tmp.data))
        tmp = tmp.next
        
    print(' -> '.join(values))


# Function to append nodes at the end of a singly linked list
# Args:
#   linkedList 
#   value - data in the new node
def sll_append(ll_head, value):
    newNode = SinglyLinkedListNode(value)
    if ll_head is None:
        ll_head = newNode
        return True
    
    tmp = ll_head
    while tmp.next:
        tmp = tmp.next
        
    tmp.next = newNode
    return True
    
    
    

def run():
    # Creating a linked list with just a head pointer
    newNode = SinglyLinkedListNode(1)
    llHead = newNode
    sll_append(llHead, 2)
    sll_append(llHead, 3)
    sll_append(llHead, 4)
    sll_append(llHead, 5)
    
    sll_print(llHead)


if __name__ == '__main__':
    run()