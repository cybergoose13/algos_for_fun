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

    def getLast(self):
        value= self.head
        if self.isEmpty():
            return None
        for x in range(self.size() -1):
            value= value.next
        return value.data

    def size(self):
        counter= 0
        value= self.head
        while value:
            counter += 1
            value= value.next
        return counter

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


if __name__ == "__main__":
    list1= LinkedList()
    list1.head= Node('One')
    second= Node('second')
    third= Node('Third')
    fourth= Node('4th')
    last= Node('last')
    list1.head.next= second
    second.next= third
    third.next= fourth
    fourth.next= last

    list2= LinkedList()

    print(list1.getLast())
    print(list2.getLast())