import glob
import shutil
import os
from pathlib import Path
from tkinter import *

#Masterfully crafted by Cameron Lewis

root = Tk()
root.title('Copy all PDFs from the selected Directory and Subdirectories')
menu = Menu(root)
root.config(menu=menu)

def displayme():
    labelResult3 = Label(root, text="This program was masterfully crafted by Cameron Lewis.", bg="green", fg="white")
    labelResult3.pack()

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Who made this?", command=displayme)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit)

LabelPrompt = Label(root, text="Paste the source directory path from where you wish the PDFs to be copied:")
LabelPrompt.pack()

LabelPrompt1 = Label(root, text="PLEASE do NOT include spaces or slashes at the end of the directory's path - YOU WILL BREAK IT")
LabelPrompt1.pack()

entryField = Entry(root)
entryField.pack(fill=X,expand = True)

LabelPrompt2 = Label(root, text="Paste the destination directory path to where you wish the PDFs to be copied:")
LabelPrompt2.pack()

entryField1 = Entry(root)
entryField1.pack(fill=X,expand = True)

def mainfunction():
    filepath = entryField.get()
    filetype = r"\**\*.pdf"
    combinedfile = Path(filepath + filetype)
    destinationfile = entryField1.get()
    #print(combinedfile)
    #for f in glob.glob(r"\\Odshumprintfiles\p\printfiles\root\489984_01-02-2019\**\*.pdf", recursive=True):
    for f in glob.glob(r"{}".format(combinedfile), recursive=True):
        shutil.copy(f, r"{}".format(destinationfile))

button1 = Button(root, text="Press this button to copy PDFs from the source directory AND its subdirectories to the destination directory", command=mainfunction)
button1.pack()

root.geometry("650x180")
root.mainloop()
