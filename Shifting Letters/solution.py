class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        accum_shifts=[0] * len(shifts)

        accum_shifts[len(shifts)-1]= shifts[len(shifts)-1]

        for i in range(len(shifts)-2, -1, -1):
            accum_shifts[i]= accum_shifts[i+1]+shifts[i]

        answer=chr((ord(s[0])-97+accum_shifts[0])%26+97)

        for i in range(1, len(s)):
            answer += chr((ord(s[i])-97+accum_shifts[i])%26+97)

        return answer
