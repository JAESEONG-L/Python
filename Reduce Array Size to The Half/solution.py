class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        count=[0] * 100000

        for num in arr:
            count[num-1] += 1

        count.sort()

        # Accumulating the sum of the removed occurrences from the highest.
        sum=0

        for answer in range(1, 50001):
            sum += count[100000-answer]

            if len(arr)//2<=sum:
                return answer
