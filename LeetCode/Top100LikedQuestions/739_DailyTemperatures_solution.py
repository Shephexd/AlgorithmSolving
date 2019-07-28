class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temp_stack = []
        res = [0 for i in T]
        
        for idx, t in enumerate(T):
            while temp_stack and temp_stack[-1][1] < t:
                day_after = idx - temp_stack[-1][0]
                res[temp_stack[-1][0]] = day_after
                temp_stack.pop()
            temp_stack.append((idx, t))
        return res


