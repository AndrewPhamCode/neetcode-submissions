# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #set a dummy 
        left = dummy 
        right = head
        #keep the distance from l to r to n
        while n > 0 and right:  
            right = right.next
            n -= 1 
        #inex until right hits the end of the linked list 
        while right:
            left = left.next 
            right = right.next 
        #delete the node
        left.next = left.next.next 
        return dummy.next

