import image_slicer
from PIL import ImageDraw, ImageFont
from tkinter import *
from PIL import ImageTk

canvas = Canvas(width = 1200, height = 1200, bg = 'white')
canvas.pack(expand = YES, fill = BOTH)
tiles = image_slicer.slice('car2.svg', 4, save=False)
h=10
w=10
for i in range(1,5):

    image = PhotoImage(file="1.png")
    canvas.create_image(h, w, image=image)
    h+=100
    w+=100
    #canvas.create_rectangle(h, w, 250, 250, fill='blue')
    print(i)
mainloop()