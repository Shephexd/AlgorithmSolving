class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        ans = dict()
        for s in strs:
            key = tuple(sorted(s))
            if key not in ans:
                ans[key] = list()
            ans[key].append(s)
        return list(ans.values())


