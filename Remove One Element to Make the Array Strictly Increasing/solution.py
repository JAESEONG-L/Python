class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        abnorm_idx=None
        abnorm_count=0

        for idx in range(len(nums)-1):
            if nums[idx]>=nums[idx+1]:
                abnorm_idx= idx

                abnorm_count += 1

        if abnorm_count==0:
            return True
        elif abnorm_count==1:
            # After removing the left element.
            if abnorm_idx==0 or nums[abnorm_idx-1]<nums[abnorm_idx+1]:
                return True

            # After removing the right element.
            if abnorm_idx==len(nums)-2 or nums[abnorm_idx]<nums[abnorm_idx+2]:
                return True

        return False
