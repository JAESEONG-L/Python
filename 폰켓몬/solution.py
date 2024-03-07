def solution(nums):
    nums_len=len(nums)
    nums.sort()

    num_count=1

    for idx in range(1, nums_len):
        if nums[idx]!=nums[idx-1]:
            num_count += 1

    return min(nums_len//2, num_count)
