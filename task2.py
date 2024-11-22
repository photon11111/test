from collections import deque

class EmptyQueueError(Exception):
    '''raised when queue is empty and operation requires at least one element in queue'''
    pass

class Queue1:
    class _QueueNode:
        def __init__(self, value, next):
            self._nodeValue = value
            self._nextNode = next

        @property
        def value(self):
            return self._nodeValue
        
        @property
        def next(self):
            return self._nextNode
        
        @next.setter
        def next(self, new_node):
            self._nextNode = new_node
        
    def __init__(self, bufferSize):
        if bufferSize < 1:
            raise ValueError("buffer size can't be zero or negative")

        self._head = None
        self._tail = None
        self._capacity = bufferSize
        self._length = 0

    def __len__(self):
        return self._length

    @property
    def capacity(self):
        '''max queue length'''
        return self._capacity

    def isEmpty(self):
        '''checks if any element contains in queue'''
        return len(self) == 0
    
    def peek(self):
        '''retrieves the first element in the queue without its deletion'''
        if self.isEmpty():
            raise EmptyQueueError("operation requires at least one element in queue")
        
        return self._head.value
    
    def enqueue(self, value):
        '''includes the element at the end of the queue'''
        newNode = self._QueueNode(value, None)

        if self._length == 0:
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.next = newNode
            self._tail = newNode

        self._length += 1

        if len(self) > self.capacity:
            self.dequeue()

    def dequeue(self):
        '''removes and retrieves the first element in the queue'''
        if self.isEmpty():
            raise EmptyQueueError("operation requires at least one element in queue")
        
        toReturn = self._head.value
        self._head = self._head.next
        self._length -= 1

        return toReturn

class Queue2:
    def __init__(self, bufferSize):
        if bufferSize < 1:
            raise ValueError("buffer size can't be zero or negative")
        
        self._buffer = deque(maxlen=bufferSize)
        self._capacity = bufferSize

    def __len__(self):
        return len(self._buffer)
    
    @property
    def capacity(self):
        '''max queue length'''
        return self._capacity

    def isEmpty(self):
        '''checks if any element contains in queue'''
        return len(self) == 0
    
    def peek(self):
        '''retrieves the first element in the queue without its deletion'''
        if self.isEmpty():
            raise EmptyQueueError("operation requires at least one element in queue")
        
        return self._buffer[0]
    
    def enqueue(self, value):
        '''includes the element at the end of the queue'''
        self._buffer.append(value)

    def dequeue(self):
        '''removes and retrieves the first element in the queue'''
        try:
            return self._buffer.popleft()
        except IndexError:
            raise EmptyQueueError("operation requires at least one element in queue")
        
class Queue3:
    def __init__(self, bufferSize):
        if bufferSize < 1:
            raise ValueError("buffer size can't be zero or negative")
        
        self._capacity = bufferSize
        self._buffer = []

    def __len__(self):
        return len(self._buffer)

    @property
    def capacity(self):
        '''max queue length'''
        return self._capacity
    
    def isEmpty(self):
        '''checks if any element contains in queue'''
        return len(self) == 0
    
    def peek(self):
        '''retrieves the first element in the queue without its deletion'''
        if self.isEmpty():
            raise EmptyQueueError("operation requires at least one element in queue")
        
        return self._buffer[0]
    
    def enqueue(self, value):
        '''includes the element at the end of the queue'''
        self._buffer.append(value)

        if len(self) > self.capacity:
            self.dequeue()

    def dequeue(self):
        '''removes and retrieves the first element in the queue'''
        if self.isEmpty():
            raise EmptyQueueError("operation requires at least one element in queue")
        
        return self._buffer.pop(0)
    
class Queue4:
    def __init__(self, bufferSize):
        if bufferSize < 1:
            raise ValueError("buffer size can't be zero or negative")
        
        self._buffer1 = []
        self._buffer2 = []
        self._capacity = bufferSize

    def __len__(self):
        return len(self._buffer1) + len(self._buffer2)
    
    @property
    def capacity(self):
        '''max queue length'''
        return self._capacity
    
    def isEmpty(self):
        '''checks if any element contains in queue'''
        return len(self) == 0
    
    def peek(self):
        '''retrieves the first element in the queue without its deletion'''
        if self.isEmpty():
            raise EmptyQueueError("operation requires at least one element in queue")
        
        if len(self._buffer1) > 0:
            return self._buffer1[0]
        
        return self._buffer2[-1]
    
    def enqueue(self, value):
        '''includes the element at the end of the queue'''
        self._buffer1.append(value)

        if len(self) > self.capacity:
            self.dequeue()

    def dequeue(self):
        '''removes and retrieves the first element in the queue'''
        if self.isEmpty():
            raise EmptyQueueError("operation requires at least one element in queue")
        
        if len(self._buffer2) == 0:
            while len(self._buffer1) > 0:
                self._buffer2.append(self._buffer1.pop())

        return self._buffer2.pop()

class Queue5:
    def __init__(self, bufferSize):
        if bufferSize < 1:
            raise ValueError("buffer size can't be zero or negative")
        
        self._buffer = [None] * bufferSize
        self._length = 0
        self._head = 0
        self._tail = 0

    def __len__(self):
        return self._length

    @property
    def capacity(self):
        '''max queue length'''
        return len(self._buffer)
    
    def isEmpty(self):
        '''checks if any element contains in queue'''
        return len(self) == 0
    
    def peek(self):
        '''retrieves the first element in the queue without its deletion'''
        if self.isEmpty():
            raise EmptyQueueError("operation requires at least one element in queue")
        
        return self._buffer[self._head]

    def enqueue(self, value):
        '''includes the element at the end of the queue'''
        if len(self) == self.capacity:
            self._head = (self._head + 1) % self.capacity
        else:
            self._length += 1

        self._buffer[self._tail] = value
        self._tail = (self._tail + 1) % self.capacity

    def dequeue(self):
        '''removes and retrieves the first element in the queue'''
        if self.isEmpty():
            raise EmptyQueueError("operation requires at least one element in queue")

        toReturn = self._buffer[self._head]
        self._head = (self._head + 1) % self.capacity
        self._length -= 1
        return toReturn