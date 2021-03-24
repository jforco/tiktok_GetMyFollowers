import json
import requests

def ordenar(e):
    return e["stats"]["followerCount"]

lista = []
u1 = 'https://m.tiktok.com/api/user/list/?count=199&maxCursor='
u2 = '&minCursor='
max = 0
min = 0
# paste value of sessionid_ss cookie 
# (if you are here, i think you know how to get that value from your browser when you are in your tiktok account)
cookie_session= "0f81329afa648386452e6c9f11d8622d"
for x in range(1,16):
    url = u1 + str(max) + u2 + str(min) 
    data = requests.get(
            url, 
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "authority": "m.tiktok.com",
                "path": url.split("tiktok.com")[1],
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "m.tiktok.com",
                "cookie": "sessionid_ss="+ cookie_session +";",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            },
        )
    min = data.json()['minCursor']
    #print(min)
    max = data.json()['maxCursor']
    #print(max)
    lista = lista + data.json()['userList']
    print(len(lista))
    #if(x%2 == 0):
    #    print("..")
lista.sort(reverse=True, key=ordenar)
for y in range(30):
    print(lista[y]['user']['nickname'], lista[y]['user']['uniqueId'], lista[y]['stats']['followerCount'])
    #print(lista[y]['stats']['followerCount'])


#print (data.json()["userList"][0]["user"]["nickname"])
