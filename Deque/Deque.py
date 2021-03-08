class Node:
    def __init__(self,value):
        '''
        constructor for the new node to be interted in a queue
        parameters:
            value : value to be inserted in array
        '''
        self.value = value
        self.rear = None
        self.front = None

class Deque:
    def __init__(self,value):
        self.front = Node(value)
        self.rear = self.front
        self.front_number = 1
        self.rear_number = 0

    def insert_front(self,value):
        node = Node(value)
        self.front.front = node
        node.rear = self.front
        self.front = node    
        self.front_number += 1

    def insert_rear(self,value):
        node = Node(value)
        self.rear.rear = node
        node.front = self.rear
        self.rear = node
        self.rear_number -= 1

    def delete_front(self):
        if self.rear_number == self.front_number:
            return "emmpty Deque"
        value = self.front.value
        self.front = self.front.rear
        self.front.front = None
        self.front_number -= 1
        return value

    def delete_rear(self):
        if self.rear_number == self.front_number:
            return "emmpty Deque"
        value = self.rear.value
        self.rear = self.rear.front
        self.rear.rear = None
        self.rear_number += 1
        return value

    def size(self):
        return self.front_number - self.rear_number


    def __str__(self):
        curr = self.front
        rep = ''
        while curr:
            rep = rep + f'{curr.value}'+ '-->'
            curr = curr.rear
        return rep[:-3]

if __name__ == "__main__":
    a = Deque(4)

    print('\nInserting elements from front')
    for i in range(4):
        a.insert_front(i)

    print(a)

    print('\nInserting elements from rear')
    for i in range(4):
        a.insert_rear(i)
        
    print(a)
    
    print('\nDeleting from front')
    value = a.delete_front()
    print(value)
    print(a)

    print('\nDeleting from Rear')
    value = a.delete_rear()
    print(value)
    print(a)

    print('\n')
    for i in range(a.size()+1):
        print(a.delete_front())
        print(a)