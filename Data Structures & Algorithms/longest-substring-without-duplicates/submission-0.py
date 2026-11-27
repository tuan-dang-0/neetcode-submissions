class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        # Want counts of characters in current window
        counts = defaultdict(int)
        l = r = 0
        ret = 0
        # While right pointer in range of string
        while(r < len(s)):
            print(s[l], s[r])
            counts[s[r]] += 1
            while(counts[s[r]] > 1):
                counts[s[l]] -= 1
                l += 1
            ret = max(ret, r - l + 1)
            r += 1
        
        return ret