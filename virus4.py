import tkinter as tk
import random
import pyttsx3
import pyautogui
from pynput import keyboard
import threading



pyautogui.FAILSAFE = False


#Gjentar en melding kontinuerlig
def gjenta_melding():
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)  # Full lyd
    engine.setProperty('rate', 150)    # Vanlig hastighet
    while kjører:
        for _ in range(100):
            engine.say("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        engine.runAndWait()  # Dette må være her – uten det, spilles ikke meldingen




#Starter vinduet og blinking
def start_vindu():
    global vindu
    vindu = tk.Tk()
    vindu.title("Epileptisk vindu")
    vindu.geometry("1920x1080")

    # Function called when user tries to close the window
    def on_close():
        vindu.destroy()  # Close the current window
        start_vindu()    # Reopen it immediately

    # Bind the close event BEFORE mainloop
    vindu.protocol("WM_DELETE_WINDOW", on_close)

    blink()  # Start blinking colors
    vindu.mainloop()  # Start Tkinter loop




#Blinkende farger
farger = ["white", "black"]
def blink():
    if not kjører:
        return
    ny_farge = random.choice(farger)
    vindu.configure(bg=ny_farge)
    vindu.after(20, blink) # Gjentar blinkingen hvert 20. millisekund



#Beveger musen rundt
def beveg_mus():
    while kjører:
        x = random.randint(-500, 500)
        y = random.randint(-500, 500)
        pyautogui.moveRel(x, y, duration=0.05)


#Starter alt
def hoved():
    global kjører
    kjører = True

    threading.Thread(target=gjenta_melding).start()
    threading.Thread(target=start_vindu).start()
    threading.Thread(target=beveg_mus).start()

hoved()
