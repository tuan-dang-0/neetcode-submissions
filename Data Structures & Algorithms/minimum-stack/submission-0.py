class MinStack:

    def __init__(self):

        self.stk = []
        

    def push(self, val: int) -> None:

        currMin = val
        if self.stk:
            currMin = min(self.stk[-1][1], currMin)

        self.stk.append([val, currMin])
        

    def pop(self) -> None:
        self.stk.pop()
        

    def top(self) -> int:
        return self.stk[-1][0]
        

    def getMin(self) -> int:
        return self.stk[-1][1]
        
