class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        val_to_ind = {}

        for i, num in enumerate(nums):

            complement = target - num
            if complement in val_to_ind:
                return [val_to_ind[complement], i]

            val_to_ind[num] = i
        
        return None