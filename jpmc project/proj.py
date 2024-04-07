import pytesseract as tess
import pyttsx3
from PIL import Image
import pathlib
import os
import pyautogui
import time
import keyboard
from summary import *
screenshot_path = "screenshots/"

tess.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Set the path where you want to save the screenshots
if not os.path.exists(screenshot_path):
    os.makedirs(screenshot_path)
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)
recognized_path = os.path.join(os.getcwd(), "Recognized")
if not os.path.exists(recognized_path):
    os.makedirs(recognized_path)

timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
file_name = os.path.join(recognized_path, f"myfile_{timestamp}.txt")

# f=open(f"Recognized/myfile_{timestamp}.txt","a")


def on_key_press(event):
    if event == '0':
        # print("Stopping the program...")
        keyboard.unhook_all()  # Unhook all keyboard events
        # You can add additional cleanup code here if needed
        # f.close()
        # global X
        X=False
        # print(X)  # Exit the program
    elif event == '2':
        # f.close()
        # time.sleep(2)
        summarize()

        # global X
        X=False



final_text = ""
def textToSpeech(text,path):
    os.remove(path)
    # print(text)
    with open(file_name,"a") as f:
        f.write(text)
    global final_text
    final_text = final_text + text
    engine.say(text)
    time.sleep(1)
    engine.say("If you want me to summarize the information I narrated, press 2")
    engine.say("If you want me to stop narrating press 0")
    
    engine.runAndWait()
    # keyboard.on_press(on_key_press)  # Register the key press event
    ch = None
    while ch not in ('0', '2'):
        ch = input("Enter 0 to stop or 2 to summarize: ")
        if ch not in ('0', '2'):
            print("Invalid choice. Please enter either 0 or 2.")

    if ch == '0':
        on_key_press('0')
    elif ch == '2':
        on_key_press('2')
def imgToText():
    desktop=pathlib.Path(os.getcwd())
    for path in desktop.iterdir():
        img=Image.open(path)
        text1=tess.image_to_string(img)
        text=text1.splitlines()
        textToSpeech(" ".join(text),path)

def take_screenshot_of_active_app():
    screen_width, screen_height = pyautogui.size()
    active_app_window = pyautogui.getActiveWindow()
    app_x, app_y, app_width, app_height = active_app_window.left, active_app_window.top, active_app_window.width, active_app_window.height

    screenshot = pyautogui.screenshot(region=(app_x, app_y, app_width, app_height))

    timestamp1 = time.strftime("%Y%m%d%H%M%S", time.localtime())
    screenshot.save(f"active_app_screenshot_{timestamp1}.png")
    imgToText()



if __name__ == "__main__":
    X=True
    while X:
        time.sleep(4)
        take_screenshot_of_active_app()
        X=False
