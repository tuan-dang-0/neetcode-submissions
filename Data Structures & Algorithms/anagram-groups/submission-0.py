class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        key_to_groups = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            
            key = tuple(arr)

            key_to_groups[key].append(s)
        
        return list(key_to_groups.values())
