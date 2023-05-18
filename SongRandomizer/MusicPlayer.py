from tkinter import *
from pygame import mixer
import songShuffler
 
start = 1
end = 20

mixer.init()

# function to play a song
def playSong():
    if songShuffler.index >= end - start + 1:
        songShuffler.songs = songShuffler.randomize(start, end)
        songShuffler.index = 0
        print('\n')
    mixer.music.load("./Songs/" + str(songShuffler.songs[songShuffler.index]) + ".mp3")
    print(songShuffler.songs[songShuffler.index])
    song.config(text=str(songShuffler.songs[songShuffler.index]) + ".mp3")
    songShuffler.index += 1
    mixer.music.play()

# GUI
root = Tk()
root.title("Music Player")
root.geometry("330x140+290+85")
root.resizable(False, False)

play = Button(root, text="play", command=playSong, width=10)
n = Button(root, text="next", command=playSong, width=10)
stop = Button(root, text="stop", command=mixer.music.stop, width=10)
pause = Button(root, text="pause", command=mixer.music.pause, width=10)
resume = Button(root, text="resume", command=mixer.music.unpause, width=10)

song = Label(root, text="")

play.grid(row=0, column=1)
resume.grid(row=1, column=0)
pause.grid(row=1, column=2)
n.grid(row=2, column=0)
stop.grid(row=2, column=2)
song.grid(row=3, column=1)

root.update()
root.mainloop()