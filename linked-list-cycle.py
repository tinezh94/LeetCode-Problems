"""

141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the index of the node that 
tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

"""

def hasCycle(head):
    seen = set()

    while head:
        # if head is in seen, means there is a cycle created
        if head in seen:
            return True
        # if head is not in seen, add head to seen and point to the next val in head
        seen.add(head)
        head = head.next
    return False
        

print(hasCycle([3,2,0,-4]))
print(hasCycle([1,2]))
print(hasCycle([1]))