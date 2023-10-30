from dataclasses import dataclass
from typing import NoReturn


@dataclass
class Node:
    number: int = None
    next_node: "Node" = None


@dataclass
class Stack:
    node: Node = None

    def push(self, number: int) -> NoReturn:
        """
        Method that creates a new node and inserts a number
        specified as an argument inside this node.

        The `node` attribute of this stack needs to be changed to
        point to the new node. 

        Parameters
        ----------
        number : `int`
            The number to be inserted.

        Returns
        -------
        `NoReturn`
            This class doesn't returns anything.
        """ 
        auxiliar_node = Node(number=number)

        if self.node is None:
            self.node = auxiliar_node
            auxiliar_node.next_node = None
        else:
            auxiliar_node.next_node = self.node
            self.node = auxiliar_node
    
    def pop(self) -> int:
        """
        Method that removes the number of the last node added
        to the stack, and returns it.

        Before this, the number is saved into an auxiliar
        variable, and the `node` attribute of this stack
        is changed to point to the next node.
        
        Returns
        -------
        `int`
            The number to be removed.
        """
        if self.node is None:
            return -1
        else:
            number = self.node.number
            self.node = self.node.next_node
        
        return number
