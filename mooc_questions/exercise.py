class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        q=0

        i=0
        j=0
        if i-K<0:
            x1=0
        else:
            x1=i-K
        if j-K<0:
            x2=0
        else:
            x2=j-K

        if i+K>n:
            y1=n
        else:
            y1=i+K
        if j+K>m:
            y2=m
        else:
            y2=i+K
        answer = [[0] * n for _ in range(m)]
        for t in range(0,m*n)
            for i in range(x1,y1):
                for j in range(x2,y2):
                    q+=mat[i][j]
            answer[t%m][t-t%m*n]=q
        return answer
