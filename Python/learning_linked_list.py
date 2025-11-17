class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next
class Solution:
    def insertAtHead(self, head,newData):
        newNode = Node(newData, head)
        return newNode
    def printList(self, head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp= temp.next
        print()

if __name__== "__main__":
    '''
    arr=[1,3,5,6]
    y=Node(arr[0])
    print(y)
    print(y.data)
    '''
    sol= Solution()
    head=Node(2)
    head.next=Node(3)
    print("Original List :")
    sol.printList(head)
    head=sol.insertAtHead(head,1)
    print("After insert at head : ")
    sol.printList(head)

