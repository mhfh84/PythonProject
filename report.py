from tkinter import *
import tkinter
import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
from fpdf import FPDF
import os
from tkinter import END, Button, IntVar, Label, StringVar, Toplevel, ttk
from tkcalendar import DateEntry
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

# Create a connection to the SQLite database
conn = sqlite3.connect('database.db')

# Define function to generate report
def generate_report():
    # Get user input
    admin = admin_combo.get()
    stage = edu.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()

    # Query the database
    query = f"SELECT * FROM الأوذونات WHERE الادارة = '{admin}' AND المرحلة = '{stage}' AND التاريخ BETWEEN '{start_date}' AND '{end_date}'"
    df = pd.read_sql_query(query, conn)

    # Check if there are any results
    if df.empty:
        messagebox.showinfo("Error", "No data found for the selected criteria.")
    else:
        # Display the results in a new window
        result_window = window

        # Create a text widget to display the results
        result_text = Text(result_window, height=31, width=157)
        result_text.place(x=10, y=100)

        # Insert the results into the text widget
        result_text.insert(END, df.to_string(index=False))

        # Add buttons to save the results to Excel and PDF
        save_excel_button = Button(result_window, text="Save to Excel", command=lambda: save_to_excel(df))
        save_excel_button.pack()

        save_pdf_button = Button(result_window, text="Save to PDF", command=lambda: save_to_pdf(df))
        save_pdf_button.pack()

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

# Define function to save results to Excel
def save_to_excel(df):
    # Get the file path from the user
    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')

    # Save the results to Excel
    df.to_excel(file_path, index=False)

# Define function to save results to PDF
def save_to_pdf(df):
    # Get the file path from the user
    file_path = filedialog.asksaveasfilename(defaultextension='.pdf')

    # Create a new PDF document
    pdf = FPDF()
    pdf.add_page()

    # Add the results to the PDF document
    for index, row in df.iterrows():
        for value in row:
            pdf.cell(40, 10, str(value), 1)
        pdf.ln()

    # Save the PDF document
    pdf.output(file_path)

# Clear Button
def clear_text():
    admin_combo.delete(0, END)
    edu.set(None)
    start_date_entry.delete(0, END)
    end_date_entry.delete(0, END)

# Exit Button
def askYesNo():
    reply = messagebox.askyesno('تاكيد الخروج', 'هل تريد الخروج من البرنامج؟')
    if reply == True:
        window.destroy()
        os.system("python main.py")  # Replace with "python3" if using Python 3.x

# Create the Tkinter GUI


# Add labels and entry fields to select data
admin_combo_Lable = tkinter.Label(window, text="الإدارة التعليمية").place(x=1190, y=30)
admin_combo = ttk.Combobox(window, values=الادارات)
admin_combo.place(x=1030, y=30)

# Creating a Radio Button for Educational Stages
edu_Lable = tkinter.Label(window, text="المرحلة التعليمية")
edu_Lable.place(x=930, y=30)

edu=tk.StringVar()
edu.set(None)

r1 = ttk.Radiobutton(window, text="رياض اطفال", variable=edu, value="رياض اطفال")
r1.place(x=830, y=30)
r1 = ttk.Radiobutton(window, text="أبتدائى", variable=edu, value="أبتدائى")
r1.place(x=750, y=30)
r1 = ttk.Radiobutton(window, text="أعدادى", variable=edu, value="أعدادى")
r1.place(x=670, y=30)
r1 = ttk.Radiobutton(window, text="ثانوى", variable=edu, value="ثانوى")
r1.place(x=590, y=30)
# Creating Date Entry
date_entry_Lable = tkinter.Label(window, text="التاريخ").place(x=510, y=30)


start_date_entry_Lable = tkinter.Label(window, text="من")
start_date_entry_Lable.place(x=490, y=30)
start_date_entry=DateEntry(window,selectmode='day')
start_date_entry.place(x=390, y=30)

end_date_entry_Lable = tkinter.Label(window, text="حتى")
end_date_entry_Lable.place(x=340, y=30)
end_date_entry=DateEntry(window,selectmode='day')
end_date_entry.place(x=240, y=30)



# Add a button to generate the report
button = ttk.Button(master = window, text="عرض البيانات", command=generate_report).place(x=100, y=20, width=120,height=40)
button = ttk.Button(master = window, text = "مسح البيانات", command = clear_text).place(x=150, y=660, width=120,height=40)
button = ttk.Button(master = window, text = "خروج", command = askYesNo).place(x=25, y=660, width=120,height=40)
# Run the Tkinter event loop
window.mainloop()
