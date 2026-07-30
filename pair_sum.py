# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        
        # I think the most straightforward is to make a separate LL but reversed, and then just sum i of each until halfway point, not sure if most efficient
        # also an emphasis on even length so no edge cases with odd length
        # like it's not like it's sum of first then mid then increment both, it's specifically far ends then continue pairing

        # new_head = ListNode(head.val)
        # ptr = head.next
        # placeholder = new_head
        # while ptr:
        #     placeholder.next = ListNode(ptr.val)
        #     placeholder = placeholder.next
        # reversed_list = self.reverseList(new_head)

        # ptr1 = head
        # ptr2 = reversed_list
        # max_sum = 0
        # while ptr1: 
        #     max_sum = max(max_sum, ptr1.val + ptr2.val)
        #     ptr1 = ptr1.next
        #     ptr2 = ptr2.next
        
        # return max_sum

        # * can still go w/ the idea of, one ptr at start, one ptr at mid, and increment both, if the second half is reversed
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # want to reverse the list starting from slow
        new_head = self.reverseList(slow)

        max_sum = 0
        ptr1 = head
        ptr2 = new_head
        while ptr1 and ptr2: 
            max_sum = max(max_sum, ptr1.val + ptr2.val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return max_sum

    def reverseList(self, head): # from prev prob
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        first = None
        second = head

        while second: 
            third = second.next
            second.next = first
            first = second
            second = third
        
        return first