class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Keep count for each possible character for each word, if they match they are anagrams

        charCounts = defaultdict(int)

        for c in s:

            charCounts[c] += 1
        
        for c in t:
            charCounts[c] -= 1

        for cnt in charCounts.values():
            if cnt != 0:
                return False
        
        return True