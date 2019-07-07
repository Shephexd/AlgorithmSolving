class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = self.helper(n, n)
        return res
    
    def helper(self, lp, rp, res=''):
        if lp < 0 or rp < 0:
            return []
        if lp == 0 and rp==0:
            return [res]
        
        result = []
        if lp < rp:
            result += self.helper(lp, rp-1, res=res+')')
        result += self.helper(lp-1, rp, res+'(')
        return result

