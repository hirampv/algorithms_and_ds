# algorithms_and_ds
Back to practicing ye old Algorithms and Data Structures


# Singly Linked List Implementation

This repository contains the implementation of a singly linked list in Python. 
A singly linked list is a data structure where each node contains a value and a reference to the next node in the list.

## Features

- Implementation of a singly linked list.
- Basic operations such as adding, removing, and retrieving elements.
- Maintains references to both the first and last nodes for efficiency.

## Class Structure

### SinglyLinkedListNode

Class representing a node in the linked list.

#### Attributes:
- `data`: Holds the node's value.
- `next`: Reference to the next node in the list.

#### Constructor:
```python
SinglyLinkedListNode(data)
```

### SinglyLinkedList

Class representing the singly linked list.

#### Attributes:
- `head`: Reference to the first node in the list.
- `tail`: Reference to the last node in the list.

#### Methods:

- `__init__(data)`: Creates a list with an initial node.
- `print()`: Prints the list in a readable format.
- `append(data)`: Adds a node to the end of the list (O(1)).
- `prepend(data)`: Adds a node to the beginning of the list (O(1)).
- `pop()`: Removes and returns the last node of the list (O(n)).
- `pop_first()`: Removes and returns the first node of the list (O(1)).
- `remove(n)`: Removes and returns the node at position `n` (O(n)).
- `length()`: Returns the number of nodes in the list (O(n)).

## Usage

Example usage of the linked list:

```python
from data_structures import SinglyLinkedList

# Create a list with an initial node
linked_list = SinglyLinkedList(10)
linked_list.append(20)
linked_list.append(30)
linked_list.prepend(5)
linked_list.print()

# Remove a node
linked_list.pop()
linked_list.print()
```

## Time Complexity of Operations

| Operation    | Complexity |
|-------------|------------|
| Append      | O(1)       |
| Prepend     | O(1)       |
| Pop         | O(n)       |
| Pop First   | O(1)       |
| Remove(n)   | O(n)       |
| Length      | O(1)       |

## Notes / ToDo

- The `remove(n)` implementation does not correctly handle empty lists.
- The `pop()` function could be optimized for better performance.

## Contribution

If you would like to improve this implementation or add new features, feel free to fork the repository and submit a pull request.

## License

This project is distributed under the MIT license.



# Stack Data Structure Implementation

## Overview
This module implements a **Stack** data structure using a **singly linked list**. It provides standard stack operations such as **push**, **pop**, and **print**.

## Prerequisites
The implementation depends on the `SinglyLinkedListNode` class from the `data_structures` module. Ensure this dependency is available before using this stack.

## Class: `Stack`
The `Stack` class represents a stack data structure where elements follow the **Last In, First Out (LIFO)** principle.

### **Constructor**
```python
Stack(value)
```
- **Description**: Initializes a new stack with a single node.
- **Parameters**:
  - `value` (*any*): The initial value of the stack.
- **Usage**:
  ```python
  my_stack = Stack(10)
  ```

### **Methods**

#### `push(value)`
```python
push(value)
```
- **Description**: Adds a new element on top of the stack.
- **Parameters**:
  - `value` (*any*): The value to be added to the stack.
- **Usage**:
  ```python
  my_stack.push(20)
  ```

#### `pop()`
```python
pop() -> SinglyLinkedListNode | None
```
- **Description**: Removes and returns the top element from the stack.
- **Returns**:
  - The top node (*SinglyLinkedListNode*) if the stack is not empty.
  - `None` if the stack is empty.
- **Usage**:
  ```python
  popped_node = my_stack.pop()
  print(popped_node.data)  # Access the value
  ```

#### `print()`
```python
print()
```
- **Description**: Prints the current stack in the format:
  ```
  Top -> value1 -> value2 -> ... -> None
  ```
- **Usage**:
  ```python
  my_stack.print()
  ```

## Example Usage
```python
if __name__ == "__main__":
    print("Running ds_stack.py module")
    myStack = Stack(0)
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.print()

    print("Popping element at the top: ", myStack.pop().data)
    myStack.print()
```

## Notes
- The stack implementation is based on a **linked list**, so it does not have a predefined size limit.
- Operations like `push()` and `pop()` have **O(1) time complexity**.
- Ensure that the `data_structures` module containing `SinglyLinkedListNode` is correctly implemented and imported.

## Author
This module is part of a data structures library developed for educational and practical use cases.



# Queue Data Structure Implementation

## Overview
This module implements a **Queue** data structure using a **singly linked list**. It provides standard queue operations such as **enqueue**, **dequeue**, and **print**.

## Prerequisites
The implementation depends on the `SinglyLinkedListNode` class from the `data_structures` module. Ensure this dependency is available before using this queue.

## Class: `Queue`
The `Queue` class represents a queue data structure where elements follow the **First In, First Out (FIFO)** principle.

### **Constructor**
```python
Queue(value)
```
- **Description**: Initializes a new queue with a single node.
- **Parameters**:
  - `value` (*any*): The initial value of the queue.
- **Usage**:
  ```python
  my_queue = Queue(10)
  ```

### **Methods**

#### `enqueue(value)`
```python
enqueue(value)
```
- **Description**: Adds a new element at the rear of the queue.
- **Parameters**:
  - `value` (*any*): The value to be added to the queue.
- **Usage**:
  ```python
  my_queue.enqueue(20)
  ```

#### `dequeue()`
```python
dequeue() -> SinglyLinkedListNode | None
```
- **Description**: Removes and returns the front element from the queue.
- **Returns**:
  - The front node (*SinglyLinkedListNode*) if the queue is not empty.
  - `None` if the queue is empty.
- **Usage**:
  ```python
  dequeued_node = my_queue.dequeue()
  print(dequeued_node.data)  # Access the value
  ```

#### `print()`
```python
print()
```
- **Description**: Prints the current queue in the format:
  ```
  Front -> value1 -> value2 -> ... -> Rear
  ```
- **Usage**:
  ```python
  my_queue.print()
  ```

## Example Usage
```python
if __name__ == "__main__":
    myQueue = Queue(0)
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    myQueue.print()
    myQueue.dequeue()
    myQueue.print()
```

## Notes
- The queue implementation is based on a **linked list**, so it does not have a predefined size limit.
- Operations like `enqueue()` and `dequeue()` have **O(1) time complexity**.
- Ensure that the `data_structures` module containing `SinglyLinkedListNode` is correctly implemented and imported.

## Author
This module is part of a data structures library developed for educational and practical use cases.

