class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for r in range(len(board[0])):
            for c in range(len(board)):

                val = board[r][c]

                if val == '.': continue

                curr_box = (r // 3, c // 3)

                if val in rows[r] or val in cols[c] or val in box[curr_box]: 
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                box[curr_box].add(val)
        
        return True
