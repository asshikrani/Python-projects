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

# a = pyjokes.get_jokes()
# print(a)


