from pathlib import WindowsPath
import os
from tkinter import *
from pytube import *

root = Tk()
root.geometry('500x300')
root.resizable(500, 300)
root.title("Ninde achande pen drive")

label = Label(root, text= "Youtube best video downloader")
label.pack()

link = StringVar()

linklabel = Label(root, text= "Paste link here", textvariable= link)
linklabel.place(x = 160, y = 60)
link_enter = Entry(root, width= 70, textvariable= link).place(x= 32, y= 90)
def VideoDownloader():
    yt = YouTube(str(link.get()))
    video = yt.streams.get_by_resolution("720p")
    video.download(str(os.path.join(WindowsPath.home(), "Downloads")))
    completelabel = Label(root, text="Downloaded", font="arial 20 bold")
    completelabel.place(x = 180, y = 210)

def AudioDownloader():
    yt = YouTube(str(link.get()))
    audio = yt.streams.get_audio_only()
    audio.download()    
    completelabel = Label(root, text="Downloaded", font="arial 20 bold")
    completelabel.place(x = 180, y = 210)

clickbutton = Button(root, text="Download Video", font="arial 20 bold", bg='blue', padx= 2, command= VideoDownloader)
clickbuttonaudio = Button(root, text="Download Audio", font="arial 20 bold", bg="blue", padx= 2,command=AudioDownloader )
clickbutton.place(x = 180, y = 150)
clickbuttonaudio.place(x = 180, y = 250)
root.mainloop()


