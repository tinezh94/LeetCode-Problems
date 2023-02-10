"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

def removeElements(head, val):
    dummy = ListNode(next=head)
    prev, curr = dummy, head
    
    while curr:
        nxt = curr.next
        if curr.val == val:
            prev.next = nxt
        else:
            prev = curr
        
        curr.next = nxt
    
    return dummy.next