class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer=""

        for i in range(0, len(s)-1):
            max_l=-1

            for l in range(2, min(i+1, len(s)-i-1)*2+2, 2):
                if s[i-l//2+1]!=s[i+l//2]:
                    break

                max_l= l

            if max_l>len(answer):
                answer= s[i-max_l//2+1:i+max_l//2+1]

        for i in range(0, len(s)):
            max_l=1 # One letter is a palindrome.

            for d in range(1, min(i, len(s)-i-1)+1):
                if s[i-d]!=s[i+d]:
                    break

                max_l= 1+2*d

            if max_l>len(answer):
                answer= s[i-(max_l-1)//2:i+(max_l-1)//2+1]

        return answer
