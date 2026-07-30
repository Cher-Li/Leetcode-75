# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        # just increment through, keep doing second.next = first? 
        # first = head
        # second = head.next
        # * this vibe, but also handling first vs last nodes
        first = None # essentially prev
        second = head # essentially curr

        # while second and second.next: # <- ends loop too early
        while second: 
            third = second.next
            second.next = first

            # then incrementing
            first = second
            second = third
        
        # return second # <- not new head
        # when "curr" becomes none, prev is actually just before that aka reversed list head
        return first