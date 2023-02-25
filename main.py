from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
tick_mark = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label.config(text="SHORT BREAK", fg=RED)
        count_down(short_break_sec)
    elif reps % 2 == 0:
        label.config(text="LONG BREAK", fg=PINK)
        count_down(long_break_sec)
    else:
        label.config(text="WORK", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
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
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += tick_mark
        check_marks.config(text=tick_mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO TIMER")
window.config(padx=25, pady=25, bg=YELLOW)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(150, 170, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(row=2, column=2)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold") ,fg=GREEN)
label.config(padx=0, pady=0, bg=YELLOW, highlightthickness=0)
label.grid(row=1, column=2)

start = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start.grid(row=3, column=1)

reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset.grid(row=3, column=3)

check_marks = Label( fg=GREEN, bg=YELLOW)
check_marks.grid(row=4, column=2)


window.mainloop()