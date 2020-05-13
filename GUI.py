import tkinter as tk
import timeit
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
from Image import *

root = tk.Tk()
root.title("SVD Image Compressor")

canvas = tk.Canvas(root, height=30, width=500)
canvas.pack()

frame = tk.Frame(root, bg='#262626')
frame.place(relwidth=500, relheight=10)


def file():
    global my_image
    global my_label
    global my_image_label
    global filename
    root.filename = filedialog.askopenfilename(initialdir="/home/sachin/Videos", title="Select a file", filetypes=(("jpg files", "*.jpg"), ("jpeg files", "*.jpeg")))
    my_label = Label(root, text=root.filename).pack()
    button1.forget()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


def compress():
    
    img = openImage(root.filename)
    start = timeit.default_timer()
    imageWidth = 512
    imageHeight = 512


    singularValuesLimit = 160    # number of singular values to use for reconstructing the compressed image

    aRedCompressed = compressSingleChannel(img[0], singularValuesLimit)
    aGreenCompressed = compressSingleChannel(img[1], singularValuesLimit)
    aBlueCompressed = compressSingleChannel(img[2], singularValuesLimit)

    imr = Image.fromarray(aRedCompressed, mode=None)
    img = Image.fromarray(aGreenCompressed, mode=None)
    imb = Image.fromarray(aBlueCompressed, mode=None)

    newImage = Image.merge("RGB", (imr, img, imb))

    mr = imageHeight
    mc = imageWidth

    originalSize = mr * mc * 3
    compressedSize = singularValuesLimit * (1 + mr + mc) * 3

    stop = timeit.default_timer()

    print('Original size: %d' % originalSize)

    print('Compressed size: %d' % compressedSize)

    print('Ratio compressed size / original size:')
    ratio = compressedSize * 1.0 / originalSize
    print(ratio)

    print('Compressed image size is ' + str(round(ratio * 100, 2)) + '% of the original image ')

    print('Time: ', stop - start)


button1 = tk.Button(root, bg='#262626', fg='black', command=file)
button1.pack(side='top', fill='both')
plusimage = PhotoImage(file="/home/sachin/Downloads/Plus.png")
button1.config(image=plusimage)
size = plusimage.subsample(2, 2)
button1.config(image=size)

button = tk.Button(root, text="compress image", bg='green', font='Helvetica', command=compress)
button.pack(side='bottom', fill='both')

root.mainloop()
