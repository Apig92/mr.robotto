from src.linked_list import Node
from src.linked_list import LinkedList

class Queue:

    def __init__(self):
        self.__list = LinkedList()
        self.__rear = Node()
        self.__front = Node()
        self.__size = 0

    def size(self):
        return self.__list.size()

    def is_empty(self):
        return self.size == 0

    def front(self):
        return self.__front

    def enqueue(self, elem):
        e = Node(elem)
        if self.__list.head() != None:
            self.__rear.set_next(e)
        else:
            self.__list.add_head(e)
            self.__front = e
        self.__rear = e

    def dequeue(self):
        if self.__list.head()!= None:
            temp = self.__front
            self.__list.remove_head()
            self.__front = self.__front.get_next()
            return temp.get_element()
        else:
            print('Queue is empty, cannot remove element!')
            return 1

    def __repr__(self):
        result = "-> "
        p = self.__list.head()
        print(p)
        if p is not None:
            while p is not None:
                result += "%s " % str(p.get_element())
                p = p.get_next()
        return result


