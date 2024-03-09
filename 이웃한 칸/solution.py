def solution(board, h, w):
    size = len(board)

    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]

    count = 0

    for d in range(4):
        nh, nw = h + dh[d], w + dw[d]
        if 0 <= nh and nh <= size - 1 and 0 <= nw and nw <= size - 1 and board[nh][nw] == board[h][w]:
            count += 1

    return count
