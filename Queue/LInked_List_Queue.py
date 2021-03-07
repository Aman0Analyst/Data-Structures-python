'''
Implementing queue using linked list

Operations on Queue:
Mainly the following four basic operations are performed on queue:

Enqueue(): Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
Dequeue(): Removes an item from the queue. The items are popped in the same order in which they are pushed.
         If the queue is empty,then it is said to be an Underflow condition.
Front(): Get the front item from queue.
Rear(): Get the last item from queue.


'''

class Node:
    def __init__(self,value):
        '''
        constructor for the new node to be interted in a queue
        parameters:
            value : value to be inserted in array
        '''
        self.value = value
        self.new = None

class Queue:
    def __init__(self,value):
        self.front = Node(value)
        self.rear = self.front
        self.front.new = self.rear 
        self.size = 1

    def enqueue(self,value):
        '''
        Pushes new Node in queue 
        
        Parameters:
            value : value to be stored in new node inserted
                    to queue

        '''
        node = Node(value)
        self.rear.new = node
        self.rear = node
        self.size += 1

    def dequeue(self):
        member = self.front.value
        self.front = self.front.new
        self.size -= 1
        return member    

    def front_element(self):
        if not self.isempty():
            return self.front.value
        else: return 'Empty queue'

    def rear_element(self):
        '''

        '''
        if not self.isempty():
            return self.rear.value    
        else: return 'Empty queue'

    def isempty(self):
        '''
        Checks if queue is empty
        
        Return:
            bool : True if queue is empty
                   and False if queue is not Empty
        '''
        if self.size == 0:
            return True
        else: return False    

    def __str__(self):
        '''
        A string representation function
        '''
        curr = self.front
        rep = ""
        while curr:
            rep = rep + str(curr.value) + " --> "
            curr = curr.new
        return f"\nFRONT >> {rep[:-4]} >> Rear\n"         


if __name__ == '__main__':
    a = Queue(5)

    for i in range(8):
        a.enqueue(i)
    
    print(a)

    print(a.front_element())
    print(a.rear_element())

    while not a.isempty():
        print(a.dequeue())
        print(a,'\n')

    print(a.front_element())
    print(a.rear_element())