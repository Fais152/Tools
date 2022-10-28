import os 

os.system('clear')
os.system('pip install pyshorteners')
os.system('pip install pytube')
os.system('pip install pyqrcode')
os.system('pip install phonenumbers')
os.system('pip install gdown')
os.system('pip install requests')
os.system('pip install gtts')

import random
import pyqrcode
import phonenumbers
from phonenumbers import geocoder,carrier
import gdown
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from pytube import YouTube
from pyshorteners import Shortener
import calendar as cal

os.system('clear')

#warna
w='\e[97m'
g='\033[1;92m'
r='\033[1;91m'
a='\033[1;94m'
b='\e[1;4m'
cyan='\033[1;36m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
reset='\033[0m'
G='\e[110m'
G1='\e[101m'
o='\033[0m'

def textlogo():
    print (blue, """
 _____           _____    ___     ___    _       ____
|  ___|         |_   _|  / _ \   / _ \  | |     / ___|
| |_     _____    | |   | | | | | | | | | |     \___ |
|  _|   |_____|   | |   | |_| | | |_| | | |___   ___) |
|_|               |_|    \___/   \___/  |_____| |____/

Github : https://github.com/Fais152/
Coded by : Fais

 """, reset, green, "Note : Tools ini masih dalam tahap pengembangan", reset)

def menu():
    print (purple + """
    ---------- Silahkan Dipilih ----------
    
    [1] Lacak HP Menggunakan Nomor HP
    [2] Membuat QR Code
    [3] Pencarian Google (Suara)
    [4] Pencarian Google (Text)
    [5] Download Video YouTube
    [6] Password Generator
    [7] Link Shortener
    [8] Membuat Kalender
    
    --------------------------------------
    """ + reset)

def find_phone():
    print(blue + """
 _                    _      _   _ ____
| |    __ _  ___ __ _| | __ | | | |  _ |
| |   / _` |/ __/ _` | |/ / | |_| | |_) |
| |__| (_| | (_| (_| |   <  |  _  |  __/
|_____\__,_|\___\__,_|_|\_\ |_| |_|_|

Note : Hanya menampikan negara dan operator.
    """ + reset)
    inp = input(green + "Masukan nomor hp : ")
    nomor = phonenumbers.parse(inp)
    lokasi = geocoder.description_for_number(nomor, "id")
    operator = carrier.name_for_number(nomor, "id")
    print(lokasi,operator)

def gst():
    print(blue + """
   ____                   _        ____                      _
 / ___| ___   ___   __ _| | ___  / ___|  ___  __ _ _ __ ___| |__
| |  _ / _ \ / _ \ / _` | |/ _ \ \___ \ / _ \/ _` | '__/ __| '_ |
| |_| | (_) | (_) | (_| | |  __/  ___) |  __/ (_| | | | (__| | | |
 \____|\___/ \___/ \__, |_|\___| |____/ \___|\__,_|_|  \___|_| |_|

Note : Menampilkan hasil berupa text biasa
    """ + reset)
    find = input(green + "Cari : ")
    url = f"https://www.google.com/search?q={find}"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    cari = soup.find("div", class_="BNeawe").text
    print(cari)

def gsv():
    print(blue + """
   ____                   _        ____                      _
 / ___| ___   ___   __ _| | ___  / ___|  ___  __ _ _ __ ___| |__
| |  _ / _ \ / _ \ / _` | |/ _ \ \___ \ / _ \/ _` | '__/ __| '_ |
| |_| | (_) | (_) | (_| | |  __/  ___) |  __/ (_| | | | (__| | | |
 \____|\___/ \___/ \__, |_|\___| |____/ \___|\__,_|_|  \___|_| |_|

Note : Menampilkan result berupa suara dengan file berformat .mp3
    """ + reset)
    find = input(green + "Cari : ")
    url = f"https://www.google.com/search?q={find}"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    cari = soup.find("div", class_="BNeawe").text
    bahasa = "id"
    file = gTTS(text = cari, lang=bahasa)
    file.save('Suara.mp3')
    print("Suara Tersimpan, Silahkan Cek Di Dalam Folder!")
    
def qrcode():
    print(blue + """
  ___  ____     ____ ___  ____  _____
 / _ \|  _ \   / ___/ _ \|  _ \| ____|
| | | | |_) | | |  | | | | | | |  _|
| |_| |  _ <  | |__| |_| | |_| | |___
 \__\_\_| \_\  \____\___/|____/|_____|

Note : Membuat QR Code
    """ + reset)
    url = input(green + "Masukan URL : ")
    img = pyqrcode.create(url)
    img.svg("Qrcode.svg", scale=10)
    print(img.terminal(quiet_zone=1))

def ytdown():
    print(red + """
__   _______   ____                      _                 _
\ \ / /_   _| |  _ \  _____      ___ __ | | ___   __ _  __| |
 \ V /  | |   | | | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |
  | |   | |   | |_| | (_) \ V  V /| | | | | (_) | (_| | (_| |
  |_|   |_|   |____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|


Note : Downloaad Video YouTube
    """ + reset)
    print (green + "Contoh : https://youtu.be/fswGCaqCZoQ")
    link = input("Masukan Url YT : ")
    yt = YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download Selesai!")

def pswd(): 
    print(blue + """
____                  ____                           _
|  _ \ __ _ ___ ___   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __
| |_) / _` / __/ __| | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
|  __/ (_| \__ \__ \ | |_| |  __/ | | |  __/ | | (_| | || (_) | |
|_|   \__,_|___/___/  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|

Note : Membuat Password Random
    """ + reset)
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "ABCDEFGHIJKLMNOPQRSTUFWXYZ"
    c = "0123456789"
    d = "~!@#$%^&*()_."
    text = a + b + c + d
    jumlah = 17
    pswd = "".join(random.sample(text,jumlah))
    print(green + "Password Baru : " + pswd)

def shrt():
    print(blue + """
 ____  _                _     _     _       _
/ ___|| |__   ___  _ __| |_  | |   (_)_ __ | | __
\___ \| '_ \ / _ \| '__| __| | |   | | '_ \| |/ /
 ___) | | | | (_) | |  | |_  | |___| | | | |   <
|____/|_| |_|\___/|_|   \__| |_____|_|_| |_|_|\_|

Note : Hanya Short Link Biasa
    """ + reset)
    text = input(green + "Masukan URL : ")
    url = text
    shortener = Shortener()
    print("Short URL : {}".format(shortener.tinyurl.short(url)))

def kldr():
    print(blue + """
 _  __     _                _
| |/ /__ _| | ___ _ __   __| | ___ _ __
| ' // _` | |/ _ \ '_ \ / _` |/ _ \ '__|
| . \ (_| | |  __/ | | | (_| |  __/ |
|_|\_\__,_|_|\___|_| |_|\__,_|\___|_|

Note : Membuat Kalender
    """ + reset)
    tahun = int(input(green + "Masukan Tahun : "))
    for i in range(1, 13):
       print(cal.month(tahun, i))

textlogo()
menu()

pilih = input(green + "Fais~# " + reset)
os.system("clear")
if pilih == "1":
    find_phone()
elif pilih == "2":
    qrcode()
elif pilih == "3":
    gsv()
elif pilih == "4":
    gst()
elif pilih == "5":
    ytdown() 
elif pilih == "6":
    pswd()
elif pilih == "7":
    shrt()
elif pilih == "8":
    kldr()