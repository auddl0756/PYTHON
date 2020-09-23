import requests
import json

#웹브라우져에서 티스토리를 접속한 것과 똑같은 이야기이다. 
url='http://www.tistory.com'
response=requests.get(url)      # www.tistory.com 이라는 주소로 GET 요청(request)를 보냈고 서버에서는 그 요청을 받아 뭔가를 처리한 후 
# print(response.status_code)   # 요청자인 나에게 응답(response)를 줬다. 우선 그 응답은 200 상태코드와 함께 왔다.
                                #  이는 티스토리 서버에서 잘 처리되어서 정상적인 응답을 보내줬다는 OK 싸인을 의미한다. 
# print(response.text)          # 그리고 응답의 내용은? HTML 코드.

#출처: https://dgkim5360.tistory.com/entry/python-requests


###########################################################################################################
#1. GET 요청할 때 parameter 전달법
params={'query':'아이유'}
#내가 준 URL과 파라미터를 requests 모듈이 엮어서 적절한 새로운 요청을 만든 것
res=requests.get('http://search.naver.com/search.naver/',params=params)       

#print(res.url)
#print(res.text)
#print(res.content)


###########################################################################################################
#2. POST 요청할 때 data 전달법
data={'param1':'value1','param2':'value2'}
res2=requests.post(url,data=data)


#조금 더 복잡한 구조로 POST 요청을 해야 할 때가 있다. 이럴 때는 위의 방법처럼 순진하게 주면 안된다. 
#우리가 인지하고 있는 그 딕셔너리의 구조를 유지하면서 문자열로 바꿔서 전달해줘야 하는데,
# python에서 이 노동을 해주는 친구가 json 모듈이다.

headers={'Content-Type':'application/json; charset=utf-8'}
res=requests.get(url,headers=headers)
# print(res.headers)
# print(res.history)


###########################################################################################################
url="http://www.naver.com"
res3=requests.get(url)
print("******************enter naver******************")
print(res3.text)








