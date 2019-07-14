# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        history = []
        
        while head is not None:
            history.append(head.val)
            head = head.next
        
        flag = True
        for rv, v in zip(history[::-1], history):
            if rv != v:
                flag = False
                break
                
        return flag
