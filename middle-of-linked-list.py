"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

"""

def middleOfLinkedList(head):
    slow = fast = head 
    #step 0:
    # slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
    #slow at 1, fast at 1
    #step 1:
    # slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
    #slow at 2, fast at 3
    #step 2:
    # slow: [1, 2, 3, 4, 5], fast: [1, 2, 3, 4, 5]
    #slow at 3, fast at 5 
    # fast cannot move anymore and slow is at the midpoint, return slow
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        
    return slow
    

print(middleOfLinkedList([1,2,3,4,5]))
print(middleOfLinkedList([1,2,3,4,5,6]))