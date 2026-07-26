# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_list = None
        
        while head:
            next_list = head.next       # 1. Save Node 2 before we cut the link
            head.next = previous_list   # 2. Node 1 now points back to None (flip!)
            previous_list = head        # 3. Move 'previous' up to Node 1
            head = next_list            # 4. Move 'head' forward to Node 2
            
        return previous_list  # When 'head' reaches None, 'previous_list' is the new head!