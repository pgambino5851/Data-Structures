"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
# [1,3]
    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head == None:
            self.head = ListNode(value, None, None)
            self.tail = self.head
            print(f"New head is: {self.head.value}, {self.head.prev}, {self.head.next}")
            self.length += 1
            return self.head
        newHead = ListNode(value, None, self.head)
        self.head.prev = newHead
        self.head = newHead
        print(f"New head is: {self.head.value}, {self.head.prev}, {self.head.next.value}")
        self.length += 1
        return self.head


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head == None:
            return None
        if self.tail == self.head:
            currentHead = self.head
            self.tail = None
            self.head = None
            self.length =- 1
            return currentHead
        prevHead = self.head
        newHead = prevHead.next
        self.head = newHead
        prevHead.delete()
        self.length -= 1
        return prevHead.value
        
        # currentHead = self.head
        # newHead = self.head.next
        # newHead.prev = None
        # self.head = newHead
        # return currentHead


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail == None:
            self.tail = ListNode(value, None, None)
            self.head = self.tail
            self.length += 1
            return self.tail
        newTail = ListNode(value, self.tail, None)
        self.tail.next = newTail
        self.tail = newTail
        print(f"New head is: {self.tail.value}, {self.tail.prev}")
        self.length += 1
        return self.tail

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail == None:
            return None
        if self.tail == self.head:
            currentTail = self.tail
            self.tail = None
            self.head = None
            self.length =- 1
            return currentTail
        prevTail = self.tail
        newTail = prevTail.prev
        self.tail = newTail
        self.length -= 1
        prevTail = None
        return prevTail

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass


# dll = DoublyLinkedList()
# dll.add_to_head(10)
# print(dll.length)
# # dll.add_to_head(2)
# dll.remove_from_tail()
# # print(dll.remove_from_head())
# print(dll.head.value)

