import requests,re, time, json, os, sys
from bs4 import BeautifulSoup
class main:
 def tik():
  titik = ['.   ','..  ','... ']
  for eek in titik:
    print ("\r"+w.i+"["+w.k+"-"+w.i+"] "+w.h+"Memulai menuyul"+eek,end="\r",flush=True);time.sleep(1)
 def banner():
  main.jalan(f"""{w.u}    ____                   ____             __       
{w.u}   / __ \____  ____ ____  / __ )__  _______/ /_______
{w.u}  / / / / __ \/ __ `/ _ \/ __  / / / / ___/ //_/ ___/
{w.ut} / /_/ / /_/ / /_/ /  __/ /_/ / /_/ / /__/ ,< (__  ) 
{w.u}/_____/\____/\__, /\___/_____/\__,_/\___/_/|_/____/  
{w.u}            /____/                                   """)
 def subbanner():
  main.jalan(f"""{w.i}[{w.h}-{w.i}] {w.b}Author {w.i}: {w.m}abilseno11
{w.i}[{w.h}-{w.i}] {w.b}Nama SC {w.i}: {w.m}Script nuyul web dogebucks.online
{w.i}[{w.h}-{w.i}] {w.b}Github {w.i}: {w.m}https://github.com/AbilSeno
                           {w.tm}START{w.df}""")
 def jalan(kntl):
        for oon in kntl + '\n':
                sys.stdout.write(oon)
                sys.stdout.flush()
                time.sleep(0.001)
 def start():
     os.system("clear")
     main.banner()
     main.subbanner()
     main.tik()
     while True:
      mul = r.get('https://dogebucks.online/dashboard',headers=hd,cookies=coki).text
      soup = BeautifulSoup(mul, 'html.parser')
      cari = soup.find("input", {'type':'hidden','id':'getBalance'})
      print (f"{w.i}[{w.c}+{w.i}] {w.k}Balance kamu : {w.u}"+cari["value"])
      time.sleep(4)
class w:
 m = '\033[1;31m' # merah
 b = '\033[1;36m' # biru
 k = '\033[1;33m' # kuning
 h = '\033[1;32m' # hijau
 u = '\033[1;35m' # ungu
 p = '\033[1;37m' # putih
 i = '\033[1;90m' # abu abu
 ut = '\033[1;34m' # ungu tua
 tm = '\x1b[103m\x1b[31m' # tebal merah (background kuning)
 df = '\x1b[0m'
 c = '\033[1;96m' # cyan
r = requests.Session()
hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36',
}
with open('config.json','r') as tod:
 y = json.loads(tod.read())
coki = {
'__cfduid':y["__cfduid"],
'ci_session':y["ci_session"],
'remember_code':y["remember_code"]
}
if __name__ == '__main__':
 try:
  main.start()
 except TypeError:print (f"{w.i}[{w.k}-{w.i}] {w.m}Login gagal, periksa file configmu")
 except KeyboardInterrupt:print (f"{w.i}[{w.k}-{w.i}] {w.b}Ok, keluar...");sys.exit()
 except requests.exceptions.ConnectionError:
  print (f"{w.i}[{w.k}-{w.i}] {w.m}Jaringan tidak memadai silahkan coba lagi...")
  elol = input(f"{w.i}[{w.k}-{w.i}] {w.k}Coba lagi {w.i}[{w.h}y{w.i}/{w.m}n{w.i}] ? ")
  if (elol == 'y') or (elol == 'Y'):
   main.start()
  else:
   print (f"{w.i}[{w.k}-{w.i}] {w.b}Ok, keluar...")
