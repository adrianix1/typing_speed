from tkinter import Tk, Label, Button, Text, Canvas, WORD

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "grey80"
FONT_NAME = "Courier"


window = Tk()
window.title("Typedometer")
window.config(bg=YELLOW)

# info label
label = Label(text="This is Typedometer - a desktop program that tests Your typing speed.\nPress start and begin typing (You've got one minute). Good Luck!")
label.config(bg=YELLOW)
label.pack(padx=20, pady=10)

# countdown timer
canvas = Canvas(width=100, height=50, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(50, 25, text="0", fill="black", font=(FONT_NAME, 25, "bold"))
canvas.pack(pady=10)

# correct typed words
canvas2 = Canvas(width=400, height=80, bg=YELLOW, highlightthickness=0)
words_typed = canvas2.create_text(200, 20, text="correct word", fill="black", font=(FONT_NAME, 14, "bold"), width=400)
words_to_type = canvas2.create_text(200, 60, text="to type", fill="black", font=(FONT_NAME, 14, "bold"), width=400)
canvas2.pack()

# input text field
text_field = Text(height=5, width=52, wrap=WORD)
text_field.pack(padx=20, pady=10)

start_button = Button(text="Start")
start_button.pack(pady=10)

window.mainloop()
