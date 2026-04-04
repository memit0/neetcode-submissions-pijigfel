class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        close_to_open = {')': '(', '}': '{', ']':'['}
        for char in s:
            if char in close_to_open.keys():
                if res and res[-1] == close_to_open[char]:
                    res.pop()
                else:
                    res.append(char)
            else:
                res.append(char)

        print(res)
        return len(res) == 0