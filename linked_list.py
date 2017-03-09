class Node(object):
    """ A Node in a Linked List
    """

    def __init__(self, element=None):
        self.__next = None
        self.__element = element

    def get_next(self):
        return self.__next

    def get_element(self):
        return self.__element

    def set_next(self, next):
        self.__next = next

    def set_element(self, element):
        self.__element = element

    def __repr__(self):
        return "node: " + str(self.get_element())


class LinkedList(object):
    """ The List itself
    """

    def __init__(self, node=None):
        self.__first = node

    def head(self):
        return self.__first

    def add_tail(self, node):
        current = self.head()
        while not current.get_next() == None:
            current = current.get_next()
        current.set_next(node)

    def add_head(self, node):
        node.set_next(self.head())
        self.__first = node

    def remove_head(self):
        self.__first = self.__first.get_next()

    def size(self):
        result = 0
        current = self.head()
        while not (current is None):
            result += 1
            current = current.get_next()
        return result

    def __repr__(self):
        result = ""
        current = self.head()
        while not (current is None):
            result += " -> " + str(current)
            current = current.get_next()
        return result
