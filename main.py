from tkinter import *
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.geometry("300x300")

my_link = StringVar()


def choose_directory():
    output_path = filedialog.askdirectory()
    video_location = output_path
    my_link.set(video_location)


def download():
    yt = YouTube(url_entry.get())
    stream = yt.streams.get_audio_only()
    stream.download(filepath_entry.get())


url_label = Label(root, text="YouTube URL")
url_entry = Entry(root)

filepath_direction = Label(root, text="Download Filepath")
filepath_entry = Entry(root, textvariable=my_link)
filepath_button = Button(text="filepath", command=lambda: choose_directory())

download_button = Button(text="download", command=download)

url_label.pack()
url_entry.pack()
filepath_direction.pack()
filepath_entry.pack()
filepath_button.pack()
download_button.pack()

root.mainloop()