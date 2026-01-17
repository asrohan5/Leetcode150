class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        l = d
        right = head
        while n>0 and right:
            right = right.next
            n-=1
            
        while right:
            l = l.next
            right = right.next
        
        l.next = l.next.next
        return d.next
        
