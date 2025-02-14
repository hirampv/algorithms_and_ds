from data_structures import SinglyLinkedListNode

class Stack:
    def __init__(self, value):
        newNode = SinglyLinkedListNode(value)
        self.top = newNode

    def push(self, value):
        newNode = SinglyLinkedListNode(value)
        if self.top is None:
            self.top = newNode

        else:
            newNode.next = self.top
            self.top = newNode

    def pop(self):
        if self.top is None:
            return None
        
        else:
            nodeToReturn = self.top
            self.top = self.top.next
            nodeToReturn.next = None
            return nodeToReturn


    def print(self):
        outputString = "Top -> "
        tmp = self.top
        while(tmp):
            outputString += str(tmp.data) + " -> "
            tmp = tmp.next
        outputString += "None"
        print(outputString)


if __name__ == "__main__":
    print("Running ds_stack.py module")
    myStack = Stack(0)
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.print()

    print("Popping element at the top: ", myStack.pop().data)
    myStack.print()
