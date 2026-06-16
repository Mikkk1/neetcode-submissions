class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        have, need_count = 0, len(need)
        resL, resR = 0, 0
        resLen = float('inf')
        L = 0
        
        for R in range(len(s)):
            c = s[R]
            window[c] = window.get(c,0) + 1
            
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == need_count:
                if (R - L + 1) < resLen:
                    resLen = min(resLen, (R - L + 1))
                    resL, resR = L, R
                
                window[s[L]] -= 1
                if s[L] in need and window[s[L]] < need[s[L]]:
                    have -= 1
                L += 1
        
        return s[resL:resR+1] if resLen != float('inf') else ""