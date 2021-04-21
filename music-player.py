import pygame.mixer
import tkinter as tk
import sys
import os
import tkinter.filedialog
import webbrowser

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

#ウィンドウを作成
root = tk.Tk()
root.title(u'Neya-Tetsu Music Player')
root.geometry('640x200')
root.resizable(0,0)
#プレーヤーフレーム作成
playerFrame = tk.Frame(root)

#メディアプレーヤー用意
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)

#About Neya-Tetsu Music Player
def openLink(url):
    webbrowser.open(url)
def aboutPlayer():
    aboutWindow = tk.Toplevel(root)
    aboutWindow.resizable(0,0)
    label1 = tk.Label(aboutWindow, text='Credit', font=('',20))
    label1.pack()
    label2 = tk.Label(aboutWindow, text='本ソフトウェアには、 PyGame が含まれています。 PyGame は GNU LGPL v2.1 のもとで配布されています。')
    label2.pack()
    button2 = tk.Button(aboutWindow, text='PyGame Lisence')
    button2.pack()
    button2.bind('<1>', lambda e: openLink('https://www.pygame.org/docs/LGPL.txt'))
    label3 = tk.Label(aboutWindow, text='本ソフトウェアには、 Ionicons が含まれています。 Ionicons は MIT ライセンスのもとで配布されています。')
    label3.pack()
    button3 = tk.Button(aboutWindow, text='Ionicon Lisence')
    button3.pack()
    button3.bind('<1>', lambda e: openLink('https://github.com/ionic-team/ionicons/blob/master/LICENSE'))
    label4 = tk.Label(aboutWindow, text='Neya-Tetsu Music Player は GNU LGPL v2.1 でライセンスされています。', font=('',12,'normal','roman','underline'), fg='blue')
    label4.pack(pady=6)
    label4.bind('<1>', lambda e: openLink('https://github.com/NeyaTetsu/music-player'))
    label5 = tk.Label(aboutWindow, text='Copylight (c) Neya 2021', font=('',20,'bold','italic'))
    label5.pack()
#GUI
buttonAbout = tk.Button(playerFrame, text='About Music Player', command=aboutPlayer)
buttonAbout.pack(fill='x')

#ファイル指定
def fileSelect():
    file_path = tkinter.filedialog.askopenfilename(
        filetypes=[("All Support File", "*.*")],
        title="ファイルを開く",
    )
    if file_path != '':
        pygame.mixer.music.unload()
        pygame.mixer.music.load(file_path)
#GUI
buttonSelect = tk.Button(playerFrame, text="Let's file select!", font=('',42), relief='ridge', command=fileSelect)
buttonSelect.pack(fill='x')

#一時停止中かどうか
pauseNow = False

#再生ボタン
def musicPlay():
    global pauseNow
    if pauseNow:
        pygame.mixer.music.unpause()
        pauseNow = False
    else:
        if loopChecked.get():
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play(0)
playImage = tk.PhotoImage(file=resource_path('./asset/play.png'))
buttonPlay = tk.Button(playerFrame, image=playImage, command=musicPlay)
buttonPlay.pack(side='left', anchor='nw')
#一時停止ボタン
def musicPause():
    global pauseNow
    pygame.mixer.music.pause()
    pauseNow = True
#GUI
pauseImage = tk.PhotoImage(file=resource_path('./asset/pause.png'))
buttonPause = tk.Button(playerFrame, image=pauseImage, command=musicPause)
buttonPause.pack(side='left', anchor='nw')

#停止ボタン
def musicStop():
    global pauseNow
    pygame.mixer.music.stop()
    pauseNow = False
#GUI
stopImage = tk.PhotoImage(file=resource_path('./asset/stop.png'))
buttonStop = tk.Button(playerFrame, image=stopImage, command=musicStop)
buttonStop.pack(side='left', anchor='nw')

#ループボタン
def musicLoop():
    if pygame.mixer.music.get_busy():
        if loopChecked.get():
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play(0)
#GUI
loopImage = tk.PhotoImage(file=resource_path('./asset/refresh-sharp.png'))
loopChecked = tk.BooleanVar()
loopChecked.set(False)
checkLoop = tk.Checkbutton(playerFrame, image=loopImage, var=loopChecked, command=musicLoop)
checkLoop.pack(side='left', anchor='nw')

#音量バー
def musicVolume(self,event=None):
    pygame.mixer.music.set_volume(volumeChange.get()/100)
#GUI
volumeChange = tk.IntVar(value=70)
barVolume = tk.Scale(playerFrame, orient='horizontal', length=1000, width=32, font=('',24), sliderlength=64, var=volumeChange, command=musicVolume)
barVolume.pack(fill='x', side='right')
playerFrame.pack(fill='x')
root.mainloop()
