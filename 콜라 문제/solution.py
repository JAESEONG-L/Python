def solution(a, b, n):
    answer=0

    while True:
        answer += b*(n//a)

        n= n%a+b*(n//a)
        if n<a:
            break

    return answer
