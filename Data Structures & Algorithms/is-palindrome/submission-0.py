class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        new_s = ''.join(c for c in s if c.isalnum()).lower()
        l, r = 0, len(new_s) - 1
        
        # Even case 
        # Odd case
        while l < r:
            if new_s[l] == new_s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True