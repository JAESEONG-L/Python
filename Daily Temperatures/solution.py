class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        MAXOF_N=100000

        r_check=list()

        for _ in range(30, 101):
            r_check.append(0)

        answer=[0] * len(temperatures)

        for idx in range(len(temperatures)-1, -1, -1):
            min_i=MAXOF_N

            for t in range(temperatures[idx]+1, 101):
                if r_check[t-30] and r_check[t-30]<min_i:
                    min_i= r_check[t-30]

            if min_i<MAXOF_N:
                answer[idx]= min_i-idx

            r_check[temperatures[idx]-30]= idx

        return answer
