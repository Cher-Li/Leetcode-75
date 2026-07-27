# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # *
        if not head or not head.next:
            return None
        
        # two pointers vibe, reach the middle when the fast ptr reaches the end
        slow = fast = head
        # * 
        prev = None

        # * this while statement
        while fast and fast.next: # breaks when fast reaches end
            # * this way to update prev
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        # now slow should be at middle
        # singly linked so also need the prev of the middle node? 

        # could loop through until prev.next is slow, not sure if best method tho
        prev.next = slow.next
        # slow.next = null # don't need, also should be None
        return head