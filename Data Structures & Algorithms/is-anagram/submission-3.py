class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqA, freqB = collections.Counter(s), collections.Counter(t)

        return freqA == freqB