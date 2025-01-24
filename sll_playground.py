from data_structures import SinglyLinkedListNode, SinglyLinkedList

def run():
    my_list = SinglyLinkedList(1)
    my_list.append(2)
    my_list.append(3)
    my_list.prepend(0)
    my_list.print()

    print("Removing the element ", my_list.pop().data)
    my_list.print()

    print("Removing the element ", my_list.pop().data)
    my_list.print()

    print("Removing the element ", my_list.pop_first().data)
    my_list.print()

    print("Removing the element ", my_list.pop_first().data)
    my_list.print()

if __name__ == '__main__':
    run()