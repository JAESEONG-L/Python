class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        m=len(board)
        n=len(board[0])

        # Starting from the right direction.
        dx=[0, 1, 1, 1, 0, -1, -1, -1]
        dy=[1, 1, 0, -1, -1, -1, 0, 1]

        # From a live cell perspective.
        for i in range(m):
            for j in range(n):
                if board[i][j]>=1:
                    for d in range(8):
                        (di, dj) = (i+dx[d], j+dy[d])

                        if 0<=di and di<=m-1 and 0<=dj and dj<=n-1:
                            board[di][dj] += 1 if board[di][dj]>=1 else -1

        for i in range(m):
            for j in range(n):
                board[i][j]= 1 if (board[i][j]==3 or board[i][j]==4 or board[i][j]==-3) else 0
