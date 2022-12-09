from tkinter import *
from tkinter import ttk
import random
from BubbleSort import bubble_sort
from SelectionSort import seletion_sort
from InsertionSort import insertion_sort

LABEL_FONT = ("new roman", 16, "italic bold")
LABEL_BG = "#05897A"
LABEL_WIDTH = 15
LABEL_TEXT_COLOR = "#E5BA73"
COMBOBOX_WIDTH = 20
COMBOBOX_FONT = ("new roman", 20, "italic")
ALGORITHMS = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
BUTTON_FONT = ("new roman", 16, "italic bold")
BUTTON_BG_P = "#251749"
BUTTON_BG_A = "#7F167F"
SCALE_FONT = ("new roman", 16, "italic bold")
CANVAS_BG = "#CCD6A6"
DATA_COLOR = "#FF9E9E"
data = []

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("1080x800+400+150")
root.config(bg="#C58940")


def draw_rects(loc_data):
    canvas.delete("all")
    canvas_height = 570
    canvas_width = 1050
    x_width = canvas_width / (len(loc_data) + 1)
    normalized = [i / max(loc_data) for i in loc_data]

    for i, height in enumerate(normalized):
        x0 = i * x_width
        y0 = canvas_height - height * 550
        x1 = (i + 1) * x_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=DATA_COLOR)
    root.update_idletasks()


def generate_random():
    global data
    sizevalue = int(sizescale.get())
    data = []
    for i in range(sizevalue):
        data.append(random.randrange(1, 201))
    draw_rects(data)


def start_sorting():
    global data
    if algorithm_menu.get() == "Bubble Sort":
        bubble_sort(data, draw_rects, speedscale.get())
    if algorithm_menu.get() == "Selection Sort":
        seletion_sort(data, draw_rects, speedscale.get())
    if algorithm_menu.get() == "Insertion Sort":
        insertion_sort(data, draw_rects, speedscale.get())


# Labels,Buttons,Combobox

# Algorithm Label
alg_label = Label(root, text="Algorithm", font=LABEL_FONT, bg=LABEL_BG, width=LABEL_WIDTH,
                  fg=LABEL_TEXT_COLOR, relief="ridge")
alg_label.place(x=0, y=0)

# Algorithm Menu
selected_alg = StringVar()
algorithm_menu = ttk.Combobox(root, width=COMBOBOX_WIDTH, font=COMBOBOX_WIDTH,
                              textvariable=selected_alg, values=ALGORITHMS)
algorithm_menu.place(x=0, y=50)
algorithm_menu.current(0)  # Default Bubble Sort

# Size Label and Scale
sizelabel = Label(root, text="Size", font=LABEL_FONT, bg=LABEL_BG, width=LABEL_WIDTH,
                  fg=LABEL_TEXT_COLOR, relief="ridge")
sizelabel.place(x=250, y=0)
sizescale = Scale(from_=10, to=100, resolution=1, orient="horizontal", width=20,
                  font=SCALE_FONT, bg=LABEL_BG, relief="ridge", length=195)
sizescale.place(x=250, y=50)

# Speed Label and Scale
speedlabel = Label(root, text="Speed", font=LABEL_FONT, bg=LABEL_BG, width=LABEL_WIDTH,
                   fg=LABEL_TEXT_COLOR, relief="ridge")
speedlabel.place(x=570, y=0)
speedscale = Scale(from_=1, to=100, resolution=1, orient="horizontal", width=20,
                   font=SCALE_FONT, bg=LABEL_BG, relief="ridge", length=195)
speedscale.place(x=570, y=50)

# Generate Button
button_random = Button(root, text="Generate", bg=BUTTON_BG_P, font=BUTTON_FONT,
                       width=20, activebackground=BUTTON_BG_A, relief="groove",
                       command=generate_random)
button_random.place(x=795, y=150)

# Start Button

button_start = Button(root, text="Start", bg=BUTTON_BG_P, font=BUTTON_FONT,
                      width=20, activebackground=BUTTON_BG_A, relief="groove",
                      command=start_sorting)
button_start.place(x=795, y=100)

# Canvas

canvas = Canvas(width=1050, height=570, bg=CANVAS_BG)
canvas.place(x=10, y=210)

root.mainloop()
