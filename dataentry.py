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
window.geometry("500x320")
window.config()
window.iconbitmap("")
window.resizable(width=False,height=False)
window.title("ادخال الاذونات")

frame = tkinter.Frame(window)
frame.pack()

# Data Sources
def enter_data():
    الإدارة = administrations_combo.get()
    المدرسة = schools_combo.get()
    التاريخ = cal.get()
    المرحلة = edu.get()
    الوجبات = meals_entry.get()

    if الإدارة and المدرسة and التاريخ and المرحلة and  الوجبات:
    
        # print ("الإدارة: ", الإدارة)
        # print ("المدرسة: ", المدرسة)
        # print ("التاريخ: ", التاريخ)
        # print ("المرحلة: ", المرحلة)
        # print ("الوجبات: ", الوجبات)
        # print ("-----------------------------------------")

        # Create Table On Database
        conn = sqlite3.connect('database.db')
        
        table_create_query = '''create table if not exists الأوذونات
            (الادارة TEXT, المدرسة TEXT, التاريخ TEXT, المرحلة TEXT, الوجبات INT)
        '''
        conn.execute(table_create_query)

        # Insert data into the table
        data_insert_query = '''INSERT INTO الأوذونات (الادارة, المدرسة, التاريخ, المرحلة, الوجبات) VALUES (?,?,?,?,?)'''
        data_insert_tuple = (الإدارة, المدرسة, التاريخ, المرحلة, الوجبات)
        cursor = conn.cursor()
        cursor.execute(data_insert_query, data_insert_tuple)
        conn.commit()
        conn.close()

        messagebox.showinfo('معلومات','تم الادخال بنجاح')

        administrations_combo.delete(0, END)
        schools_combo.delete(0, END)
        edu.set(None)
        meals_entry.delete(0, END)

    else:
        tkinter.messagebox.showerror("خطا", "رجاء ادخال كافة الخلايا")
    
# Clear Button
def clear_text():
    administrations_combo.delete(0, END)
    schools_combo.delete(0, END)
    edu.set(None)
    meals_entry.delete(0, END)

# Exit Button
def askYesNo():
    reply = messagebox.askyesno('تاكيد الخروج', 'هل تريد الخروج من البرنامج؟')
    if reply == True:
        window.destroy()
        os.system("python main.py")  # Replace with "python3" if using Python 3.x
        
# Creating a list of Administrations
الادارات = [
    "روض الفرج",
    "الساحل",
    "مصر القديمة"
]

# Creating a list of schools
روض_الفرج = [
    "1",
    "2",
    "3"
]

الساحل = [
    "4",
    "5",
    "6"
]

مصر_القديمة = [
    "7",
    "8",
    "9"
]

# Define the Drop Boxes
def pick_school(e):
    if administrations_combo.get() == "روض الفرج":
        schools_combo.configure(values=روض_الفرج)
        schools_combo.current(0)
    if administrations_combo.get() == "الساحل":
        schools_combo.configure(values=الساحل)
        schools_combo.current(0)
    if administrations_combo.get() == "مصر القديمة":
        schools_combo.configure(values=مصر_القديمة)
        schools_combo.current(0)

# Info of Adminstrations and Schools and Date
user_info_frame = tkinter.LabelFrame(frame, text="معلومات الاذن")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

# Creating Administrations drop box
administrations_combo_Lable = tkinter.Label(user_info_frame, text="الإدارة التعليمية")
administrations_combo_Lable.grid(row=0, column=2)
administrations_combo = ttk.Combobox(user_info_frame, values=الادارات)
administrations_combo.grid(row=1, column=2)

#Bind the combobox
administrations_combo.bind("<<ComboboxSelected>>", pick_school)

# Creating Schools drop box
schools_combo_Lable = tkinter.Label(user_info_frame, text="المدرسة")
schools_combo_Lable.grid(row=0, column=1)
schools_combo = ttk.Combobox(user_info_frame, values=[" "])
schools_combo.grid(row=1, column=1)
schools_combo.current(0)

# Creating Date Entry
cal_Lable = tkinter.Label(user_info_frame, text="التاريخ")
cal_Lable.grid(row=0, column=0)
cal=DateEntry(user_info_frame,selectmode='day')
cal.grid(row=1,column=0)

# For Padding
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Info of Tickets
tickets_frame = tkinter.LabelFrame(frame, text="أدخال البيانات")
tickets_frame.grid(row= 1, column=0, sticky="news", padx=20, pady=10)

# Creating a Radio Button for Educational Stages
edu_Lable = tkinter.Label(tickets_frame, text="المرحلة التعليمية")
edu_Lable.grid(row=0, column=5)

edu=tk.StringVar()
edu.set(None)

r1 = ttk.Radiobutton(tickets_frame, text="رياض اطفال", variable=edu, value="رياض اطفال")
r1.grid(row=1, column=5)

r1 = ttk.Radiobutton(tickets_frame, text="أبتدائى", variable=edu, value="أبتدائى")
r1.grid(row=1, column=4)

r1 = ttk.Radiobutton(tickets_frame, text="أعدادى", variable=edu, value="أعدادى")
r1.grid(row=1, column=3)

r1 = ttk.Radiobutton(tickets_frame, text="ثانوى", variable=edu, value="ثانوى")
r1.grid(row=1, column=2)

# Number of Meals
meals_Lable = tkinter.Label(tickets_frame, text="عدد الوجبات")
meals_Lable.grid(row=2, column=5)
meals_entry = tkinter.Entry(tickets_frame)
meals_entry.grid(row=2, column=4)

# For Padding
for widget in tickets_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Data Entry Buttons
# Button(window, text="إدخال الأذن", width=15,height=2, command=enter_data).place(x=350, y=250)
# Button(window, text="مسح البيانات", width=15,height=2, command=clear_text).place(x=190, y=250)
# Button(window, text="خروج", width=15,height=2, command=askYesNo).place(x=30, y=250)

button = ttk.Button(master = window, text = "إدخال الأذن", command = enter_data).place(x=350, y=250, width=120,height=40)
button = ttk.Button(master = window, text = "مسح البيانات", command = clear_text).place(x=185, y=250, width=120,height=40)
button = ttk.Button(master = window, text = "خروج", command = askYesNo).place(x=25, y=250, width=120,height=40)



# button = tkinter.Button(frame, text="أدخل البيانات", command=enter_data)
# button.grid(row=3, column=0, padx=20, pady=10)

# button = tkinter.Button(window, text="Quit", command=askYesNo).pack()
# Button(window,text="Clear", command=clear_text, font=('Helvetica bold',10)).pack()

window.mainloop()