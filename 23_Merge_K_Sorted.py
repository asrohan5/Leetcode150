import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        min_heap = []

        for i, node in enumerate(lists):
            if node:

                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, i, smallest_node = heapq.heappop(min_heap) 
            current.next = smallest_node 
            current = current.next

            
            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, i, smallest_node.next))

        return dummy.next 
