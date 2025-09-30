import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    text.config(text = "Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_button():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_brake_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_brake_sec)
        text.config(text="BREAK" ,fg=RED)
    elif reps % 2 == 0:
        count_down(short_brake_sec)
        text.config(text="BREAK" ,fg=PINK)
    else:
        count_down(work_sec)
        text.config(text="WORK" ,fg=GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_button()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✔"
            check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


text = Label(text="TIMER", fg=GREEN, font=(FONT_NAME,50), bg=YELLOW)
text.grid(row=0,column=1)


canvas = Canvas(width=200,height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111.5, image= tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


button = Button(text="Start", command=start_button, highlightthickness=0)
button.grid(row=2,column=0)
button2 = Button(text="Reset", command=reset_timer, highlightthickness=0)
button2.grid(row=2,column=2)

check = Label(text="",fg=GREEN,bg=YELLOW)
check.grid(row=3,column=1)





window.mainloop()