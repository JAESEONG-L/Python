def solution(x, y, n):
    dp=[-1] * (y+1)

    dp[x]= 0

    for num in range(x+1, y+1):
        if dp[num-n]!=-1:
            dp[num]= dp[num-n]+1

        if num%2==0 and dp[num//2]!=-1:
            dp[num]= positive_min(dp[num], dp[num//2]+1)

        if num%3==0 and dp[num//3]!=-1:
            dp[num]= positive_min(dp[num], dp[num//3]+1)

    return dp[y]

def positive_min(m, n):
    if m<0 and n<0:
        return -1

    # not (m<0 and n<0)
    # Ignore the negative value.
    if m<0:
        return n

    # Ignore the negative value.
    if n<0:
        return m

    return min(m, n)
