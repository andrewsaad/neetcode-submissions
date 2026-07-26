# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_add = next_add = None
        while head:
            next_add = head.next
            head.next = previous_add
            previous_add = head
            head = next_add
                

        return previous_add

        