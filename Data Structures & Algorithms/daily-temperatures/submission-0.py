class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stk = []

        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while stk and stk[-1][0] < temp:

                pastTemp, prevInd = stk.pop()
                
                result[prevInd] = i - prevInd
            
            stk.append((temp, i))
        
        return result