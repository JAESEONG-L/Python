class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        s_mat=[mat[0] + [0]]

        for i in range(1, len(mat)):
            s_mat.append(mat[i] + [i])

            for j in range(i-1, -1, -1):
                if self.row_compare(s_mat, j, j+1):
                    break

                (s_mat[j], s_mat[j+1]) = (s_mat[j+1], s_mat[j])

        answer=[]

        for idx in range(k):
            answer.append(s_mat[idx][len(mat[0])])

        return answer

    def row_compare(self, s_mat, a, b):
        temp=len(s_mat[0])-1

        for i in range(len(s_mat[0])-1):
            if s_mat[a][i]==0 or s_mat[b][i]==0:
                temp= i

                break

        if temp==len(s_mat[0])-1 or (s_mat[a][temp]==0 and s_mat[b][temp]==0):
            return a<=b

        return s_mat[a][temp]<=s_mat[b][temp]
