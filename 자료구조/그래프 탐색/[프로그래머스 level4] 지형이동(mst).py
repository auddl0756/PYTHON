from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class DSU:
    def __init__(self):
        #self.MAX=100001
        self.MAX= 310*1000
        self.parent=[0 for _ in range(self.MAX)]
        for i in range(self.MAX):
            self.parent[i]=i          
        
    def find(self,idx):
        if idx==self.parent[idx]:
            return idx
        
        #return self.parent[idx] = find(self.parent[idx])
        self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]

    def merge(self,idx1,idx2):
        p1=self.find(idx1)
        p2=self.find(idx2)
        if p1==p2:
            return
        
        self.parent[p1]=p2



visited=set()
maps= [[[0,0,0,0] for _ in range(350)] for _ in range(350)]     #x,y,h,group
dx=[0,-1,0,1]
dy=[-1,0,1,0]


# 런타임 에러 발생함. ==> sys.setrecursionlimit(10**6)하면 해결됨.
# def dfs(n,x,y,group,limit):
#     #global visited
#     #global maps

#     visited.add((x,y))
#     maps[x][y][3]=group

#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
        
#         if nx<0 or nx>=n or ny<0 or ny>=n:
#             continue
        
#         if (nx,ny) in visited:
#             continue

#         if abs(maps[x][y][2]-maps[nx][ny][2]) >limit:
#             continue

        
#         dfs(n,nx,ny,group,limit)


def bfs(n,x0,y0,group,limit):
    q=deque()
    q.append((x0,y0))
    visited.add((x0,y0))
    maps[x0][y0][3]=group
    
    while len(q):
        here=q.popleft()
        x,y=here[0],here[1]

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if (nx,ny) in visited or abs(maps[x][y][2]-maps[nx][ny][2])>limit:
                continue
            
            maps[nx][ny][3]=group
            q.append((nx,ny))
            visited.add((nx,ny))



def solution(land, height):
    #global visited
    #global maps
    answer = 0

    n=len(land)
    groupcnt=0
    for i in range(n):
        for j in range(n):
            maps[i][j][0]=i
            maps[i][j][1]=j
            maps[i][j][2]=land[i][j]
    
    
    for i in range(n):
        for j in range(n):
            if (i,j) in visited:
                continue
            #dfs(n,i,j,groupcnt,height)
            bfs(n,i,j,groupcnt,height)
            groupcnt+=1
    
    #print(groupcnt)
  
    # for i in range(n):
    #     for j in range(n):
    #         print(maps[i][j][3],end=" ")
    #     print()
    # print()

############################################################
#below MST 
    
    edges=[]        #cost,from,to
    d=DSU()         #use disjoint set to check if node is connected

    for x in range(n):
        for y in range(n):
            node1=n*x+y             #make 2nd order degree to 1st order hash value for represent node 
            #d.parent[node1]=maps[x][y][3]
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
        
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                
                node2=n*nx+ny
                if maps[x][y][3]==maps[nx][ny][3]:
                    d.merge(node1,node2)

                edges.append([abs(maps[x][y][2]-maps[nx][ny][2]),node1,node2])  

    
    edges.sort()    #sort by cost
    
    # for i in range(n*n):
    #     print(d.find(i),end=" ")
    #     # print(d.parent[i],end=" ")
    # print()
    
    # print(edges)
    
    

    # ***iterate for all edges ('E' times)==> except 'continue', this loop makes connection of n-1 edges ***
    for i in range(len(edges)):
        cost,n1,n2=edges[i][0],edges[i][1],edges[i][2]
        x1=n1//n
        y1=n1%n
        x2=n2//n
        y2=n2%n
        if maps[x1][y1][3]==maps[x2][y2][3]:
            continue
        
        p1=d.find(n1)
        p2=d.find(n2)

        if p1==p2:
            continue

        d.merge(n1,n2)
        answer+=cost
        #print(n1,n2,cost)
        # for i in range(n*n):
        #     print(d.find(i),end=" ")
        # print()

    # for i in range(n*n):
    #     print(d.find(i),end=" ")
    # print()

    return answer


#########################test##################################

#land=[[1,2],[100,101]]
#height=2

# land=[[1,4,8,10],[5,5,5,5],[10,10,10,10],[10,10,10,20]]
# height=3

# land=[[10,11,10,11],[2,21,20,10],[1,20,21,11],[2,1,2,1]]
# height=1

# land=[[2,3],[10,1]]
# height=1

# ans=solution(land,height)
# print(ans)