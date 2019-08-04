class Solution:
    def decodeString(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        bracket_stack = []
        idx = 0
        while len(s) >= idx+1:
            c = s[idx]
            if c == '[':
                compressed_n = self.get_compressed_n(s, idx-1)
                bracket_stack.append([idx, compressed_n])
            elif c == ']':
                sidx, compressed_n = bracket_stack.pop()
                updated_idx = len(str(s[sidx+1:idx]) * int(compressed_n)) - len(s[sidx-len(compressed_n):idx+1])
                
                listed_s = list(s)
                listed_s[sidx-len(compressed_n):idx+1] = int(compressed_n) * listed_s[sidx+1:idx]
                
                s = ''.join(listed_s)
                
                idx = idx + updated_idx
            idx += 1
        return s
    
    def get_compressed_n(self, s, sidx):
        str_num = ''
        while s[sidx] >= '0' and s[sidx] <= '9':
            str_num = s[sidx] + str_num
            sidx -= 1
        return str_num
