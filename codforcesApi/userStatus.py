# requests module install : https://blog.daum.net/dhlee-0915/34
import requests

# r=requests.get('https://api.github.com/events') # r=Response object
# print(r.status_code)
# print(r.text)

# r = requests.post('https://httpbin.org/post', data={'key': 'value'})
# print(r)

# r = requests.delete('https://httpbin.org/delete')
# print(r)


# host='https://search.naver.com'
# path='/search.naver'
# URL=host+path
# payload = {'query':'api'}
# r = requests.get(URL, params=payload)
#
# print(r.url)
# print(r.status_code)
# print(r.text)



# With Codeforces API you can get access to some of our data in machine-readable JSON format.
# To access the data you just send a HTTP-request to address https://codeforces.com/api/{methodName}
# only public data will be accessable via API

URL='https://codeforces.com/api/'
# method='contest.standings/'
# URI=URL+method
# payload={'contestId':'1476','from':1,'count':100,'handles':100}
# r=requests.get(URI,payload)
# print(r.status_code)
#
# response=r.json()
# print(response)
# problems = response['result']['problems']
# #print(problems)
# rating=[0 for _ in range(10)]
# for p in problems:
#     print(p['rating'],end=" ")


URL='https://codeforces.com/api/'
method='user.status'
payload={'handle':'flip-flop'}
URI=URL+method
r=requests.get(URI,payload)
print(r.status_code)
response=r.json()

res=response['result']
solved=[]
print(res[0])
for r in res:
    if r['verdict']=='OK':
        solved.append([r['problem']['index'],r['problem']['name'],r['problem']['rating'],r['programmingLanguage']])


def rating(s):
    return s[2]

solved.sort(key=rating)
solved_per_rating={}
solved_per_language={}
for s in solved:
    print(s)
    if solved_per_rating.get(s[2]) is None:
        solved_per_rating[s[2]]=1
    else:
        solved_per_rating[s[2]]+=1

    if solved_per_language.get(s[3]) is None:
        solved_per_language[s[3]]=1
    else:
        solved_per_language[s[3]]+=1

print(solved_per_rating)
print(solved_per_language)