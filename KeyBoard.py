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

        self.duration = IntVar()
        self.duration.set(1000)
        self.WaveForms = ["Sine","Square","Triangle","Sawtooth","Pulse"]
        validatecommand = self.kb.register(self.valid_duration)

        Label(self.kb,text="DURATION:",bg="gray12",fg="white").place(x=15,y=10)
        Label(self.kb,text="WAVEFORM:",bg="gray12",fg="white").place(x=10,y=40)
        self.durEntry = Entry(self.kb,width=8,textvariable=self.duration,validate="key",validatecommand=(validatecommand, "%S"))
        self.durEntry.place(x=90,y=10)
        self.waveEntry = ttk.Combobox(self.kb,width=8)
        self.waveEntry.place(x=90,y=40)
        self.waveEntry["values"] = self.WaveForms
        self.waveEntry.current(0)
        self.key1 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(261.63))
        self.key1.place(x=15,y=150)
        self.key2 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(293.66))
        self.key2.place(x=96,y=150)
        self.key3 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(329.63))
        self.key3.place(x=177,y=150)
        self.key4 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(349.23))
        self.key4.place(x=258,y=150)
        self.key5 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(392.00))
        self.key5.place(x=339,y=150)
        self.key6 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(440.00))
        self.key6.place(x=420,y=150)
        self.key7 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(493.88))
        self.key7.place(x=501,y=150)
        self.key8 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(522))
        self.key8.place(x=582,y=150)
        self.mkey1 = Button(self.kb,width=5,height=6,bg="black",activebackground="light gray",command=lambda:self.init_task(277.18))
        self.mkey1.place(x=72,y=150)
        self.mkey2 = Button(self.kb,width=5,height=6,bg="black",activebackground="light gray",command=lambda:self.init_task(311.13))
        self.mkey2.place(x=153,y=150)
        self.mkey3 = Button(self.kb,width=5,height=6,bg="black",activebackground="light gray",command=lambda:self.init_task(369.99))
        self.mkey3.place(x=315,y=150)
        self.mkey4 = Button(self.kb,width=5,height=6,bg="black",activebackground="light gray",command=lambda:self.init_task(415.30))
        self.mkey4.place(x=396,y=150)
        self.mkey5 = Button(self.kb,width=5,height=6,bg="black",activebackground="light gray",command=lambda:self.init_task(466.16))
        self.mkey5.place(x=477,y=150)
        
        self.kb.mainloop()

    def make_tone(self):
        if self.waveEntry.get() == "Sine":
            tone = Sine(self.freq).to_audio_segment(duration=int(self.durEntry.get()))
        elif self.waveEntry.get() == "Square":
            tone = Square(self.freq).to_audio_segment(duration=int(self.durEntry.get()))
        elif self.waveEntry.get() == "Triangle":
            tone = Triangle(self.freq).to_audio_segment(duration=int(self.durEntry.get()))
        elif self.waveEntry.get() == "Sawtooth":
            tone = Sawtooth(self.freq).to_audio_segment(duration=int(self.durEntry.get()))
        elif self.waveEntry.get() == "Pulse":
            tone = Pulse(self.freq).to_audio_segment(duration=int(self.durEntry.get()))
        play(tone)

    def valid_duration(self,char):
        return char in "0123456789"

    def init_task(self,n):
        self.freq = n
        t = threading.Thread(target=self.make_tone)
        t.start()

if __name__=="__main__":
    m_keyboard()

