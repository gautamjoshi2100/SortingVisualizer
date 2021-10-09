from QuickSort import quick_sort
from tkinter import *
from tkinter import ttk
import random
from BubbleSort import bubble_sort
from QuickSort import quick_sort

root = Tk()
root.title('Sorting Algorithms Visualiser')
root.maxsize(900, 600)
root.config(bg = 'black')

selected_algo = StringVar()
data = []

def drawData(data, colors):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i *  x_width + offset + spacing
        y0 = c_height - height * 340

        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])
        canvas.create_text(x0 + 1, y0, anchor = SW, text = str(data[i]))
    root.update_idletasks()

def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    data = []
    for x in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data,['red' for x in range(len(data))])

def start_algorithm():
    global data
    if not data:
        return 
    
    if (algMenu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data) - 1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])
    elif (algMenu.get() == 'Bubble Sort'):
        bubble_sort(data, 0, speedScale.get())


UI_frame = Frame(root, width = 600, height = 200, bg = 'grey')
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

canvas = Canvas(root, width = 600, height = 380, bg = 'white')
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

Label(UI_frame, text = "Algorithm: ", bg = 'grey').grid(row = 0, column = 0, padx = 5, sticky = W)
algMenu = ttk.Combobox(UI_frame, textvariable = selected_algo, values = ['Bubble Sort', 'Merge Sort', 'Quick Sort'])
algMenu.grid(row = 0, column = 1, padx = 5, pady = 5)
algMenu.current(0);

speedScale = Scale(UI_frame, from_ = 0.1, to = 2.0, length = 200, digits = 2, resolution = 0.2, orient = HORIZONTAL, label = "Select Speed [s]")
speedScale.grid(row = 0, column = 2, padx = 5, pady = 5)
Button(UI_frame, text = "Start", command = start_algorithm, bg = 'red').grid(row = 0, column = 3, padx = 5, pady = 5)


#Label(UI_frame, text = "Size: ", bg = 'grey').grid(row = 1, column = 0, padx = 5, sticky = W)
sizeEntry = Scale(UI_frame, from_ = 3, to = 25, length = 200, resolution = 1, orient = HORIZONTAL, label = "Select Size")
sizeEntry.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = W)

#Label(UI_frame, text = "Min Value: ", bg = 'grey').grid(row = 1, column = 2, padx = 5, sticky = W)
minEntry = Scale(UI_frame, from_ = 1, to = 10, length = 200, resolution = 1, orient = HORIZONTAL, label = "Select Min Value")
minEntry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

#Label(UI_frame, text = "MaxValue: ", bg = 'grey').grid(row = 1, column = 4, padx = 5, sticky = W)
maxEntry = Scale(UI_frame, from_ = 10, to = 100, length = 200, resolution = 1, orient = HORIZONTAL, label = "Select Max Value")
maxEntry.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = W)

Button(UI_frame, text = "Generate", command = Generate, bg = 'white').grid(row = 1, column = 3, padx = 5, pady = 5)
root.mainloop()