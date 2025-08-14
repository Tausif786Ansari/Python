from tkinter import *
import tkcalendar as tkc
from datetime import datetime,date
from tkinter import messagebox
import os
import pygame
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# Initialize Window using Tkinter
root = Tk()
root.title("Age Calculator")
root.geometry("500x800+500+50")
root.minsize(500, 800)
root.resizable(True, True)

# Apply ttkbootstrap theme manually
style = tb.Style()
style.theme_use("solar")  # Apply the "solar" theme

# Icon
base_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(base_dir, "Ageicon.ico")
root.iconbitmap(icon_path)

#fetching current date
current_date=date.today()
pDay=int(current_date.day)
pMonth=int(current_date.month)
pYear=int(current_date.year)
pDate=current_date.strftime("%d-%m-%y")
# Function to fetch date and separate day, month, year
def get_date_birth():
    textbox_age.delete("1.0", "end")  # Clear previous text

    try:
        fetch_DOB = Birth_Date.entry.get()  # Get date as string from DateEntry widget
        # Convert to date object
        fetch_DOB = datetime.strptime(fetch_DOB, "%d/%m/%Y").date()  # Convert string to date object

        # Extract day, month, and year as integers
        Bday,Bmonth,Byear = fetch_DOB.day,fetch_DOB.month,fetch_DOB.year 

        #age calculating function
        age_cal(byear=Byear,bmonth=Bmonth,bday=Bday,Pday=pDay,Pmonth=pMonth,Pyear=pYear)

        # Insert extracted values into the textbox

    except Exception as e:
        textbox_age.insert("end", f"Error: {str(e)}")  # Handle any errors (e.g., invalid date)

#age solver function
def age_cal2(Pyear,Pmonth,Pday,Byear,Bmonth,BDay):
    ageYear=Pyear-Byear
    ageMonth=Pmonth-Bmonth
    ageDay=Pday-BDay
    textbox_age.insert(END,f"Age: {ageYear} years/ {ageMonth} months/ {ageDay} days")
#age calculating function
def age_cal(byear,bmonth,bday,Pday,Pmonth,Pyear):
    byear,bmonth,bday=int(byear),int(bmonth),int(bday)
    try:
        textbox_age.delete(1.0, END)
        if byear>Pyear:  
            textbox_age.insert(END,"You are not born yet")
         #code for calculating the age 
        elif (Pmonth<bmonth):
            year1=Pyear-1
            if(Pday>=bday):
                month1=Pmonth+12
                resultage=age_cal2(Pyear=year1,Pmonth=month1,Pday=Pday,Byear=byear,Bmonth=bmonth,BDay=bday)
            elif(Pday<bday):
                month1=Pmonth+11
                day1=Pday+30
                resultage=age_cal2(Pyear=year1,Pmonth=month1,Pday=day1,Byear=byear,Bmonth=bmonth,BDay=bday)
        elif (Pmonth>=bmonth):
            if(Pday>=bday):
                resultage=age_cal2(Pyear=Pyear,Pmonth=Pmonth,Pday=Pday,Byear=byear,Bmonth=bmonth,BDay=bday)
            elif(Pday<bday):
                month1=Pmonth-1
                day1=Pday+30
                resultage=age_cal2(Pyear=Pyear,Pmonth=month1,Pday=day1,Byear=byear,Bmonth=bmonth,BDay=bday)
    except Exception as e:
            textbox_age.insert("end", f"Error: {str(e)}")

def validate_date(event):
    date_text = Birth_Date.entry.get()  # Get text from DateEntry
    try:
        # Try converting to a valid date format
        datetime.strptime(date_text, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in dd/mm/yyyy format!")
        Birth_Date.delete(0, 'end')  # Clear invalid input

# Heading
headingLbl = Label(root, text="Age Calculator", font=("Algerian", 30, "bold"))
headingLbl.pack(pady=5)

# Frame 1
frame1 = Frame(root)
frame1.pack(fill="x", padx=10, pady=45)

# Birthdate Label
Birth_Label = Label(frame1, text="D.O.B", font=("Arial", 17, "bold"))
Birth_Label.grid(row=1, column=5, padx=35, ipadx=4, pady=10, sticky='nsew')

# Date Entry
Birth_Date = tb.DateEntry(frame1, firstweekday=0, startdate=datetime(2001, 11, 10), dateformat="%d/%m/%Y")
Birth_Date.grid(row=1, column=6, padx=10, pady=10, ipadx=4, sticky='nsew')

# Bind validation
Birth_Date.bind("<FocusOut>", validate_date)
Birth_Date.bind("<Return>", validate_date)

# Button Click Sound
base_dir1 = os.path.dirname(os.path.abspath(__file__))
sound_path1 = os.path.join(base_dir1, "sound.wav")
pygame.mixer.init()
click_sound = pygame.mixer.Sound(sound_path1)

def play_click_sound():
    click_sound.play()

# Frame 2
frame2 = Frame(root, height=120)
frame2.pack(fill="x", padx=10, pady=45)

# Button
date_btn = tb.Button(frame2, text="Click",command=lambda: [play_click_sound(), get_date_birth()],bootstyle="success-outline",padding=(10, 5))
date_btn.pack(pady=20, padx=20)

# Frame 3
frame3 = Frame(root, height=120)
frame3.pack(fill="x", padx=10, pady=45)

# Textbox to display result
textbox_age = Text(frame3, height=3.5, wrap="word", font=("Arial", 18, "bold"))
textbox_age.pack(fill='x', expand=True, ipadx=5, ipady=5)

root.mainloop()
