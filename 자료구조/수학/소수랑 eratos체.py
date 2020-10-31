#MAX=100000
MAX=3500
primes = [False for _ in range(MAX)]
primenums=[]
checked = [False for _ in range(MAX)]

def eratos():
    for i in range(2,MAX):
        if checked[i]:
            continue

        primes[i]=True
        primenums.append(i)

        for j in range(i,MAX,i):
            checked[j]=True



def solution(nums):
    answer = 0

    eratos()

    n= len(nums)

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                s=nums[i]+nums[j]+nums[k]
                if s in primenums:
                    answer+=1

    return answer