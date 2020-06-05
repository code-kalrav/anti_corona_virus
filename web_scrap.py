from gtts import gTTS
from playsound import playsound
import requests
import bs4
from tkinter import *
from urllib.request import urlopen
import urllib.request

language = "en"

#           ------------------------------world data------------------------------
casesW = "0"
deathW = "0"
recoverW = "0"


def world():
    global casesW
    global deathW
    global recoverW
    requestW = requests.get("https://www.worldometers.info/coronavirus/")
    lxmlW = bs4.BeautifulSoup(requestW.text, 'html.parser')
    selectW = lxmlW.select(".maincounter-number > span")
    casesW = selectW[0].text
    deathW = selectW[1].text
    recoverW = selectW[2].text


def audio_file():
    total_world = "the total corona virus cases are.... " + str(casesW)
    output = gTTS(text=total_world, lang=language)
    output.save("world_cases.mp3")


def audio():
    playsound('starting.mp3')
    playsound('world_cases.mp3')


#          -------------------------------------------------------------------------


#          ---------------------------india data------------------------------------
casesI = "0"
deathI = "0"
recoverI = "0"


def india():
    # print("this is working")
    global casesI
    global deathI
    global recoverI
    res1 = requests.get("https://www.mohfw.gov.in")
    soup = bs4.BeautifulSoup(res1.content, 'html.parser')
    select1 = soup.find_all('td')
    for i in range(175, 270):
        print(select1[i])
        if select1[i].text == "Total#":
            print("this loop is working")
            casesI = str(select1[i + 1].text)
            # print(casesI)
            deathI = str(select1[i + 3].text)
            # print(deathI)
            recoverI = str(select1[i + 2].text)
            # print(recoverI)
            break
        else:
            pass


#          ------------------------------------------------------------------------
i = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
     "Himachal Pradesh",
     "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
     "Mizoram",
     "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
     "Uttarakhand",
     "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu",
     "Lakshadweep",
     "Delhi", "Puducherry"]
k = open("precautions.txt", "r")

top = None
top1 = None
def precautions():
    global top
    print(type(top))
    if str(type(top)) != "<class 'tkinter.Toplevel'>":
        pass
    else:
        top.destroy()
        top.update()
    top = Toplevel()
    top.title("precautions to be taken")
    top.config(bg="green")
    top.geometry("570x370")
    top.resizable(False, False)
    label = Label(top, text="precautions to be taken", fg="white", bg="green", font="times 15").place(x=180, y=10)
    for j in range(0, 21):
        a = k.readline()
        label = Label(top, text=a, fg="white", bg="green").place(x=20, y=(j * 15) + 40)
    k.seek(0)


l = open("symptoms.txt", "r")


def symptoms():
    global top1
    print(type(top1))
    if str(type(top1)) != "<class 'tkinter.Toplevel'>":
        pass
    else:
        top1.destroy()
        top1.update()
    top1 = Toplevel()
    top1.title("symptoms for corona")
    top1.config(bg="green")
    top1.geometry("580x500")
    top1.resizable(False, False)
    label = Label(top1, text="symptoms for corona", fg="white", bg="green", font="times 15").place(x=180, y=10)
    for j in range(0, 27):
        a = l.readline()
        label = Label(top1, text=a, fg="white", bg="green").place(x=20, y=(j * 15) + 40)
    l.seek(0)


def picture():
    html = urlopen('https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India')
    bs = bs4.BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img',
                         alt="India COVID-19 confirmed cases map.svg")  # ,class_='name of class'   alt="Extended-protected article"
    b = "https:" + images[0]['src']
    # print(b)
    urllib.request.urlretrieve(b, 'C:/Users/kalra/Desktop/anticoronavirus/unnamed.jpg')

def t():
    top.destroy()
    top.update()