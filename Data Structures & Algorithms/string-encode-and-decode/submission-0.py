class Solution:

    def encode(self, strs: List[str]) -> str:

        # Encode number of characters with some delimiter before
        # each word

        arr = []
        for s in strs:
            cnt = 0

            for c in s:
                cnt += 1
            
            arr.append(str(cnt) + '#')
            arr.append(s)
    
        return "".join(arr)

    def decode(self, s: str) -> List[str]:

        output = []

        while len(s) > 0:

            delim = s.find('#')

            if delim == -1: break

            length = int(s[0:delim])

            word = s[delim+1:delim+length + 1]
            output.append(word)

            s = s[delim+length + 1:]
        
        return output


