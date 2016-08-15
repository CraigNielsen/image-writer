import sys
import argparse
# im = Image.open(sys.argv[1])
# im.show()
# print("hello from : ", sys.argv[0])
def rma_sheet(*args):
    header= 'from PIL import ImageFont, ImageDraw, Image\n'
    importt = 'im = Image.open(argv[1]).convert("RGBA")'
    font = 'font = ImageFont.truetype("usr/share/fonts/truetype/freefont/FreeSans.ttf", 35)'
    draw = 'draw = imageDraw(im)'
    text = 'draw.text(({}, {}), argv[{}], font=font, fill=(0, 0, 0, 255))\n'
    rows = ''
    final = 'im.show()'
    y=1
    for i in args:
        rows = rows + text.format(i[0] , i[1], y)
        y+=1
    s = '\n'
    f = s.join((header, importt, font, draw, rows, final))
    return f


from tkinter import *
from tkinter.filedialog import askopenfilename
if __name__ == "__main__":
    root = Tk()
    parser = argparse.ArgumentParser(description="read input")
    parser.add_argument('--f',dest='filename', required=True, help='the filename to use for the generated code')
    args = parser.parse_args()

    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)

    #adding the image
    File = askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
    img = PhotoImage(file=File)
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    #function to be called when mouse is clicked
    allpoints = []
    def printcoords(event):
        #outputting x and y coords to console
        allpoints.append([event.x, event.y])
        print (allpoints)
    #mouseclick event
    canvas.bind("<Button 1>",printcoords)

    root.mainloop()
    print("finished")
    print("writing to file {}".format(args.filename))
    with open(args.filename, 'w') as file:
        for line in rma_sheet(*allpoints):
            file.write(line)
