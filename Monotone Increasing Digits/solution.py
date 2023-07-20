class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        answer=0
        min_d=1
        p_value=10**9

        while p_value:
            for d in range(9, min_d-1, -1):
                if answer+d*(p_value*10-1)/9<=n:
                    answer += d*p_value

                    min_d= d

                    break

            p_value //= 10

        return answer
