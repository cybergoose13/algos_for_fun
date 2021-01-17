'''
    Practice with linked lists
'''

class Node:
    def __init__(self, data=None):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def push(self, item):
        if self.isEmpty():
            self.head= Node(item)
            return
        else:
            self.getLastNode().next= Node(item)

    def pop(self):
        if self.isEmpty():
            return None
        elif self.size() == 1:
            self.head = None
        else:
            value= self.head
            for x in range(self.size() - 2):
                value= value.next
            value.next = None

    def pushToFront(self, item):
        if self.isEmpty():
            self.push(item)
        lst= self.toList()
        self.head= Node(item)
        for i in range(len(lst)):
            self.push(lst[i].data)

    def getLastValue(self):
        if self.isEmpty():
            return None
        return self.getLastNode().data

    def getLastNode(self):
        value= self.head
        if self.isEmpty():
            return None
        for x in range(self.size() - 1):
            value= value.next
        return value

    def size(self):
        counter= 0
        value= self.head
        while value:
            counter += 1
            value= value.next
        return counter

    def toList(self):
        if self.isEmpty():
            return None
        value= self.head
        lst= [value]
        for i in range(self.size() -1):
            value= value.next
            lst.append(value)
        return lst

    def indexOf(self, item):
        counter= 0
        value= self.head
        while value:
            if value.data == item:
                return counter
            counter += 1
            value= value.next
        return None

    def valueAt(self, indx):
        if self.isEmpty():
            return None
        value= self.head
        if indx > self.size() - 1:
            return None
        for i in range(indx):
            value= value.next
        return value

    def contains(self, item):
        value= self.head
        while value:
            if value.data == item:
                return True
            value= value.next
        return False

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def printList(self):
        value= self.head
        while value:
            print(value.data)
            value= value.next


