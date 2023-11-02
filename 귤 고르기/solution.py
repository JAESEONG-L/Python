def solution(k, tangerine):
    tangerine.sort()


    counts=[]

    startIndex=0

    for i in range(1, len(tangerine)):
        if tangerine[i-1]!=tangerine[i]:
            counts.append(i-startIndex)

            startIndex= i

    counts.append(len(tangerine)-startIndex)

    counts.sort()

    counts.reverse()

    sum=0

    i=0

    while sum<k:
        sum += counts[i]

        i += 1

    return i
