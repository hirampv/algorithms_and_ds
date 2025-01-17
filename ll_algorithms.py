from data_structures import SinglyLinkedListNode

'''
    There are several ways to work with linked lists, the most common being:
        - Create a LinkedList class containing a head pointer (to a ll_node), and the methods to operate it
        - Use a simple head pointer to a node and create external functions to work with a list
'''

# Print the contents of a singly linked list
def sll_print(ll_head):
    outputStr = ""
    tmp = ll_head
    while tmp:
        outputStr += str(tmp.data) + " -> "
        tmp = tmp.next
        
    outputStr += "None"
    print(outputStr)


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

# The function needs to return a pointer/reference to the newly added first item
# because otherwise it is copied by value within this function
def sll_prepend(ll_head, value):
    newNode = SinglyLinkedListNode(value)
    newNode.next = ll_head
    ll_head = newNode
    return ll_head
    
    

def run():
    # Creating a linked list with just a head pointer
    newNode = SinglyLinkedListNode(1)
    llHead = newNode
    sll_append(llHead, 2)
    sll_append(llHead, 3)
    sll_append(llHead, 4)
    sll_append(llHead, 5)
    
    # We call the prepend funcion, but don't assign the return value to the original llHead variable
    # Therefore, the original list is not modified
    sll_prepend(llHead, 0)
    sll_print(llHead)
    
    # We call the prepend function and assign the return value to the original list
    # Hence, the list gets modified
    llHead = sll_prepend(llHead, 0)
    sll_print(llHead)


if __name__ == '__main__':
    run()