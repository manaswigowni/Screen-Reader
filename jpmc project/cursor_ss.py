import pyautogui
import pytesseract
import pyttsx3
import time
import os

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
def create_folder_if_not_exists():
    folder_path = "Cursor_Captures"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def textToSpeech(text):
    # print(text)
    engine.say(text)
    time.sleep(1)
    engine.say("Press q to stop the program")
    engine.runAndWait()

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def select_line_at_mouse_position():
    time.sleep(3)
    mouse_x, mouse_y = pyautogui.position()

    pyautogui.moveTo(0, mouse_y)
    pyautogui.keyDown('shift')
    pyautogui.moveTo(pyautogui.size().width, mouse_y)
    pyautogui.keyUp('shift')

    screenshot = pyautogui.screenshot()
    capture_region = (0, mouse_y - 50, pyautogui.size().width, mouse_y + 250)
    captured_image = screenshot.crop(capture_region)
    detected_text = pytesseract.image_to_string(captured_image)
    
    
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    captured_image.save(f"Cursor_Captures/active_app_screenshot_{timestamp}.png")
    
    # print(detected_text)
    textToSpeech(detected_text)

if __name__ == "__main__":

    create_folder_if_not_exists()
    select_line_at_mouse_position()
