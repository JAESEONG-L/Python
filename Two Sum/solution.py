class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        (num1, num2)=self.find_solution(sorted(nums), target)

        answer=[]

        for idx in range(len(nums)):
            if nums[idx]==num1:
                answer.append(idx)

                break

        for idx in range(len(nums)):
            if nums[idx]==num2 and idx not in answer:
                answer.append(idx)

                return answer

        # No return because the solution (uniquely) exists.

    def find_solution(self, s_nums, target):
        for i in range(len(s_nums)-1):
            num1=s_nums[i]

            left=i+1
            right=len(s_nums)-1

            while left<=right:
                mid=(left+right)//2

                if s_nums[mid]==target-num1:
                    return (num1, target-num1)

                # s_nums[mid]!=target-num1
                if s_nums[mid]<target-num1:
                    left= mid+1
                else:
                    right= mid-1

        # No return because the solution (uniquely) exists.
