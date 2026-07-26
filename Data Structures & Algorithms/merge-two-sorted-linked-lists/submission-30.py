# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        tail = merged_list
        while list1 != None and list2 != None:
            smaller_value = ListNode()
            if list1.val <= list2.val: 
                smaller_value = list1
                list1 = list1.next
            elif list1.val > list2.val:
                smaller_value = list2
                list2 = list2.next
            tail.next = smaller_value
            tail = tail.next
        tail.next = list1 if list1 else list2
        return merged_list.next