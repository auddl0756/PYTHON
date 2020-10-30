from collections import deque
import sys
input = sys.stdin.readline

dx=[0,-1,0,1]
dy=[-1,0,1,0]

#bfs in grid

def bfs(x0,y0):
    visited=set()
    q=deque()
    q.append((x0,y0))
    visited.add((x0,y0))        

    while len(q):
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i],ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if (nx,ny) in visited:
                continue

            q.append((nx,ny))
            visited.add((nx,ny))        #방문체크 빼먹으면 무한루프.


