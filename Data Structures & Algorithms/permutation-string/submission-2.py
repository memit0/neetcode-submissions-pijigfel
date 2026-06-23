class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, windowSize = 0, len(s1)
        s1Freq, runningFreq = Counter(s1), Counter(s2[:windowSize]) 


        if runningFreq == s1Freq:
                return True 

        for r in range(windowSize, len(s2)):
            
            if s2[r] not in runningFreq:
                runningFreq[s2[r]] = 1
            else:
                runningFreq[s2[r]] += 1
            
            if runningFreq[s2[l]] == 1:
                del runningFreq[s2[l]]
            else:
                runningFreq[s2[l]] -= 1
            l += 1            

            # Check if we found the permutation substring
            if runningFreq == s1Freq:
                return True 

        return False

            
