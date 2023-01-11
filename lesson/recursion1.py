class maze:
    def __init__(self,mazefilename):
        rowsinmaze=0
        colomnsinmaze=0
        self.mazelist=[]
        mazefile=open(mazefilename,'r')
        rowsinmaze=0
        for line in mazefile:
            rowlist=[]
            col=0
            for ch in line[:-1]:
                rowlist.append(ch)
                if ch=='S':
                    self.startrow=rowsinmaze
                    self.starcol=col
                col =col +1
            rowsinmaze=rowsinmaze+1
            self.mazelist.append(rowlist)
            columnsinmaze=len(rowlist)


    def drawMaze(self):
        t = maze('long.txt')
        self.t.speed(50)  # 绘图速度
        for y in range(self.rowsInMaze):  # 按单元格依次循环迷宫
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:  # 如果迷宫列表的该位置为障碍物，则画方块
                    self.drawCenteredBox(x + self.xTranslate, -y + self.yTranslate, 'orange')
    print(t.mazelist)






def searchfrom(maze,startrow,startcolumn):
    maze.udateposition(startrow,startcolumn)
    if maze[startrow][startcolumn]==OBSTACLE:
        return False
    if maze[startrow][startcolumn]== TRIED or  maze[startrow][startcolumn]==DEAD_END:

     if maze.isExit(startrow,startcolumn):
        maze.updateposition(startrow,startcolumn,PART_OF_PATH)
        return True
    maze.updateposition(startrow,startcolumn,TRIED)

    found=searchfrom(maze,startrow-1,startcolumn) or \
          searchfrom(maze,startrow+1,startcolumn) or \
          searchfrom(maze, startrow , startcolumn-1) or \
          searchfrom(maze, startrow, startcolumn+1)

    if found:
        maze.updateposition(startrow,startcolumn,PART_OF_PATH)
    else:
        maze.updateposition(startrow,startcolumn,DEAD_END)
    return found




if __name__ == '__main__':
	PART_OF_PATH = 'O'			#部分路径
	TRIED = '.'					#尝试
	OBSTACLE = '+'				#障碍
	DEAD_END = '-'				#死胡同
	myMaze = maze('123.txt')	#实例化迷宫类，maze文件是使用“+”字符作为墙壁围出空心正方形空间，并用字母“S”来表示起始位置的迷宫文本文件。
	myMaze.drawMaze()			#在屏幕上绘制迷宫。
	searchfrom(myMaze, myMaze.startRow, myMaze.startCol)	#探索迷宫

