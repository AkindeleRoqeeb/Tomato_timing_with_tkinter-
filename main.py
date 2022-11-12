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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

tom_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tom_image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
# label.config(width=10, height=10)
label.grid(column=1, row=0)



button_2 = Button(text="Start", highlightthickness=0)
button_2.grid(column=0, row=3)

button_1 = Button(text="Reset", highlightthickness=0)
button_1.grid(column=2, row=3)

check_mark = Label(text="mark")
check_mark.grid(column=1, row=4)

window.mainloop()