from tkinter import *
from tkinter import ttk
from pydub import AudioSegment
from pydub.generators import Sine, Square, Triangle, Sawtooth, Pulse
from pydub.playback import play
import threading

class m_keyboard():
    def __init__(self):
        self.kb = Tk()
        self.kb.geometry("1163x325")
        self.kb.title("Sound Keyboard")
        self.kb.configure(background="gray12")

        self.duration = IntVar()
        self.duration.set(1000)
        self.WaveForms = ["Sine","Square","Triangle","Sawtooth","Pulse"]
        validatecommand = self.kb.register(self.valid_duration)

        Label(self.kb,text="DURATION:",bg="gray12",fg="white").place(x=15,y=10)
        Label(self.kb,text="WAVEFORM:",bg="gray12",fg="white").place(x=185,y=10)
        Label(self.kb,text="FADE OUT",bg="gray12",fg="white").place(x=1094,y=10)
        Label(self.kb,text="FADE IN",bg="gray12",fg="white").place(x=1015,y=10)
        Label(self.kb,text="GAIN",bg="gray12",fg="white").place(x=911,y=10)
        Label(self.kb,text="VOLUME",bg="gray12",fg="white").place(x=820,y=10)
        self.durEntry = Entry(self.kb,width=8,textvariable=self.duration,validate="key",validatecommand=(validatecommand, "%S"))
        self.durEntry.place(x=90,y=10)
        self.waveEntry = ttk.Combobox(self.kb,width=9,state='readonly')
        self.waveEntry.place(x=268,y=10)
        self.waveEntry["values"] = self.WaveForms
        self.waveEntry.current(0)
        self.slider = Scale(self.kb,bg="gray12",fg="white",from_=500, to=1)
        self.slider.set(1)
        self.slider.place(x=1102,y=32)
        self.slider2 = Scale(self.kb,bg="gray12",fg="white", from_=500, to=1)
        self.slider2.set(1)
        self.slider2.place(x=1018,y=32)
        self.slider3 = Scale(self.kb,bg="gray12",fg="white",from_=100, to=-100)
        self.slider3.set(0)
        self.slider3.place(x=904,y=32)
        self.slider4 = Scale(self.kb,bg="gray12",fg="white", from_=20, to=0)
        self.slider4.set(0)
        self.slider4.place(x=827,y=32)
        
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
        self.key8 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(523.25))
        self.key8.place(x=582,y=150)
        self.key9 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(587.33))
        self.key9.place(x=663,y=150)
        self.key10 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(659.25))
        self.key10.place(x=744,y=150)
        self.key11 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(698.45))
        self.key11.place(x=825,y=150)
        self.key12 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(783.99))#
        self.key12.place(x=906,y=150)
        self.key13 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(880.00))
        self.key13.place(x=987,y=150)
        self.key14 = Button(self.kb,width=10,height=11,command=lambda:self.init_task(987.76))
        self.key14.place(x=1068,y=150)

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
        self.mkey6 = Button(self.kb,width=5,height=6,bg="black",activebackground="light gray",command=lambda:self.init_task(554.36))
        self.mkey6.place(x=639,y=150)
        self.mkey7 = Button(self.kb,width=5,height=6,bg="black",activebackground="light gray",command=lambda:self.init_task(622.25))
        self.mkey7.place(x=720,y=150)
        self.mkey8 = Button(self.kb,width=5,height=6,bg="black",activebackground="light gray",command=lambda:self.init_task(740.00))
        self.mkey8.place(x=882,y=150)
        self.mkey9 = Button(self.kb,width=5,height=6,bg="black",activebackground="light gray",command=lambda:self.init_task(830.60))
        self.mkey9.place(x=963,y=150)
        self.mkey10 = Button(self.kb,width=5,height=6,bg="black",activebackground="light gray",command=lambda:self.init_task(932.32))
        self.mkey10.place(x=1044,y=150)
        
        self.kb.mainloop()

    def make_tone(self,freq):
        if self.waveEntry.get() == "Sine":
            tone = (Sine(freq).to_audio_segment(duration=int(self.durEntry.get())).fade_out(self.slider.get()).fade_in(self.slider2.get())).apply_gain(self.slider3.get())+self.slider4.get()
        elif self.waveEntry.get() == "Square":
            tone = (Square(freq).to_audio_segment(duration=int(self.durEntry.get())).fade_out(self.slider.get()).fade_in(self.slider2.get())).apply_gain(self.slider3.get())+self.slider4.get()
        elif self.waveEntry.get() == "Triangle":
            tone = (Triangle(freq).to_audio_segment(duration=int(self.durEntry.get())).fade_out(self.slider.get()).fade_in(self.slider2.get())).apply_gain(self.slider3.get())+self.slider4.get()
        elif self.waveEntry.get() == "Sawtooth":
            tone = (Sawtooth(freq).to_audio_segment(duration=int(self.durEntry.get())).fade_out(self.slider.get()).fade_in(self.slider2.get())).apply_gain(self.slider3.get())+self.slider4.get()
        elif self.waveEntry.get() == "Pulse":
            tone = (Pulse(freq).to_audio_segment(duration=int(self.durEntry.get())).fade_out(self.slider.get()).fade_in(self.slider2.get())).apply_gain(self.slider3.get())+self.slider4.get()
        play(tone)

    def valid_duration(self,char):
        return char in "0123456789"

    def init_task(self,fr):
        t = threading.Thread(target=self.make_tone, args=(fr,))
        t.start()

if __name__=="__main__":
    m_keyboard()



