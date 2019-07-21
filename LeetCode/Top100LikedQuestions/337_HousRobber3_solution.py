# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        self.memo = dict()
        return self.helper(root)
    
    def helper(self, root):
        if root in self.memo:
            return self.memo[root]
        
        if root is None:
            return 0
        val = root.val
        
        if root.left:
            val += self.helper(root.left.left) + self.helper(root.left.right)
        
        if root.right:
            val += self.helper(root.right.left) + self.helper(root.right.right)
        
        child_val = self.helper(root.left) + self.helper(root.right)
        self.memo[root] = max(val, child_val)
        return self.memo[root]

