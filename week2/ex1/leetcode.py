class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        """
        ## Brute force O(n^3)
        left = 0
        right = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[j] not in s[i:j]:
                    if (j-i+1) > (right-left+1):
                        left = i
                        right = j
                else:
                    break
                    
        print(s[left:right+1])
        return right-left+1
        """
        
        ## Approach2 O(n^2)
        i, j = 0, 0
        length = j-i+1
        left, right = i, j
        
        while j < len(s):
            if s[j] not in s[i:j]:
                 if (j-i+1) > (right-left+1):
                        left = i
                        right = j
            else:
                while s[i] != s[j]: 
                    i+=1
                i+=1
                
            j+=1
            
        print(s[left:right+1])
        return right-left+1

if __name__ == '__main__':
    sol = Solution()
    strr = "abcabcbb"
    print('string: ', strr )
    print('Length of longest substring:', sol.lengthOfLongestSubstring(strr))
        
    
   
        
            
                    
                
            
            
        
                    