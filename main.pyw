from pytube import YouTube
import os
import sys
import ffmpy
from tkinter import *
import threading

def best_video():
	res = ["1440p", "1080p", "720p", "480p", "360p", "240p"]
	fps = [60, 30]
	for i in res:
		for j in fps:
			try:
				yt.streams.filter(adaptive=True, res=i, fps=j).first().download(filename="video")
				dl = True
				break
			except:
				dl = False
		if dl:
			break

def best_audio():
	yt.streams.get_audio_only().download(filename="audio")

def merge():
	title = ""
	for j in yt.title:
		if j == "\"" or j == "/" or j == "\\" or j == "*" or j == "?" or j == "<" or j == ">" or j == "|"or j == ":":
			title = title + " "
		else:
			title = title + j
	ff = ffmpy.FFmpeg(
	inputs={"video.mp4": None, "audio.mp4":None},
	outputs={title + ".mp4": None}
	)
	ff.run()

def video_download():
	b1["state"]="disabled"
	global yt
	yt = YouTube(e.get())
	best_video()
	best_audio()
	merge()
	os.remove(r"audio.mp4")
	os.remove(r"video.mp4")
	b1["state"]="normal"



def audio_download():
	b2["state"]="disabled"
	yt = YouTube(e.get())
	yt.streams.get_audio_only().download(filename="pure_audio")
	
	title = ""
	for j in yt.title:
		if j == "\"" or j == "/" or j == "\\" or j == "*" or j == "?" or j == "<" or j == ">" or j == "|"or j == ":":
			title = title + " "
		else:
			title = title + j
	ff = ffmpy.FFmpeg(
	inputs={"pure_audio.mp4": None},
	outputs={title + ".mp3": None}
	)
	ff.run()
	
	os.remove(r"pure_audio.mp4")
	b2["state"]="normal"


root = Tk()
root.title("YouTube Downloader")
root.resizable(width=False, height=False)
root.geometry("200x50")
root.iconbitmap(r"ressources\yt.ico")

e = Entry(root)
e.grid(row=0, column=0, columnspan=4)

t1 = threading.Thread(target=video_download)
t2 = threading.Thread(target=audio_download)

b1 = Button(root, text="Video Download", command=t1.start)
b1.grid(row=1, column=1)
b2 = Button(root, text="Audio Download", command=t2.start)
b2.grid(row=1,column=2)
root.mainloop()