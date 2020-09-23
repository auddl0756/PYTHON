# c++의 map에 해당하는 dictionary 사용법

#선언
#x={}
x={'a':97,'b':98,'c':99,'d':100};

#추가
x['e']=100

#값 변경
x['a']=1

#list -> dict 변환
x2=[['A',1],['B',2],['C',3]]
y=dict(x2)
print('y= ',y)


#출력,순서는 정해져 있지 않음.
for k in x.keys():
    print(k,end=' ')
print()

for v in x.values():
    print(v,end=' ')
print()

for k,v in x.items():
    print(k,v,end=' ')
print()


#검색 
print('a' in x)