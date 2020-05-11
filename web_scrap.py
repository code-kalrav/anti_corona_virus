from gtts import gTTS
from playsound import playsound
import requests
import bs4
from tkinter import *

language = "en"

#           ------------------------------world data------------------------------
casesW = 0
deathW = 0
recoverW = 0


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
casesI = 0
deathI = 0
recoverI = 0


def india():
    global casesI
    global deathI
    global recoverI
    res1 = requests.get("https://www.mohfw.gov.in")
    soup = bs4.BeautifulSoup(res1.content, 'html.parser')
    select1 = soup.find_all('td')
    casesI = select1[161].text
    deathI = select1[162].text
    recoverI = select1[163].text


#          ------------------------------------------------------------------------

i = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
     "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
     "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
     "Uttarakhand", "Uttar Pradesh", "West Bengal"]

k = open("precautions.txt", "r")
def precautions():
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
    top = Toplevel()
    top.title("symptoms for corona")
    top.config(bg="green")
    top.geometry("580x500")
    top.resizable(False, False)
    label = Label(top, text="symptoms for corona", fg="white", bg="green", font="times 15").place(x=180, y=10)
    for j in range(0, 27):
        a = l.readline()
        label = Label(top, text=a, fg="white", bg="green").place(x=20, y=(j * 15) + 40)
    l.seek(0)