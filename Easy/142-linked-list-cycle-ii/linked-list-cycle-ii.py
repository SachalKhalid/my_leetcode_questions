# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        fast = head
        slow = head
        entery = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                while(entery != slow):
                    slow = slow.next
                    entery = entery.next
                return slow
        return None
            