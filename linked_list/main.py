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
        return True if self.elem == other.elem else False

    def __repr__(self):
        pass


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
        pass

    def __len__(self):
        return self.count()

    def __iter__(self):
        counter_node = self.start
        while counter_node:
            yield counter_node
            counter_node = counter_node.next

    def __getitem__(self, index):
        counter = 0
        for node in self:
            if counter == index:
                return node
            counter += 1
            
    def _dd__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        other_node = other.start
        for item in self:
            if item == other_node:
                other_node = other_node.next
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

    def count(self):
        counter = 0
        for item in self:
            counter +=1
        return counter

    def pop(self, index=None):
        if index is None:
            index = self.count()-1
            
        if len(self) == 0 or index >= self.count():
            raise IndexError()
            
        if index == 0:
            dummy = self.start.elem
            self.start = self.start.next
            return dummy
        
        if self[index].next:    
            node = self[index-1]
            node.next = self[index].next
            return self[index].elem
        else:
            elem = self.start.elem
            self.start = None
            self.end = None
            return elem
            
        # for i in xrange(index-1):
        #     before = before.next
            
        # if before.next:    
        #     remove = before.next
        #     before.next = remove.next
        #     return remove.elem
        # else:
        #     self.start = None
        #     return before.elem        
            
