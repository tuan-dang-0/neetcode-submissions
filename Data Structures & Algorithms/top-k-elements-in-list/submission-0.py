class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for i in range(len(nums) + 1)]

        cnts = defaultdict(int)

        for num in nums:
            cnts[num] += 1
        
        for num in cnts:
            buckets[cnts[num]].append(num)
        
        ret = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if k == 0:
                    return ret
                
                ret.append(num)
                k -= 1
        
        return ret
            
