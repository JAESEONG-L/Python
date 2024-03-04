def solution(x, n):
    answer=[x]

    for idx in range(0, n-1):
        answer.append(answer[idx]+x)

    return answer
