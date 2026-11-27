class Solution:

    def encode(self, strs: List[str]) -> str:

        arr = []
        for s in strs:
            arr.append(str(len(s)))
            arr.append("#")
            arr.append(s)
        
        return "".join(arr)


    def decode(self, s: str) -> List[str]:
        ret = []

        while(s):
            delim = s.find('#')
            length = int(s[:delim])
            word = s[delim + 1 : delim + 1 + length]

            ret.append(word)
            s = s[delim + 1 + length:]
        
        return ret



