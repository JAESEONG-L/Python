def solution(sequence, k):
    answer = [-1, len(sequence)]

    record, sum = {0: -1}, 0

    for idx in range(len(sequence)):
        sum += sequence[idx]

        if sum - k in record and idx - record[sum - k] < answer[1] - answer[0] + 1:
            answer[0], answer[1] = record[sum - k] + 1, idx

        record[sum] = idx

    return answer
