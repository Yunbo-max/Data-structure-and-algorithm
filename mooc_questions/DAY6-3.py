def solveNQueen(N):
    pool =[0]*N

    def queen(cur=0):
        if cur == len(pool):
            return  [list(pool)]
        res =  []
        for col in range(len(pool)):
            pool[cur], flag = col, True
            for row in range(cur):
                if pool[row] == col or abs(col - pool[row]) == cur - row:
                    flag = False
                    break
            if flag:
                res += queen(cur + 1)
        return res

    return queen(0)


# test
print(solveNQueen(8))