import tkinter
import tkinter as tk
from tkinter import END, Button, IntVar, Label, StringVar, Toplevel, ttk
from tkcalendar import DateEntry
from tkinter import *
from tkinter import messagebox
import sqlite3
import os
import pytz
import time
from datetime import datetime
import subprocess
import sys

window = tkinter.Tk()
window.geometry("1280x720")
window.config()
window.iconbitmap("")
window.resizable(width=False,height=False)
window.title("برنامج مخازن التغذية المدرسية")

# def open_dataentry_file():
#     os.system("python dataentry.py")  # Replace with "python3" if using Python 3.x

def open_dataentry_file():
    subprocess.Popen(["python", "dataentry.py"])
    sys.exit()
    
def open_calc_file():
    os.system("python calc.py")  # Replace with "python3" if using Python 3.x

def open_report_file():
    subprocess.Popen(["python", "report.py"])
    sys.exit()

frame = tkinter.Frame(window)
frame.pack()

def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(200, update_clock)

def askYesNo():
    reply = messagebox.askyesno('تاكيد الخروج', 'هل تريد الخروج من البرنامج؟')
    if reply == True:
        window.destroy()

welcome_frame = tkinter.LabelFrame(frame, text="مرحبا بكم فى برنامج مخازن التغذية المدرسية")
welcome_frame.grid(row= 0, column=0, sticky="news", padx=20, pady=10)

# Day and Time
digital_clock_lbl = tkinter.Label(window, text="00:00:00", font="Helvetica 10 bold")
digital_clock_lbl.place(x=50, y=100)

update_clock()

# Creating Welcome Text
info_Lable = tkinter.Label(welcome_frame, text="")
info_Lable.grid(row=0, column=12)

info_Lable = tkinter.Label(welcome_frame, text="تستطيع من خلال هذا البرنامج ان تسجل الاذونات الخاصة بالتغذية المدرسية")
info_Lable.grid(row=2, column=5)

info_Lable = tkinter.Label(welcome_frame, text=" واستخراج كافة التقارير الاخرى الخاصة بالمخزن والمطابقات مع الادارات التعليمية بشكل سريع ومنظم")
info_Lable.grid(row=3, column=5)
info_Lable = tkinter.Label(welcome_frame, text="")
info_Lable.grid(row=4, column=0)

# Button(window, text="إدخال الأذونات", command=open_dataentry_file, width=15,height=2).place(x=1100, y=150)
# Button(window, text="أستخراج المطابقات", width=15,height=2).place(x=900, y=150)

button = ttk.Button(master = window, text = "إدخال الأذونات", command = open_dataentry_file).place(x=1100, y=150, width=150,height=50)
button = ttk.Button(master = window, text = "أستخراج المطابقات", command= open_report_file).place(x=900, y=150, width=150,height=50)
button = ttk.Button(master = window, text = "الألة الحاسبة", command = open_calc_file).place(x=700, y=150, width=150,height=50)

button = ttk.Button(master = window, text = "خروج", command = askYesNo).place(x=25, y=660, width=120,height=40)

window.mainloop()