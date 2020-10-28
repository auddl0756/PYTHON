graph=[[1e9 for _ in range(60)] for _ in range(60)]

def floyd(N):
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if k==i or k==j or i==j:
                    continue
                
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
                graph[j][i]=min(graph[j][i],graph[j][k]+graph[k][i])

                
def solution(N, road, K):
    answer = 1
    
    for i in range(len(road)):
        u,v,cost=road[i][0],road[i][1],road[i][2]
        graph[u][v]=min(graph[u][v],cost)
        graph[v][u]=min(graph[v][u],cost)
    
    floyd(N)
    
    for i in range(1,N+1):
        #print(graph[1][i],end=" ")
        if graph[1][i]<=K:
            answer+=1
        
        
    return answer