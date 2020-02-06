
#-----------------------------Imports--------------------------------------#
from node import Node
from typing import Union
from dataclasses import dataclass
#--------------------------------------------------------------------------#


@dataclass
class Stack:
    size: int
    top: Union[None, Node]


def make_empty_stack():
    return Stack(0, None)


def push(stack, element):
    stack.top = Node(element, stack.top)
    stack.size = stack.size + 1


def top(stack):
    if is_empty(stack):
        raise IndexError("top of empty stack")
    return stack.top.value


def pop(stack):
    if is_empty(stack):
        raise IndexError("pop on empty stack")
    popped = stack.top.value
    stack.top = stack.top.rest
    stack.size = stack.size - 1
    return popped


def is_empty(stack):
    return stack.top is None


def size(stack):
    return stack.size
