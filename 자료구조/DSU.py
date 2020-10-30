#disjoint set union

class DSU:
    def __init__(self):
        self.MAX=100001
        self.parent=[0 for _ in range(self.MAX)]
        for i in range(self.MAX):
            self.parent[i]=i            
        
    def find(self,idx):
        if idx==self.parent[idx]:
            return idx
        
        #return self.parent[idx] = find(self.parent[idx])
        self.parent[idx] = self.find(self.parent[idx])      #경로 압축
        return self.parent[idx]

    #idx1과 idx2번째를 합치는데 idx1의 루트(p1)를 찾고,idx2의 루트(p2)를 찾고, idx1의 루트가 idx2의 루트가 되도록 한다. 
    def merge(self,idx1,idx2):
        p1=self.find(idx1)
        p2=self.find(idx2)
        if p1==p2:
            return
        
        self.parent[p1]=p2  


d1=DSU()
d1.merge(1,2)
d1.merge(1,3)
d1.merge(1,10)

d1.merge(5,6)
d1.merge(5,7)

for i in range(1,10+1):
    print(d1.find(i),end=" ")
    


