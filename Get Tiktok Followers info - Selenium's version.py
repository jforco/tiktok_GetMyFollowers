
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time, json
from seleniumwire import webdriver
from seleniumwire.utils import decode
import json


def leerLista(direccion):
    lista = []
    try:
        f = open(direccion)
        lista = json.load(f)
        f.close()
    except Exception:
        pass
    return lista

def guardarLista(direccion, lista):
    with open(direccion, 'w') as fout:
        json.dump(lista , fout)
        
#chrome
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
# options.add_argument("--headless") # for work without a visible browser
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# Default User Profile
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=C:/tk")
driver = webdriver.Chrome(service=service, options=options)
# You can stop this script here, to log in your tiktok account. Script into 'if loopControl' works in a browser with an account already open

# When gets your followers info, script saves it on a file to process on the next running without enter tiktok again. Control that with the folling var 'loopControl'.
listaUsuariosTodos = leerLista("D:\\listaAllTK.json")

# When true, enter to selenium to get list. False to jump to process from saved file
loopControl = False

if loopControl:
    # get your list with selenium
    listaUsuariosTodos = []
    # Replace after @, with your userId.
    driver.get("https://www.tiktok.com/@XXX_YOUR_USER_ID_XXXX")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#main-content-others_homepage > div > div.css-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2.enm41492 > h3 > div:nth-child(1) > span').click()
    time.sleep(2)
    count = len(driver.find_elements(By.XPATH, '//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li'))
 
    while loopControl:
        ultimoItem = driver.find_element(By.XPATH, '//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[last()]')
        driver.execute_script("arguments[0].scrollIntoView();", ultimoItem)
        time.sleep(3)
        count2 = len(driver.find_elements(By.XPATH, '//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li'))
        loopControl = not count == count2
        count = count2
        print(count)

    listaRequests = driver.requests
    for request in listaRequests: 
        if request.path == '/api/user/list/': 
            try:
                body = decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                body = body.decode()
                data = json.loads(body)
                #data = json.dumps(data, indent=4, sort_keys=True)
                #print(data)
                data = data['userList']
                listaUsuariosTodos = listaUsuariosTodos + data
            except: 
                pass
            finally:
                print(len(listaUsuariosTodos), " + ", count)
    # check for remove larger attributes, for a smaller saved file.
    for usuario in listaUsuariosTodos:
        del usuario['user']['avatarLarger']
        del usuario['user']['avatarMedium']
        del usuario['user']['avatarThumb']
        del usuario['user']['secUid']
    # save data recovered for future work.
    guardarLista("D:\\listaAllTK.json", listaUsuariosTodos) 


# here deletes followed accounts by followers number criteria
listaUsuarios = listaUsuariosTodos.copy()
listaUsuariosEliminar = []

#get list of users to remove.
for usuario in listaUsuarios:
    if(usuario['stats']['followerCount'] > 0 and usuario['stats']['followerCount'] < 5900):
        listaUsuariosEliminar.append(usuario)

# remove them (unfollow) with selenium
for usuario in listaUsuariosEliminar:
    id = usuario['user']['uniqueId']
    driver.get("https://www.tiktok.com/@" + id)
    time.sleep(3)
    try:
        driver.find_element(By.CSS_SELECTOR, '.css-1us3psh-DivFollowIconContainer').click()
        listaUsuariosTodos.remove(usuario)
        #guardarLista("D:\\listaAllTK.json", listaUsuariosTodos)
        time.sleep(1)
    except (NoSuchElementException, ElementClickInterceptedException) as e:
        listaUsuariosTodos.remove(usuario)
    except Exception as e:
        pass
    
if len(listaUsuariosEliminar) > 0:
    guardarLista("D:\\listaAllTK.json", listaUsuariosTodos)
driver.close() 
