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
from singly_linked_list import SinglyLinkedList

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
| Length      | O(n)       |

## Notes / ToDo

- The `remove(n)` implementation does not correctly handle empty lists.
- The `pop()` function could be optimized for better performance.
- The list does not maintain a length variable, so `length()` traverses the entire list each time it is called.

## Contribution

If you would like to improve this implementation or add new features, feel free to fork the repository and submit a pull request.

## License

This project is distributed under the MIT license.

