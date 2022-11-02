"""
206. Inverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

"""

def inverseLinkedList(head):
    prev, curr = None, head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        
    return prev
    
print(inverseLinkedList([1,2,3,4,5]))
print(inverseLinkedList([1,2]))