class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        found = set()

        ret = 0

        for num in nums:
            found.add(num)
        
        for num in nums:
            if num + 1 in found:
                continue
                
            length = 1
            while num - 1 in found:
                length += 1
                num -= 1
            
            ret = max(ret, length)
        
        return ret
        