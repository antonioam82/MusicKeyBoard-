from tkinter import *
from tkinter import ttk
from pydub import AudioSegment
from pydub.generators import Sine, Square, Triangle, Sawtooth, Pulse
from pydub.playback import play
import threading

class m_keyboard():
    def __init__(self):
        self.kb = Tk()
        self.kb.geometry("675x325")
        self.kb.title("Sound Keyboard")
        self.kb.configure(background="gray12")


        self.key1 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(261))
        self.key1.place(x=15,y=150)
        self.key2 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(293))
        self.key2.place(x=96,y=150)
        self.key3 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(329))
        self.key3.place(x=177,y=150)
        self.key4 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(349))
        self.key4.place(x=258,y=150)
        self.key5 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(391))
        self.key5.place(x=339,y=150)
        self.key6 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(440))
        self.key6.place(x=420,y=150)
        self.key7 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(493))
        self.key7.place(x=501,y=150)
        self.key8 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(522))
        self.key8.place(x=582,y=150)

        self.kb.mainloop()

    def make_tone(self):
        tone = Sine(self.freq).to_audio_segment(duration=2000)
        play(tone)

    def init_task(self,n):
        self.freq = n
        t = threading.Thread(target=self.make_tone)
        t.start()

if __name__=="__main__":
    m_keyboard()
