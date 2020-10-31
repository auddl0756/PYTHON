visited=set()       #방문 여부 확인용
maps=[[0 for _ in range(500)] for _ in range(500)]

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def dfs(n,x,y):
    visited.add((x,y))

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        
        if (nx,ny) in visited:      #방문여부 검사
            continue
    
        dfs(n,nx,ny)


def solution(land, height):
    #global visited
    #global maps
    answer = 0

    n=len(land)
   
    for i in range(n):
        for j in range(n):
            maps[i][j]=land[i][j]
    
    groupcnt=0

    for i in range(n):
        for j in range(n):
            if (i,j) in visited:
                continue
            dfs(n,i,j)
            groupcnt+=1
    
    #print(groupcnt)

    




