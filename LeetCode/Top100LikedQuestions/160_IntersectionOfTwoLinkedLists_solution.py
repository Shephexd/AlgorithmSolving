# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        intersection_node = None
        head_a_dic = dict()
        while headA:
            head_a_dic[headA] = 1
            headA = headA.next
        
        while headB:
            if headB in head_a_dic:
                break
            headB = headB.next
        
        return headB
