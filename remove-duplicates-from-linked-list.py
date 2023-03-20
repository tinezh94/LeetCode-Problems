"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

"""

def removeDuplicates(head):
    dummy = ListNode(next=head)
    prev, curr = None, head
    
    seen = set()
    while curr:
        nxt = curr.next
        if curr.val in seen:
            prev.next = nxt 
        else:
            seen.add(curr.val)
            prev = curr 
        
        curr = nxt 
    
    return dummy.next