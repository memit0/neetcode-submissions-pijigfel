class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # (right - left + 1) - max_frequency > k, decrement the freq of s[left] and increment left

        freq = {}
        l, res = 0, 0
        for r in range(len(s)):
            # Build up the frequency list
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1

            max_freq = max(freq.values())
            window_size = r - l + 1
      
            # At any point if the window is invalid move left
            if window_size - max_freq > k:
                freq[s[l]] -= 1 # update the frequency
                l += 1
            else:
                res = max(res, window_size)

        return res

    

        