"""
# TODO:
1. Create a stack. -> LIFO ✅
2. Create a queue. -> FIFO
3. Create a list.
"""
from structures import Stack
from random import choice
from typing import NoReturn
from structures.stack import Node

def display_stack(stack: Stack) -> NoReturn:
    actual_node: Node = stack.node

    while actual_node:
        print(f"The data inside the actual node is: {actual_node.number}", end="\n")
        actual_node = actual_node.next_node


if __name__ == "__main__":
    my_stack = Stack()

    for _ in range(1, 11):
        my_stack.push(choice(range(1, 11)))

    display_stack(my_stack)

    print("\n\n")
    
    while my_stack.node:
        print(f"😁 - {my_stack.pop() = }", end="\n")
    

