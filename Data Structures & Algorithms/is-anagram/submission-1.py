class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []
        for char in s: 
            list1.append(char)
        for char in t:
            list2.append(char)
        list1.sort()
        list2.sort()
        if list1 == list2:
            return True
        else:
            return False
            
        