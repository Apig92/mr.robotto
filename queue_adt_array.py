class Queue:

    def __init__(self, arraySize):
        self.__array = [None]*arraySize
        self.__front = 0
        self.__rear = 0

    def size(self):
        n = len(self.__array)
        size = (n - self.__front + self.__rear) % n
        return (len(self.__array) - self.__front + self.__rear) % len(self.__array)

    def is_empty(self):
        return self.__rear == self.__front

    def front(self):
        return self.__array[self.__front]

    def dequeue(self):
        if self.is_empty():
            print('Cannot dequeue, queue is empty!')
            return 1
        temp = self.__array[self.__front]
        self.__array[self.__front] = None
        self.__front = (self.__front + 1)% len(self.__array)
        return temp

    def enqueue(self, elem):
        if self.size() == len(self.__array)-1:
            print('Queue is full, cannot enqueue!')
            return 1
        self.__array[self.__rear] = elem
        self.__rear = (self.__rear + 1)%len(self.__array)

    def __repr__(self):
        result = ""
        for item in self.__array:
            result += str(item)+' '
        return result