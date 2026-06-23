class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l, res = 0, float('inf')
        ans = ""
        resultFreq = Counter(t)
        need, have = len(resultFreq), 0
        runningFreq = {}
        for r in range(len(s)):
            runningFreq[s[r]] = runningFreq.get(s[r], 0) + 1

            # We increment have when the value of the same key is equal
            if s[r] in resultFreq and runningFreq[s[r]] == resultFreq[s[r]]:
                have += 1

            # Check that it's a valid window and start decreasing
            while have == need:
                if (r - l + 1) < res:
                    res = r - l + 1
                    ans = s[l:r+1]

                if s[l] in resultFreq and runningFreq[s[l]] == resultFreq[s[l]]:
                    have -= 1

                runningFreq[s[l]] -= 1
                
                l += 1
                

        return ans