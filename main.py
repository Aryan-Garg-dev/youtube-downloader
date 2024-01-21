from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog


def download_video(url, save_loc):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res = streams.get_highest_resolution()
        highest_res.download(output_path=save_loc)
        print("Video Downloaded Successfully !")

    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("768x1024")
    root.withdraw()

    video_url = simpledialog.askstring(title="Paste Video Link", prompt="Enter URL")
    if video_url:
        save_dir = open_file_dialog()
        if save_dir:
            print("Started download....")
            download_video(video_url, save_dir)
        else:
            print("Invalid Save Location")







