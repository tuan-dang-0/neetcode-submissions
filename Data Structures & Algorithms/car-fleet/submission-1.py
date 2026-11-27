class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        arr = list(zip(position, speed))
        arr.sort()

        stk = [arr[-1]]

        for i in range(len(arr) - 2, -1, -1):

            pos1, spd1 = arr[i]
            pos2, spd2 = stk[-1]

            if (target - pos1) / spd1 <= (target - pos2) / spd2:
                continue
            else:
                stk.append(arr[i])
            
        
        return len(stk)
            
