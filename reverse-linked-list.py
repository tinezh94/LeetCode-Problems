"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

"""

# def reverseList(head):
#     # T: O(n) M: O(1)
#     prev, curr = None, head
    
#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr.next = nxt
    
#     return prev


def reverseList(head):
    # T: O(n) M: O(n)
    if not head: return None
    
    newHead = head
    if head.next: 
        newHead = reverseList(head.next)
        head.next.next =  head
    
    head.next = None
    
    return newHead