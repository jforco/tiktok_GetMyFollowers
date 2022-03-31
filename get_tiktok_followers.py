# obtener lista de seguidores en tiktok, y ordenarlos por cantidad de seguidores, y por cantidad de videos
import json
import requests

def ordenarVideo(e):
    return e["stats"]["videoCount"]
def ordenarSeguidores(e):
    return e["stats"]["followerCount"]

lista = []
u1 = 'https://m.tiktok.com/api/user/list/?count=199&maxCursor='
u2 = '&minCursor='
max = 0
min = 0
# paste value of sessionid_ss cookie 
# (if you are here, i think you know how to get that value from your browser when you are in your tiktok account)
cookie_session= ""
# range 55 because limit followings tiktok is 10k (10 001 users, not confirmed)
# every get request, get up to 199 profiles
for x in range(55):
    if(min == -1 and max == -1):
        # end of listing
        break
    # get next max and min ids  
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
    #print(data.json())
    min = data.json()['minCursor']
    #print("min", min)
    max = data.json()['maxCursor']
    #print("max", max)
    if(min != -1 and max != -1):
        lista = lista + data.json()['userList']
    else:
        # end of listing
        print(data.json())
        print("longitud de lista:", len(lista))
    
# sort following by cant of followers
lista.sort(reverse=False, key=ordenarSeguidores)


# DESDE AQUI, LISTA PERSONAL IMPRIMIENDO PERFILES SEGUIDOS MENORES A CIERTO NUMERO DE SEGUIDORES,
# Y TAMBIEN PERFILES QUE TIENEN MENOS DE 3 VIDEOS PUBLICADOS
listavacio = []
print("-------------- lista ---------------")
for a in lista:
    if a["stats"]["followerCount"] < 920:
        # printing  
        print(a['user']['uniqueId'], a['stats']['followerCount'])
    if a['stats']['videoCount'] < 3:
        listavacio.append(a)    
print("-------------- listavacio --------------")
for b in listavacio:
    #print(json.dumps(b))
    print(b['user']['uniqueId'], b['stats']['followerCount'], b['stats']['videoCount'])
    
print("finnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
