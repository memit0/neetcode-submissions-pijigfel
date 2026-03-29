from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #a dictionary with default values as list for the undefined keys
        my_dict = defaultdict(list)
        result = []

        #loop the strings sort each of them and store them as a tuple
        for s in strs: 
            sorted_s = tuple(sorted(s))
            my_dict[sorted_s].append(s)        
        
        for value in my_dict.values():
            result.append(value)
        return result 