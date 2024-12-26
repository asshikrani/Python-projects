# This is a very sensitive program.
""" 
Before running this code make sure that qrcode module is installed in your system 
if not then run this command in you terminal or command-prompt;
(i)_For windows:
  pip install tkinter
  pip install pyjokes
(ii)_For macos:
  pip3 install tkinter
  pip3 install py jokes
(iii)_For linux:
  pip3 install tkinter
  pip install pyjokes
"""

"""
You have to set cordinnates(position) accourding to your system.
You can check cordinates by simply using this code:
while True:
    position = pg.position()
    print(position)
"""
import pyautogui as ag
import time
import pyjokes


def send_message(message, times):
    for i in range(times):
        time.sleep(1)
        joke = pyjokes.get_joke()  
        ag.write(joke)
        ag.press('enter')

def open_whatsapp():
    ag.press('win')
    ag.write('whatsapp')
    ag.press('enter')
    time.sleep(5)
    ag.click(220, 219)
    ag.click(768, 991)

def execute():
    times = 15
    open_whatsapp()
    send_message("", times) 

if __name__ == '__main__':
    execute()




