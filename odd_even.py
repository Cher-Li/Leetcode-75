# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # I was thinking two pointers, one to deal with even, one to deal with odd? 
        # first deal with edge cases
        if not head or not head.next or not head.next.next:
            return head

        odd = head
        even = head.next
        even_head = even
        # while odd.next and even.next:
        while even and even.next: 
            odd.next = even.next # 1 -> 2 -> 3 becomes 1 -> 3 
            odd = odd.next # odd points to 3

            even.next = odd.next # now 2 -> 4 
            # and just continue
            # * also need to increment even
            even = even.next
        
        # then link the final two parts together
        odd.next = even_head

        return head