import tkinter as tk
from tkinter import ttk
import math as math
import time as tm
import threading as thrd


# importing tkinter for GUI
# importing ttk from tkinter. missing GUI pieces
# importing math for the ciel() and floor() function
# importing time for added timer functionality

x = 0
y = 0
z = 0

Total_Seconds = 0

txtTime_Expression = 0


stop = True

def RuneCalculate():
    global x, y, z, Total_Seconds

    x = int(RunesDesired.get())
    y = int(RuneFarm.get())
    z = int(FarmRunTime.get())

    need = x / y                            #  Number of farming loops = Total runes / runes gained per farming loop
    timed = need * z                        #  Total seconds = Number of farming loops * seconds per farming loop
    Total_Seconds = math.ceil(timed)         # round Total seconds up the the nearest whole number

def TimeCalcutaion():
    global txtTime_Expression
    
    
    seconds = Total_Seconds % 60
    minutes = math.floor((Total_Seconds / 60) % 60)
    hours =  math.floor(((Total_Seconds / 60) / 60) % 60)

    print("For the time expression:")
    print("Seconds = " + str(seconds))
    print("Minutes = " + str(minutes))
    print("Hours = " + str(hours))

    txtTime_Expression = f"{hours:02}:{minutes:02}:{seconds:02}"

def DataBox_Voicing():

    DataBox.delete(1.0, "end")
    DataBox.insert(1.0, txtTime_Expression )
    DataBox.insert(1.0, "will take... ")
    DataBox.insert(1.0, "Each loop taking " + str(z) + " seconds ")
    DataBox.insert(1.0, "Makes " + str(math.ceil(x/y)) + " farming loops ")
    DataBox.insert(1.0, "At a rate of " + str(y) + " runes per farming loop ")
    DataBox.insert(1.0, "Gathering " + str(x) + " Runes ")

def RuneMathButton():
    RuneCalculate()
    TimeCalcutaion()
    DataBox_Voicing()

def Stop_Time():
    global stop

    stop = True

def Start_time():

    pass


# GUI instructions


root = tk.Tk()

root.geometry("700x360")
root.title("Rune Calclator")

#Entry frame, intake of details

Entry_Frame = tk.Frame()
Entry_Frame.place(x="20", y="10")



Entry_lbl = tk.Label(Entry_Frame, text="Rune Calculations", font=('papyrus', 20),)
Entry_lbl.grid(row=0, column=0, columnspan=2, pady=5)

Runes_Desired_lbl = tk.Label(Entry_Frame, text="Runes Desired", font=('papyrus', 12))
Runes_Desired_lbl.grid(row=1, column=0, pady=5)

RunesDesired = tk.Entry(Entry_Frame)
RunesDesired.grid(row=1, column=1, padx=10, pady=10)

Rune_Farm_lbl = tk.Label(Entry_Frame, text="Rune Farm", font=('papyrus', 12))
Rune_Farm_lbl.grid(row=2, column=0, pady=5)

# expand later, multiple entites with different rune values

RuneFarm = tk.Entry(Entry_Frame)
RuneFarm.grid(row=2, column=1, pady=5)

Farm_Run_Time_lbl = tk.Label(Entry_Frame, text="Farm Run Time", font=('papyrus', 12))
Farm_Run_Time_lbl.grid(row=3, column=0, pady=5)

FarmRunTime = tk.Entry(Entry_Frame)
FarmRunTime.grid(row=3, column=1, pady=5)

RunMath = tk.Button(Entry_Frame, text="Math", font=("papyrus", 12), command=RuneMathButton )
RunMath.grid(row=5, column=0, columnspan=2, sticky="news", padx=0, pady=25)

# Output frame, post prosscesing knowledge

Results_Frame = tk.Frame()
Results_Frame.place(x=320, y=10)



DataBox = tk.Text(Results_Frame, height=5, width=28, font=("helvetica", 16))
DataBox.grid(row=0, column=0, columnspan=2, padx=10, pady=10,)

STRTtime = tk.Button(Results_Frame, text="Start", font=("papyrus", 12), command=Start_time)
STRTtime.grid(row=1, column=0, sticky = "news", padx=10, pady=10)

STPtime = tk.Button(Results_Frame, text="Stop", font=("papyrus", 12), command=Stop_Time)
STPtime.grid(row=1, column=1, sticky = "news", padx=10, pady=10)

Clock_lbl = tk.Label(Results_Frame, text="00:00:00", font=("papyrus", 28))
Clock_lbl.grid(row=2, column=0, columnspan=2, sticky="news", padx=5, pady=5)



root.mainloop()

print("Test Run")