#!/bin/python3

class Node(object):
    def __init__(self, value):
        self.__value = value
        self.__next = None
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        self.__next = next
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value


class SinglyLinkedList(object):
    def __init__(self):
        self.__head = None
        self.__tail = None
    
    @property
    def head(self) -> Node:
        return self.__head
    
    @property
    def tail(self) -> Node:
        return self.__tail
    
    def append(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        
        if self.__head is None:
            self.__head = node
        
        if self.__tail is not None:
            self.__tail.next = node
        
        self.__tail = node
    
    def prepend(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        
        if self.__head is None and self.__tail is None:
            self.__head = node
            self.__tail = node
            return
        
        node.next = self.__head
        self.__head = node
    
    def remove(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        
        temp = self.__head
        counter = 0
        
        if index == 0:
            self.__head = self.__head.next
            del temp
            return
        
        while temp.next is not None:
            counter += 1
            
            if counter == index:
                node_to_delete = temp.next
                
                if node_to_delete.next is not None:
                    temp.next = node_to_delete.next
                else:
                    temp.next = None
                    self.__tail = temp
                
                del node_to_delete
                return
            
            temp = temp.next
    
    def add(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        node = Node(val)
        
        if index == 0:
            node.next = self.__head
            self.__head = node
            return
        
        temp = self.__head
        counter = 0
        
        while temp.next is not None:
            counter += 1
            
            if counter == index:
                node.next = temp.next
                temp.next = node
                return
            
            temp = temp.next
        
        if index == counter + 1:
            temp.next = node
            self.__tail = node
    
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        
        if index == 0:
            return self.__head.value
        
        temp = self.__head
        counter = 0
        
        while temp.next is not None:
            temp = temp.next
            counter += 1
            
            if counter == index:
                return temp.value
        
        return -1


if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    
    result = [
        linked_list.prepend(7),
        linked_list.prepend(2),
        linked_list.prepend(1),
        linked_list.add(3, 0),
        linked_list.remove(2),
        linked_list.prepend(6),
        linked_list.append(4),
        linked_list.get(4),
        linked_list.prepend(4),
        linked_list.add(5, 0),
        linked_list.prepend(6)
    ]
    
    assert result == [None, None, None, None, None, None, None, 4, None, None, None]