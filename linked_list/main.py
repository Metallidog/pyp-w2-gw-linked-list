class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.
    
    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """

    def __str__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def pop(self, index=None):
        raise NotImplementedError()


class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        return self.elem == other.elem
        
    repr = str


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if elements:
            elements = list(elements)
            self.length = len(elements)
            self.end = self.start = Node(elements[0])
            for elem in elements[1:]:
                current_node = Node(elem)
                self.end.next = current_node
                self.end  = current_node
        else:
            self.start = None
            self.end = None
            self.length = 0
            
    def __str__(self):
        LL_str = '['
        for index, node in enumerate(self, start=1):
            end = ']' if index == self.length else ', '
            LL_str += "{}{}".format(node, end)
        return LL_str if LL_str[-1]==']' else LL_str + ']' 
        
    __repr__ = __str__
    
    def __len__(self):
        return self.count()
    
    def __iter__(self):
        counter_node = self.start
        while counter_node:
            yield counter_node.elem
            counter_node = counter_node.next

    def __getitem__(self, index):
        if index >= self.length or index < -self.length:
            raise IndexError('LinkedList index out of range')
            
        if isinstance(index, int) is False:
            raise TypeError('LinkedList indices must be integers')
            
        place = self.start
        loop_range = index if index >= 0 else index+self.length
        for _ in range(loop_range):
            place = place.next
        return place.elem

    def __add__(self, other):
        other_node = other.start
        self.length += len(other)
        while other_node:
            self.end = other_node
            self.end = self.end.next 
            other_node = other_node.next
        return self     
        
    def __iadd__(self, other):
        return self + other

    def __eq__(self, other):
        other_node = other.start
        self_node = self.start
        while self_node is not None:
            if self_node == other_node:
                other_node = other_node.next
                self_node = self_node.next
            else:
                return False
        return True

    def append(self, elem):
        new_end = Node(elem)
        self.length += 1
        if self.end:
            self.end.next = new_end
            self.end = new_end
        else:
            self.start = new_end
            self.end = new_end
        return self

    def count(self):
        count = 0
        dummy = self.start
        while dummy is not None:
            count += 1
            dummy = dummy.next
        return count
        #return self.length
    
    def pop(self, index=None):
        before = self.start
 
        if index == None:
            index = self.length-1
            
        if index >= self.length or self.start is None:
            raise IndexError()
            
        if index == 0:
            temp = self.__getitem__(0)
            self.start = self.start.next
            self.length -= 1
            return temp
        
        for _ in xrange(index-1):
            before = before.next
        
        if self.length > 1:
            remove = before.next
            before.next = remove.next
            self.length -= 1
            return remove.elem
        else:
            self.start = None
            self.length -= 1
            return before.elem        
            