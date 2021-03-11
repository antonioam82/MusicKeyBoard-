from tkinter import *
from tkinter import ttk
from pydub import AudioSegment
from pydub.generators import Sine, Square, Triangle, Sawtooth, Pulse
from pydub.playback import play
import threading

class m_keyboard():
    def __init__(self):
        self.kb = Tk()
        self.kb.geometry("970x400")
        self.kb.title("Sound Keyboard")

        self.kb.mainloop()

if __name__=="__main__":
    m_keyboard()
