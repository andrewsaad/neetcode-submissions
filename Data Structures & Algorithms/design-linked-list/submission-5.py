class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

class MyLinkedList:

    def __init__(self):
        self.head=ListNode(-1)
        self.tail=ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        get_int_LL = self.head.next
        loop_index = 0
        while get_int_LL and get_int_LL != self.tail:
            if index != loop_index:
                get_int_LL = get_int_LL.next
                loop_index +=1
            else:
                return get_int_LL.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        newHead=ListNode(-1)
        newHead.val = val
        newHead.next = self.head.next
        newHead.next.prev = newHead
        newHead.prev = self.head
        self.head.next = newHead

        

    def addAtTail(self, val: int) -> None:
        newTail = ListNode(val)
        TailPrev = self.tail.prev
        newTail.next = self.tail
        self.tail.prev=newTail
        TailPrev.next =newTail
        newTail.prev=TailPrev



    def addAtIndex(self, index: int, val: int) -> None:
        loop_head = self.head
        add_LL=ListNode(val)
        loop_index = 0
        while loop_head:
            loop_head_next = loop_head.next
            if not loop_head_next:
                break
            if loop_index == index:
                loop_head_next.prev = add_LL
                add_LL.next = loop_head_next
                loop_head.next = add_LL
                add_LL.prev = loop_head
                break
            loop_head = loop_head.next
            loop_index+=1
            

    def deleteAtIndex(self, index: int) -> None:
        loop_head = self.head.next
        loop_index = 0
        while loop_head:
            loop_head_next = loop_head.next
            loop_head_prev = loop_head.prev
            if loop_head == self.tail:
                break
            if loop_index == index:
                loop_head_next.prev = loop_head_prev
                loop_head_prev.next = loop_head_next
                break
            loop_head = loop_head.next
            loop_index+=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)