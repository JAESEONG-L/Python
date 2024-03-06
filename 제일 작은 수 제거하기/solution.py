def solution(arr):
    min_idx=0
    for idx in range(1, len(arr)):
        if arr[idx]<arr[min_idx]:
            min_idx= idx
    arr.pop(min_idx)
    return arr if len(arr) else [-1]
