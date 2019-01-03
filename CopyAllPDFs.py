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

LabelPrompt = Label(root, text="Paste the directory path from where you wish the PDFs to be copied:")
LabelPrompt.pack()

LabelPrompt1 = Label(root, text="PLEASE do NOT include spaces or slashes at the end of the directory's path - YOU WILL BREAK IT")
LabelPrompt1.pack()

entryField = Entry(root)
entryField.pack(fill=X,expand = True)

def mainfunction():
    filepath = entryField.get()
    filetype = r"\**\*.pdf"
    combinedfile = Path(filepath + filetype)
    #print(combinedfile)
    #for f in glob.glob(r"\\Odshumprintfiles\p\printfiles\root\489984_01-02-2019\**\*.pdf", recursive=True):
    for f in glob.glob(r"{}".format(combinedfile), recursive=True):
        shutil.copy(f, r"\\odslapitstop\PitStop_Hotfolders\Detects Blank Pages\Input Folder")

buttoncrud = Button(root, text="Press this button to copy PDFs from the given directory AND the subdirectories to the Humana hotfolder", command=mainfunction)
buttoncrud.pack()

root.geometry("650x120")
root.mainloop()
