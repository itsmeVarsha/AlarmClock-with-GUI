import tkinter as tk
from tkinter import messagebox
import datetime
import time
import winsound

def set_alarm():
    alarm_time=entry.get()
    try:
        alarm_time=datetime.datetime.strptime(alarm_time,"%H:%M")
        current_time=datetime.datetime.now().strftime("%H:%M")
        while current_time!=alarm_time.strftime("%H:%M"):
            current_time=datetime.datetime.now().strftime("%H:%M")
            time.sleep(1)
        play_alarm_sound()
        messagebox.showinfo("Alarm","Wake Up!!")
    except ValueError:
        messagebox.showerror("Error,Invalid time format! please use HH:MM")

def play_alarm_sound():
    frequency=2500
    duration=2000
    winsound.Beep(frequency,duration)

window=tk.Tk()
window.title("Alarm Clock")
window.geometry("500x300")
window.configure(bg="#C0C0C0")

label=tk.Label(window,text="Enter alarm time (HH:MM) :",font=("Arial",15),bg="#007FFF")
label.pack(pady=10)

entry=tk.Entry(window,font=("Helevetica",14))
entry.pack(pady=10)

button=tk.Button(window,text="Set Alarm",command=set_alarm,font=("Arial",14),bg="#4CAF50",fg="white",relief="raised")
button.pack(pady=10)

window.mainloop()
