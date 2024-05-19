from word_base import word_base
import random
from tkinter import Tk, Label, Button, Text, Canvas, WORD, Event, messagebox

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "grey80"
FONT_NAME = "Courier"
global random_word, seconds, words_correct


def reset():
    global random_word, seconds, words_correct
    seconds = 60
    words_correct = 0
    random_word = random.sample(word_base, 100)
    text_field.config(state="normal", bg=GREY)
    text_field.delete("0.0", "end")
    text_field.config(state="disabled", bg=GREY)
    canvas2.itemconfigure(words_typed, text="", fill=GREEN)
    canvas2.itemconfigure(words_to_type, text=random_word[:5], fill="black")


def timer():
    global random_word, seconds
    text_field.config(state="normal", bg="white")
    seconds -= 1
    start_button.config(state="disabled")
    canvas.itemconfig(timer_text, text=f"{seconds}")
    if seconds == 0:
        messagebox.showinfo(title="Your result", message=f"{words_correct} words per minute")
        reset()
        start_button.config(state="normal")
    else:
        canvas.after(1000, timer)


def check(event: Event = None) -> None:
    global words_correct
    text_input = text_field.get("0.0", "end").split()[-1]
    if text_input.lower() == random_word[words_correct]:
        words_correct += 1
        if words_correct <= 4:
            canvas2.itemconfigure(words_typed, text=random_word[0:words_correct], fill=GREEN)
        else:
            canvas2.itemconfigure(words_typed, text=random_word[words_correct-5:words_correct], fill=GREEN)
        canvas2.itemconfigure(words_to_type, text=random_word[words_correct: words_correct+5], fill="black")


window = Tk()
window.title("Typedometer")
window.config(bg=YELLOW)

# info label
label = Label(text="This is Typedometer - a desktop program that tests Your typing speed.\n"
                   "Press start and begin typing (You've got one minute). Good Luck!")
label.config(bg=YELLOW)
label.pack(padx=20, pady=10)

# countdown timer
canvas = Canvas(width=100, height=50, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(50, 25, text="0", fill="black", font=(FONT_NAME, 25, "bold"))
canvas.pack(pady=10)

# correct typed words
canvas2 = Canvas(width=400, height=80, bg=YELLOW, highlightthickness=0)
words_typed = canvas2.create_text(200, 20, text="", fill="black", font=(FONT_NAME, 14, "bold"), width=400)
words_to_type = canvas2.create_text(200, 60, text="", fill="black", font=(FONT_NAME, 14, "bold"), width=400)
canvas2.pack()

# input text field
text_field = Text(height=5, width=52, wrap=WORD)
text_field.bind("<KeyRelease>", check)
text_field.pack(padx=20, pady=10)
reset()

start_button = Button(text="Start", command=timer)
start_button.pack(pady=10)

window.mainloop()
