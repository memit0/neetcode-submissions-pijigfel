class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary key: sorted(str) val: array of strs
        sorted_to_str = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in sorted_to_str:
                sorted_to_str[sorted_s].append(s)
            else:
                sorted_to_str[sorted_s] = [s]

        res = []
        for key, val in sorted_to_str.items():
            res.append(val)
        return res
