class Solution:
    def isValid(self, s: str) -> bool:
        
        mapper = {')' : '(', '}' : '{', ']' : '['}

        stk = []

        for c in s:

            if c in mapper:

                if not stk: return False

                if stk[-1] != mapper[c]:
                    return False
                
                stk.pop()
            
            else:

                stk.append(c)
        
        return not stk