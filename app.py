from tkinter import *
from tkinter import filedialog
from base64 import b16encode
from PIL import ImageTk, Image
import random
from ctypes import windll

root = Tk()


def load_img():
    x = filedialog.askopenfilename()
    pilImg = Image.open(x)
    pilImg = pilImg.resize((400, 400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(pilImg)
    cv_img.configure(image=img)
    cv_img.image = img


def draw_function(event):
    dc = windll.user32.GetDC(0)
    rgb = windll.gdi32.GetPixel(dc, event.x_root, event.y_root)
    r = rgb & 0xff
    red_slider.set(r)
    g = (rgb >> 8) & 0xff
    green_slider.set(g)
    b = (rgb >> 16) & 0xff
    blue_slider.set(b)


def get_rand_color():
    red_slider.set(random.randint(0, 255))
    green_slider.set(random.randint(0, 255))
    blue_slider.set(random.randint(0, 255))


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


def rgb_color(rgb):
    return b'#' + b16encode(bytes(rgb))


def get_color(val):
    x = round(float(val), 0)
    y = int(x)
    return y


def slider_changed(event):
    cv.configure(
        bg=rgb_color((red_slider.get(),
                      green_slider.get(),
                      blue_slider.get()))
    )

    hex_label.configure(
        text="HEX: " + rgb_to_hex((red_slider.get(),
                                   green_slider.get(),
                                   blue_slider.get()))
    )

    rgb_label.configure(
        text="RGB: " + str(red_slider.get()) + ',' + str(green_slider.get()) + ',' + str(blue_slider.get())
    )


red_label = Label(
    root,
    text='value red:'
)

red_slider = Scale(
    root,
    from_=0,
    to=255,
    orient='horizontal',
    command=slider_changed
)

green_label = Label(
    root,
    text='value green:'
)

green_slider = Scale(
    root,
    from_=0,
    to=255,
    orient='horizontal',
    command=slider_changed
)

blue_label = Label(
    root,
    text='value blue:'
)

blue_slider = Scale(
    root,
    from_=0,
    to=255,
    orient='horizontal',
    command=slider_changed
)

cv = Canvas(
    root,
    width=200,
    height=200,
    bg="black"
)

hex_label = Label(
    root,
    text='HEX',
    font=('Courir', 15)
)

rgb_label = Label(
    root,
    text='RGB',
    font=('Courir', 15)
)

btn_rand_color = Button(
    root,
    text="random color",
    command=get_rand_color
)

btn_load_img = Button(
    root,
    text="load img",
    command=load_img
)

cv_img = Label(
    root,
    width=375,
    height=375
)


cv_img.bind("<Button-1>", draw_function)

red_label.place(x=10, y=33, anchor='w')
red_slider.place(x=85, y=25, anchor='w', width=250)

green_label.place(x=10, y=73, anchor='w')
green_slider.place(x=85, y=65, anchor='w', width=250)

blue_label.place(x=10, y=113, anchor='w')
blue_slider.place(x=85, y=105, anchor='w', width=250)

cv.place(x=10, y=250, anchor='w')
cv_img.place(x=400, y=200, anchor='w')

rgb_label.place(x=225, y=200, anchor='w')
hex_label.place(x=225, y=290, anchor='w')

btn_rand_color.place(x=35, y=375, anchor='w')
btn_load_img.place(x=125, y=375, anchor='w')

root.title("Color Picker")
root.geometry("800x400")
root.resizable(False, False)

root.mainloop()