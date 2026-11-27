class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def compute(c, op1, op2):

            op1, op2 = int(op1), int(op2)

            if c == '+':
                return op1 + op2
            elif c == '-':
                return op1 - op2
            elif c == '*':
                return op1 * op2
            elif c == '/':
                return int(op1 / op2)


        ops = set(['+', '-', '*', '/'])

        stk = []

        for c in tokens:
            if c in ops:
                op2 = stk.pop()
                op1 = stk.pop()

                ret = compute(c, op1, op2)
                stk.append(str(ret))
            else:
                stk.append(c)
        
        return int(stk[-1])

