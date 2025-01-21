from data_structures import SinglyLinkedListNode, SinglyLinkedList

def run():
    my_list = SinglyLinkedList(1)
    my_list.append(2)
    my_list.prepend(0)
    my_list.print()

if __name__ == '__main__':
    run()