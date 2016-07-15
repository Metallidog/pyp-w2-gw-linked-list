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
        
    def __repr__(self):
        return str(self.elem)


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if elements:
            self.start = Node(elements[0])
            place_holder = self.start
            for elem in elements[1:]:
                current_node = Node(elem)
                place_holder.next = current_node
                place_holder = current_node
            self.end = Node(elements[-1])
        
        else:
            self.start = None
            self.end = None

            
    def __str__(self):
        str_list = [None] * self.count()
        place_holder = self.start
        index = 0
        while place_holder is not None:
            str_list[index] = place_holder
            index += 1
            place_holder = place_holder.next
        return str(str_list)
        
    def __len__(self):
        return self.count()
    
    def __iter__(self):
        counter_node = self.start
        while counter_node:
            yield counter_node.elem
            counter_node = counter_node.next

    def __getitem__(self, index):
        if index >= self.count():
            raise IndexError
            
        place = self.start
        place = [place.next for place in xrange(index - 1)]
        return place[-1]

    def __add__(self, other):
        other_node = other.start
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

    def pop(self, index=None):
        before = self.start
        
        if index >= self.count() or self.start is None:
            raise IndexError()
            
        if index == 0:
            dummy = self.start.elem
            self.start = self.start.next
            return dummy
            
        if index == None:
            index = self.count()-1
        
        for i in xrange(index-1):
            before = before.next
            
        if before.next:    
            remove = before.next
            before.next = remove.next
            return remove.elem
        else:
            self.start = None
            return before.elem        
            