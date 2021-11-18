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
cookie_session= "e6d9601f8c8646eee4dbf4c1bc900329"
for x in range(55):
    if(min == -1 and max == -1):
        break
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
    #print("min", min)
    max = data.json()['maxCursor']
    #print("max", max)
    if(min != -1 and max != -1):
        lista = lista + data.json()['userList']
    else:
        print(data.json())
    '''
    for z in data.json()['userList']:
        if z['user']['uniqueId'] == "c_flores_boliviana":
            print("---BLOQUEADA---")
            print(json.dumps(z))
        if z['user']['uniqueId'] == "carlamarianela16":
            print("---SEGUIDA---")
            print(json.dumps(z))
        if z['user']['uniqueId'] == "litzyparadachavez":
            print("---AMIGA---")
            print(json.dumps(z))
        '''
    #print(x, len(lista))
lista.sort(reverse=False, key=ordenarSeguidores)

listavacio = []
print("-------------- lista ---------------")
for a in lista:
    if a["stats"]["followerCount"] < 100:
        print(a['user']['uniqueId'], a['stats']['followerCount'])
    if a['stats']['videoCount'] <= 2:
        listavacio.append(a)
print("-------------- listavacio --------------")
for b in listavacio:
    #print(json.dumps(b))
    print(b['user']['uniqueId'], b['stats']['followerCount'], b['stats']['videoCount'])
    url_follow = "https://m.tiktok.com/api/commit/follow/user/?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=7024110700697290246&region=BO&priority_region=BO&os=windows&referer=https:%2F%2Fwww.tiktok.com%2Fsearch%3Fq%3Dmiranda_erika0%26t%3D1637247899119&root_referer=https:%2F%2Fwww.tiktok.com%2F&cookie_enabled=true&verifyFp=verify_kw4y22i6_W4ocAi9V_74Mi_4ed6_8RQf_fEtNtXW36C1b&app_language=es&timezone_name=America%2FLa_Paz&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=4&battery_info=%7B%7D&type=0&user_id=" + b['user']['id'] + "&from=19&channel_id=3&from_pre=0&current_region=BO&fromWeb=1&msToken=KhJjrwqJJHxSvn54WNSFsmzce7rGAIPCkzrVr7x-MSYrmiAd8-yxKUTyAir0brY05aLqgaCjApYBcvzAjWut9mCaHDN0ZCGQJuJTuO7taOBEIxpOT2oIaFVToicLyjx2NO5xCMvU&X-Bogus=DFSzswVu1DTANVXKS7QFnQYklTXq&_signature=_02B4Z6wo00001P7IQLQAAIDBIL4YEi2ybcj-yEQAAF4q5e"
    '''
    data2 = requests.post(
            url_follow, 
            headers={
                "Accept": "application/json, text/plain, */*",
                "authority": "m.tiktok.com",
                "content-type": "application/x-www-form-urlencoded",
                "path": url_follow.split("tiktok.com")[1],
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Host": "m.tiktok.com",
                "cookie": "tt_csrf_token=CKwhKT7SlIenEAOP695F5n0w; R6kq3TV7=AN8hEjN9AQAANXh3desljLYtcvLtYuDmHKnyQPxMI77O3uwy7ZmifzpESXbt|1|0|36e721d7127660e1cb6956d020cc888b66f7a625; passport_csrf_token_default=37e4a31ebbdc83d31159b251b13000e6; passport_auth_status=7e737df8415be40e2b953e4a8d157843%2C; passport_auth_status_ss=7e737df8415be40e2b953e4a8d157843%2C; sid_guard=e6d9601f8c8646eee4dbf4c1bc900329%7C1637239380%7C5184000%7CMon%2C+17-Jan-2022+12%3A43%3A00+GMT; uid_tt=1f5446b99a677194af771cd738d07cfef7355f9f68a5feba03de8f53cccef163; uid_tt_ss=1f5446b99a677194af771cd738d07cfef7355f9f68a5feba03de8f53cccef163; sid_tt=e6d9601f8c8646eee4dbf4c1bc900329; sessionid=e6d9601f8c8646eee4dbf4c1bc900329; sessionid_ss=e6d9601f8c8646eee4dbf4c1bc900329; sid_ucp_v1=1.0.0-KGYwMGMzMzM0NDZkYmQ0ODc2NTgwZTE5NjU4MTVjNmJiZTUzYTAxZGEKHwiGiJaE7tqo6V0Q1JTZjAYYswsgDDCQxsruBTgIQAoQAxoGbWFsaXZhIiBlNmQ5NjAxZjhjODY0NmVlZTRkYmY0YzFiYzkwMDMyOQ; ssid_ucp_v1=1.0.0-KGYwMGMzMzM0NDZkYmQ0ODc2NTgwZTE5NjU4MTVjNmJiZTUzYTAxZGEKHwiGiJaE7tqo6V0Q1JTZjAYYswsgDDCQxsruBTgIQAoQAxoGbWFsaXZhIiBlNmQ5NjAxZjhjODY0NmVlZTRkYmY0YzFiYzkwMDMyOQ; store-idc=maliva; store-country-code=bo; passport_csrf_token=37e4a31ebbdc83d31159b251b13000e6; msToken=X3v3XkTs90jBVIOf1KfpfqaQOu65RE35CypyZEDpCpbBJVRLZpcTbiPnCU2Asqw4ep_B6ix7jTxmbg5UIr6WGI6Hjczb1JdeJOuEOUwErR2iM7-gKDGUFHtO4Ov12rHb9qA8M838; cmpl_token=AgQQAPPdF-RMpY3sTHFot10_-xs-RCWKP4TtYMPHSg; ttwid=1%7CwFo1ktWgGl369jy-6ISUm3PpU6iCxCvD_Rwj2MZgkKg%7C1637249165%7Ca02269c29518b89719ad70b26119f6d050521b64ac26c2634421d4936166273a; odin_tt=8e8073f23be1505fba24869c3ebd0bcb835dbd9535559a9dad98ee1f0e4dbad0ef675dfc6131490b965f432915ef8d8f64aa4ed9fab1634e8683b0a50245429e606944d6826b6aa09b20f645ea015299",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "tt-csrf-token":"CKwhKT7SlIenEAOP695F5n0w"
            },
        )
    print(data2)
    '''
print("finnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
#for y in range(100):
    #print(y, lista[y]['user']['uniqueId'], lista[y]['stats']['followerCount'], lista[y]['stats']['videoCount'])
    #print(lista[y]['stats']['followerCount'])

#print (data.json()["userList"][0]["user"]["nickname"])
