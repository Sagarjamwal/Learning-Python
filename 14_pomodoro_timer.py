# My first python gui using tkinter 
# A 25 minute Pomodoro GUI
# tkinter is a built in library to make windows/tiles/buttons
import tkinter as tk
import math
T_MIN=25
def start_timer():
    T_SEC=T_MIN*60
    countdown(T_SEC)
def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        window.after(1000,countdown,count -1)
    else:
        label_title.config(text="Break Time!")
window =tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg="#f7f5dd")

label_title=tk.Label(text="Timer:",fg="#9bdeac", bg="#f7f5dd", font=("Courier", 50))
label_title.pack()

canvas=tk.Canvas(width=300,height=300,bg="#f7f5dd", highlightthickness=0)
timer_text = canvas.create_text(100, 112, text="25:00", fill="#35455D", font=("Courier", 35, "bold"))
canvas.pack()
button_start = tk.Button(text="Start", highlightthickness=0, command=start_timer)
button_start.pack()
window.mainloop()