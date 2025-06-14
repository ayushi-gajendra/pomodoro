from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0  # Count of completed sessions

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the timer for work/break sessions depending on the cycle."""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Runs the countdown on screen and updates every second."""
    if count >= 0:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec <= 9:
            count_sec = f"0{count_sec}"

        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick.config(text="✔️")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas with Tomato Image and Timer Text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Timer Title Label
timer = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN, highlightthickness=0)
timer.grid(row=0, column=1)

# Start Button
start = Button(text="Start", fg=PINK, highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

# Reset Button (not yet functional)
reset = Button(text="Reset", fg=PINK, highlightthickness=0)
reset.grid(row=2, column=2)

# Tick Mark Label
tick = Label(font=(FONT_NAME, 30), bg=YELLOW, fg=GREEN, highlightthickness=0)
tick.grid(row=3, column=1)

window.mainloop()
