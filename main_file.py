from tkinter import *
from tkinter import ttk
import webbrowser
from tkinter.font import Font
import threading
from playsound import playsound
import web_scrap as ws

main_window = Tk()
main_window.title("anti corona virus")
main_window.config(bg="green")
main_window.geometry("300x400")
main_window.resizable(False, False)

t1 = threading.Thread(target=ws.world)
t2 = threading.Thread(target=ws.india)
t1.start()
t2.start()
t1.join()
t3 = threading.Thread(target=ws.audio_file)
t3.start()
t2.join()
t3.join()
t4 = threading.Thread(target=ws.audio)
t4.start()
my_font = Font(family="lobster 1.4", size=20)
anticorona = Label(main_window, text='Anti Corona Virus', font=my_font, bg="green", fg="white").place(x=45, y=10)

#                   ---------------------world stats-----------------------

world = Label(main_window, text="world stats are:- ", font="times 15 bold italic", bg="green", fg="white").place(x=30, y=45)
L1 = Label(main_window, text="corona cases are:-             " + str(ws.casesW), font="times 12 bold italic", bg="green", fg="white").place(x=30, y=75)
L2 = Label(main_window, text="number of deaths are:-     " + str(ws.deathW), font="times 12 bold italic", bg="green", fg="white").place(x=30, y=95)
L3 = Label(main_window, text="people recovered are:-      " + str(ws.recoverW), font="times 12 bold italic", bg="green", fg="white").place(x=30, y=115)
#            ---------------------------------------------------------------------

#                   ---------------------india stats-----------------------

india = Label(main_window, text="india stats are:- ", font="times 15 bold italic", bg="green", fg="white").place(x=30, y=175)
L4 = Label(main_window, text="corona cases are:-            " + str(ws.casesI.replace('\n','')), font="times 12 bold italic", bg="green", fg="white").place(x=30, y=205)
L5 = Label(main_window, text="number of deaths are:-    " + str(ws.deathI.replace('\n','')), font="times 12 bold italic", bg="green", fg="white").place(x=30, y=225)
L6 = Label(main_window, text="people recovered are:-     " + str(ws.recoverI.replace('\n','')), font="times 12 bold italic", bg="green", fg="white").place(x=30, y=245)
#            ---------------------------------------------------------------------

#            ------------------------- end buttons ------------------------------
def info():
     h = variable.get()
     print(h)


def page():
     webbrowser.open('https://www.who.int/emergencies/diseases/novel-coronavirus-2019', new=1)


B1 = Button(main_window, text='precautions', font='haventica 11', fg='green', command=ws.precautions).place(x=10, y=280)
B2 = Button(main_window, text='symptoms', font='haventica 11', fg='green', command=ws.symptoms).place(x=101, y=280)
B3 = Button(main_window, text='visit WHO site', font='haventica 11', fg='green', command=page).place(x=185, y=280)
variable = StringVar()
variable.set("choose a state")
D1 = ttk.Combobox(main_window, textvariable=variable, values=ws.i, foreground="green").place(x=80, y=320)
B3 = Button(main_window, text='show stats', font='haventica 11', fg='green',command=info).place(x=100, y=350)
#           ---------------------------------------------------------------------
main_window.mainloop()
