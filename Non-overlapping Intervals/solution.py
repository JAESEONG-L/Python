class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        dp=list()

        intervals.sort(key=lambda interval : interval[1])

        for _ in range(100001):
            dp.append(0)

        dp[intervals[0][1]+50000]= 1

        temp=intervals[0][1]+50000

        for i in range(1, len(intervals)):
            if dp[temp-1]>dp[temp]:
                dp[temp]= dp[temp-1]

            for j in range(temp+1, intervals[i][1]+50000):
                dp[j]= dp[j-1]

            if dp[intervals[i][1]+50000]<dp[intervals[i][0]+50000]+1:
                dp[intervals[i][1]+50000]= dp[intervals[i][0]+50000]+1

            temp= intervals[i][1]+50000

        if dp[temp-1]>dp[temp]:
            dp[temp]= dp[temp-1]

        for i in range(temp+1, 100001):
            dp[i]= dp[i-1]

        return len(intervals)-dp[100000]
