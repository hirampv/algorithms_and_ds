from data_structures import SinglyLinkedListNode

class Queue:
    def __init__(self, value):
        newNode = SinglyLinkedListNode(value)
        self.front = newNode
        self.rear  = newNode

    def enqueue(self, value):
        newNode = SinglyLinkedListNode(value)
        
        if self.front is None:
            self.front = newNode
            self.rear  = newNode

        else:
            self.rear.next = newNode
            self.rear      = newNode


if __name__ == "__main__":
    myQueue = Queue(0)
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)