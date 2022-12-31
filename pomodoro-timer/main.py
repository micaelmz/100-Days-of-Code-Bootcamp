from tkinter import *
import sound_effect as fx

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
    global reps
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    verified_label.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        fx.RELAX.play()
        time = long_break_sec
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        fx.RELAX.play()
        time = short_break_sec
        title_label.config(text='Break', fg=PINK)
    else:
        fx.WORK.play()
        title_label.config(text='Work', fg=GREEN)
        time = work_sec

    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer

    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec:0>2}')
    if count > 0:
        timer = root.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_marks = reps // 2
        verified_label.config(text='✔' * check_marks)

# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
icon = PhotoImage(file='img/tomato.png')
root.iconphoto(False, icon)
root.title('Pomodoro')
root.config(padx=50, pady=50, bg=YELLOW)


title_label = Label(text='Timer', font=(FONT_NAME, 50, 'bold'), bg=YELLOW, fg=GREEN)
title_label.config(width=5)
title_label.grid(column=2, row=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='img/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)


star_button_image = PhotoImage(file='img/start_button.png')
start_button = Button(command=start_timer, image=star_button_image, bg=YELLOW, highlightthickness=0, borderwidth=0, activebackground=YELLOW, padx=10)
start_button.grid(column=1, row=3)

reset_button_image = PhotoImage(file='img/reset_button.png')
reset_button = Button(command=reset_timer, image=reset_button_image, bg=YELLOW, highlightthickness=0, borderwidth=0, activebackground=YELLOW, padx=10)
reset_button.grid(column=3, row=3)


verified_label = Label(text='', fg=GREEN, bg=YELLOW)
verified_label.grid(column=2, row=4)

root.mainloop()
