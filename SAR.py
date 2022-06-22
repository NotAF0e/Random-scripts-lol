import keyboard
import pyautogui
import time

print("Press b to begin and q to quit")
keyboard.wait('b')
print("Began")
while True:
    keyboard.press_and_release('ctrl+l')
    pyautogui.write("www.beamng.com/threads/update-speculation-thread.20246/page-5000",
                    interval=0.009)
    keyboard.press_and_release('enter')
    for x in range(10):
        for i in range(100):
            keyboard.press_and_release('down')

        keyboard.press_and_release('ctrl+r')
    time.sleep(3)
