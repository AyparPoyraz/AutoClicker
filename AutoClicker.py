import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
from colorama import Fore, Style

print(Fore.LIGHTMAGENTA_EX+ "HIGH-CPS = 14 For Limit and write your macro key @By Samuil")

# SETUP FOR MACRO:
mouse = Controller()
clicking = False

cps_limit = 14

KeyAsk = str(input("Your Macro Key: "))
MacroKey = KeyCode(char=KeyAsk)
print("Started")

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(1 / cps_limit)

def toggle_event(key):
    if key == MacroKey:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
