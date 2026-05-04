class Solution:

    def encode(self, strs: List[str]) -> str:
        # For each word include a delimeter and number
        st = ""
        for s in strs:
            st += f'{len(s)}#{s}'
        return st

    def decode(self, s: str) -> List[str]:
        # Decode based on that integer delimeter combination
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i+length])
            i += length
        return res
        
