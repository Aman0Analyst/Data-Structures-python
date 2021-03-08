"""
Implementation of stacks using linked List

Functions Implemented
```````````````````````
getSize()   – Get the number of items in the stack.
isEmpty()   – Return True if the stack is empty, False otherwise.
peek()      – Return the top item in the stack. If the stack is empty, raise an exception.
push(value) – Push a value into the head of the stack.
pop()       – Remove and return a value in the head of the stack. If the stack is empty, raise an exception.

"""


class Node:
    def __init__(self, value):
        '''
        constructor for the new node to be interted in a stack
        parameters:
            value : value to be inserted in array
        '''
        self.value = value
        self.prev = None


class Stack:
    def __init__(self, value):
        '''
        Constructor for the stack
        '''
        self.top = Node(value)
        self.size = 1

    def __init__(self):
        self.top = None
        self.size = 0

    def isempty(self):
        '''
        Checks if stack is empty

        Return:
            bool : True if stack is empty
                   and False if stack is not Empty
        '''
        return self.size == 0

    def push(self, value):
        '''
        Pushes new Node in stack 

        Parameters:
            value : value to be stored in new node inserted
                    to stack

        '''
        node = Node(value)
        node.prev = self.top
        self.top = node
        self.size += 1

    def peek(self):
        if self.isempty():
            return "Stack is empty"
        else:
            tops = self.top.value
            return tops

    def pop(self):
        '''
        Pops the topmost element form the stack
        Return:
            popped element of the stack

        '''
        if self.size != 0:
            poping = self.top.value
            self.top = self.top.prev
            self.size -= 1
        else:
            return 'Stack is empty'
        return poping

    def __str__(self):
        '''
        A string representation function
        '''
        curr = self.top
        rep = ""
        while curr:
            rep = rep + str(curr.value) + " --> "
            curr = curr.prev
        return f"\n{rep[:-4]}\n"


if __name__ == '__main__':
    a = Stack()
    print('Pushing 8 new values to stack')
    for i in range(8):
        a.push(i)
    print('Calling Presentation of stack:')
    print(a)

    print('Calling Peek : ', a.peek())
    print('Calling Pop : ',  a.pop())
    print('caliing Peek : ', a.peek())

    print('Calling Presentation of stack:')
    print(a)
    print('Size of stack : ', a.size)

    print('Calling Push : 56')
    a.push(56)
    print('Calling Peek : ', a.peek())
    print('Calling Presentation of stack:')
    print(a)
    print('Size of stack : ', a.size)

    for _ in range(10):
        print('popped : ', a.pop())

    print('Is stack empty ? ',a.isempty())
    print(a.pop())
    print('Size of stack : ', a.size)
