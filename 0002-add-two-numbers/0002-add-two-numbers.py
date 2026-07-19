class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify the list construction
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Iterate while there are nodes in either list or a remaining carry
        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Add the digit (total % 10) to the result list
            current.next = ListNode(total % 10)
            
            # Advance pointers
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy_head.next