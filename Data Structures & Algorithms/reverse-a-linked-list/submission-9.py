# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_add = next_add = None
        while head:
            next_add = head.next # Getting the address of the next data
            head.next = previous_add # Setting the address of the current data to point at the previous data "reverse"
            previous_add = head # Setting previous data 
            head = next_add
                

        return previous_add

        