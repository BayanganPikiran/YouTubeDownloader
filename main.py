from tkinter import *
from tkinter import filedialog
from pytube import YouTube


root = Tk()
root.geometry("300x250")
root.title("YouTube Downloader")

my_link = StringVar()
stream_choice = StringVar()
font = ("Arial", 10, 'bold')



def choose_directory():
    """searches for and sets the output path for the YouTube file download"""
    output_path = filedialog.askdirectory(initialdir="/home/boss_andre/Downloads/")
    video_location = output_path
    my_link.set(video_location)


def create_yt_object():
    """Creates the initial YouTube object with url_entry input"""
    yt = YouTube(url_entry.get(), on_complete_callback=declare_complete(), use_oauth=True, allow_oauth_cache=True)
    return yt


def get_stream():
    """Designates a YouTube object its stream according to the chosen radio button"""
    stream = None
    yt = create_yt_object()
    chosen_stream = stream_choice.get()
    if chosen_stream == "hi_res":
        stream = yt.streams.get_highest_resolution()
    elif chosen_stream == "low_res":
        stream = yt.streams.get_lowest_resolution()
    elif chosen_stream == "audio_only":
        stream = yt.streams.get_audio_only()
    return stream


def declare_complete():
    """Signifies when the download has completed"""
    completion_label["text"] = "Download complete!"


def download():
    """Takes selected YouTube stream and downloads it to the chosen output path"""
    chosen_stream = get_stream()
    chosen_stream.download(filepath_entry.get())


url_label = Label(root, text="YouTube URL", font=font)
url_entry = Entry(root, width=30)

filepath_direction = Label(root, text="Download Filepath", font=font)
filepath_entry = Entry(root, textvariable=my_link, width=30)
filepath_button = Button(text="Filepath", font=font, command=lambda: choose_directory())


rb_frame = Frame(root, width=350, height=80, highlightbackground="black", highlightthickness=1)
rb_label = Label(rb_frame, text="Choose your stream type", font=font)
rb1 = Radiobutton(rb_frame, text="hi-res", value="hi_res", variable=stream_choice,
                  command=lambda: stream_choice.get())
rb2 = Radiobutton(rb_frame, text="low-res", value="low_res", variable=stream_choice,
                  command=lambda: stream_choice.get())
rb3 = Radiobutton(rb_frame, text="audio", value="audio_only", variable=stream_choice,
                  command=lambda: stream_choice.get())
rb_label.grid(row=0, column=0, columnspan=3)
rb1.grid(row=1, column=0, padx=2)
rb2.grid(row=1, column=1, padx=3)
rb3.grid(row=1, column=2, padx=2)


download_button = Button(text="Download", font=font, command=download)

completion_label = Label(text="", font=font)

url_label.pack()
url_entry.pack()
filepath_direction.pack()
filepath_entry.pack()
filepath_button.pack(pady=5)
rb_frame.pack()
download_button.pack(pady=5)
completion_label.pack()

root.mainloop()