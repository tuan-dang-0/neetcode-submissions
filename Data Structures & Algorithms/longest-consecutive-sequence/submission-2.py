class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) <= 1: return len(nums)

        nums = set(nums)

        ret = 0

        for num in nums:

            if (num - 1) in nums: continue

            curr = num
            cnt = 0
            while curr in nums:
                cnt += 1
                ret = max(cnt, ret)
                curr += 1
        
        return ret
