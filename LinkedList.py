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
        pass

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
    list1.head.next= second
    second.next= third
    third.next= fourth

    list2= LinkedList()

    print(list1.size())
    print(list2.size())