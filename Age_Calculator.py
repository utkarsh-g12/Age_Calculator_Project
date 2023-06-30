#----------------- Modules Imported--------------
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import *
#-------------Create object for tkinter module----------
root = Tk()
#------------Set Window Size-------------
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("%dx%d" % (screen_width, screen_height))
#--------------Fetching Current Date-------------
today_date = datetime.now()
today_date_str = today_date.strftime('%d-%m-%Y')
currentv = StringVar(root, value=today_date_str)
#--------Variables Created----------
yearsentryv=IntVar()
monthsentryv=IntVar()
daysentryv=IntVar()

#-------------Main Window------------
def mainwindow():
    lab = Label(root, text="Age Calculator", font=("Ariel", 40, "bold"), bg="red", padx=500)
    lab.grid(row=0, column=0, columnspan=10)
    lab1=Label(root,text="Current Date",font=("Ariel",30,"bold"))
    lab1.grid(row=1,column=0)
    entry=Entry(root,textvar=currentv,state=DISABLED)
    entry.grid(row=1,column=2)
    lab2=Label(root,text="Date Of Birth",font=("Ariel",30,"bold"))
    lab2.grid(row=2,column=0)
    global entry1
    entry1 = DateEntry(root, date_pattern="DD-MM-YYYY",state="readonly")
    entry1.grid(row=2, column=2)
    entry1.bind("<<DateEntrySelected>>", eventcaptured)
    lab = Label(root, text="Calculated Age", font=("Ariel", 40, "bold"), bg="green", padx=500)
    lab.grid(row=6, column=0, columnspan=10)
    lab1 = Label(root, text="Years",font=("Comic Sans MS",30,"italic"))
    lab1.grid(row=8, column=1)
    yearsentry = Entry(root, textvar=yearsentryv)
    yearsentry.grid(row=9, column=1)
    lab2 = Label(root, text="Months",font=("Comic Sans MS",30,"italic"))
    lab2.grid(row=8, column=3)
    monthsentry = Entry(root, textvar=monthsentryv)
    monthsentry.grid(row=9, column=3)
    lab3 = Label(root, text="Days",font=("Comic Sans MS",30,"italic"))
    lab3.grid(row=8, column=5)
    daysentry = Entry(root, textvar=daysentryv)
    daysentry.grid(row=9, column=5)

#----------Event Occured-------
def eventcaptured(event):
    current = currentv.get()
    dob = str(entry1.get())
    # current Date convert to integer
    global current_day, current_month, current_year
    current_day = int(current[0:2])
    current_month = int(current[3:5])
    current_year = int(current[6:10])

    # dob convert to integer
    global dob_day, dob_month, dob_year
    dob_day = int(dob[0:2])
    dob_month = int(dob[3:5])
    dob_year = int(dob[6:10])

    if dob_year>current_year:
        messagebox.showerror("Error In Selection", "You can't select this year")
        yearsentryv.set("0")
        monthsentryv.set("0")
        daysentryv.set("0")
        removeallwidget()
        mainwindow()
    elif dob_month>current_month:
        if dob_year>=current_year:
            messagebox.showerror("Error In Selection", "Your selection is excedded this current month")
            yearsentryv.set("")
            monthsentryv.set("")
            daysentryv.set("")
            removeallwidget()
            mainwindow()
        else:
            maincalculation()

    elif dob_year==current_year:
        if dob_month>=current_month:

            if dob_day>current_day:
                messagebox.showerror("Error In Selection", "Your selection is exceeded this day")
                yearsentryv.set("0")
                monthsentryv.set("0")
                daysentryv.set("0")
                removeallwidget()
                mainwindow()
            else:
                maincalculation()
        else:
            maincalculation()
    elif dob_year<current_year:
            maincalculation()

#-----------Removing All Widgets--------
def removeallwidget():
    for widget in root.winfo_children():
        widget.grid_remove()
#---------Main Calculation Part----------
def maincalculation():
    current = currentv.get()
    dob = str(entry1.get())
    # current Date convert to integer
    global current_day, current_month, current_year
    current_day = int(current[0:2])
    current_month = int(current[3:5])
    current_year = int(current[6:10])

    # dob convert to integer
    global dob_day, dob_month, dob_year
    dob_day = int(dob[0:2])
    dob_month = int(dob[3:5])
    dob_year = int(dob[6:10])
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if dob_day > current_day:
        current_month = current_month - 1
        current_day = current_day + month[dob_month - 1]
    if dob_month > current_month:
        current_year = current_year - 1
        current_month = current_month + 12
    global ans_year, ans_month, ans_day
    ans_year = current_year - dob_year
    ans_month = current_month - dob_month
    ans_day = current_day - dob_day
    yearsentryv.set(ans_year)
    monthsentryv.set(ans_month)
    daysentryv.set(ans_day)

mainwindow()
mainloop()