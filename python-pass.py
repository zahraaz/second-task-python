

class Solution:

    @staticmethod
    def longest_palindromic(self,s: str) -> str:
        def helper (l,r):
            while (l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        result=""
        reslen=0

        for i in range(len(s)):
            test=helper(i,i)
            if len(test)>len(result):result=test
            test=helper(i,i+1)
            if len(test)>len(result):result=test
        
        return result

#first test
o=Solution()
print('the result is '+o.longest_palindromic(o,'babad'))

p=Solution()
print('\n the result is '+p.longest_palindromic(p,'cbbd'))