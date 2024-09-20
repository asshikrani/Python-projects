# import pyautogui as pg


# i = 0 
# pg.sleep(3)

# while i < 9 :
#     pg.write('hello brother')
#     pg.press('enter')
#     i += 1




# import pyautogui
# import time

# for i in range(10):
#     print('heloo')



# # while True:
# #     a = pyautogui.position()
# #     print(a)

# def send_whatsapp_message(message):
#     # Open WhatsApp
#     pyautogui.press('win')
#     pyautogui.write('whatsapp')
#     pyautogui.press('enter')


#     time.sleep(5)

#     # Click on the search bar
#     # pyautogui.click(350, 120)

#     # # Enter the phone number
#     # pyautogui.write(phone_number)

#     pyautogui.click(220, 219)

#     pyautogui.click(768,991)

#     pyautogui.write(message)


#     def message():
#         for i in range(10):
#             print('hello')

#     pyautogui.press('enter')

# phone_number = '+923026762926'



# send_whatsapp_message(message())


# import pyautogui as ag
# import time

# def mess():
#     for i in range(100):
#         print('hello')

# def printer():
#     ag.press('win')
#     ag.write('whatsapp')
#     ag.press('enter')

#     time.sleep(5)

#     ag.click(220, 219)
#     ag.click(768,991)
#     ag.write(mess)
#     ag.press('enter') 

# printer()



# import pyautogui as ag
# import time
# import pyjokes

# def send_message(message, times):
#     for i in range(times):
#         time.sleep(3)
#         ag.write(message)
#         ag.press('enter')


# def open_whatsapp():
#     ag.press('win')
#     ag.write('whatsapp')
#     ag.press('enter')
#     time.sleep(5)
#     ag.click(220, 219)
#     ag.click(768, 991)


# def execute():
#     # message = 'hello'
#     message = pyjokes.get_joke()
#     times = 10
#     open_whatsapp()
#     send_message(message, times)

# if __name__ == '__main__':
#     execute()





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


