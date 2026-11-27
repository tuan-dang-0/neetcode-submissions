class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mapper = defaultdict(int)

        ret = 0

        l = 0

        for r in range(len(s)):

            mapper[s[r]] += 1

            while mapper[s[r]] > 1:
                mapper[s[l]] -= 1
                l += 1
            
            ret = max(ret, r - l + 1)
        
        return ret


