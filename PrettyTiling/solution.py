# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

pretty_rotation = [1, 2, 1, 0]

def solution(A):
    def rotate(s, upper_idx):
        return s[upper_idx:] + s[:upper_idx]

    def rotation_count(s):
        count = 0

        for idx in range(1, len(A)):
            where = A[idx].index(s[1])

            count += pretty_rotation[where]
            s = rotate(A[idx], (where + 1) % 4)

        return count

    return min(
        rotation_count(A[0]),
        1 + rotation_count(rotate(A[0], 1)),
        2 + rotation_count(rotate(A[0], 2)),
        1 + rotation_count(rotate(A[0], 3))
    )
