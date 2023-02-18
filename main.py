from tkinter import *
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.geometry("400x300")

my_link = StringVar()
stream_choice = StringVar()


def choose_directory():
    output_path = filedialog.askdirectory()
    video_location = output_path
    my_link.set(video_location)


# def download():
#     yt = YouTube(url_entry.get())
#     stream = yt.streams.get_audio_only()
#     stream.download(filepath_entry.get())
def create_yt_object():
    yt = YouTube(url_entry.get())
    print(f"Step 1 is working: {url_entry.get()}")
    return yt


def get_hi_res_stream():
    yt = create_yt_object()
    stream = yt.streams.get_highest_resolution()
    return stream


def get_low_res_stream():
    yt = create_yt_object()
    stream = yt.streams.get_lowest_resolution()
    return stream


def get_audio_stream():
    yt = create_yt_object()
    stream = yt.streams.get_audio_only()
    return stream

# def activate_stream():
#     stream = create_yt_object()
#     if stream_choice == "high_res":
#         print("hi-res stream")
#         return stream.streams.get_highest_resolution()
#     elif stream_choice == "low_res":
#         print("low-res stream")
#         return stream.streams.get_lowest_resolution()
#     elif stream_choice == "audio_only":
#         print("audio stream")
#         return stream.streams.get_audio_only()


def download():
    chosen_stream = stream_choice.get()
    if chosen_stream == "hi_res":
        stream = get_hi_res_stream()
        stream.download(filepath_entry.get())
    elif chosen_stream == "low_res":
        stream = get_low_res_stream()
        stream.download(filepath_entry.get())
    elif chosen_stream == "audio_only":
        stream = get_audio_stream()
        stream.download(filepath_entry.get())


url_label = Label(root, text="YouTube URL")
url_entry = Entry(root)

filepath_direction = Label(root, text="Download Filepath")
filepath_entry = Entry(root, textvariable=my_link)
filepath_button = Button(text="filepath", command=lambda: choose_directory())


rb_frame = Frame(root, width=350, height=80)
rb1 = Radiobutton(rb_frame, text="hi-res", value="high_res", variable=stream_choice,
                  command=lambda: stream_choice.get())
rb2 = Radiobutton(rb_frame, text="low-res", value="low_res", variable=stream_choice,
                  command=lambda: stream_choice.get())
rb3 = Radiobutton(rb_frame, text="audio", value="audio_only", variable=stream_choice,
                  command=lambda: stream_choice.get())
rb1.grid(row=0, column=0)
rb2.grid(row=0, column=1)
rb3.grid(row=0, column=2)

download_button = Button(text="download", command=download)

url_label.pack()
url_entry.pack()
filepath_direction.pack()
filepath_entry.pack()
filepath_button.pack()
rb_frame.pack()
download_button.pack()

root.mainloop()