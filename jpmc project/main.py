from proj import *
from cursor_ss import *

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 200)

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

if __name__ == "__main__":
    engine.say("Hey there! I am your personal assistant. How would you like me to help you today?")
    engine.say("If you want me to narrate the whole information on the screen, press 1")
    engine.say("If you want me to narrate a particular line, press 2")
    engine.runAndWait()

    ch = int(input())
    if ch==1:
        X = True
        engine.say("Sure! I will now narrate the whole information on the screen")
        if not os.path.exists("screenshots/"):
            os.makedirs("screenshots/")
        os.chdir("screenshots/")
        keyboard.on_press(on_key_press)
        while X:
            time.sleep(4)
            take_screenshot_of_active_app()
    else:
        engine.say("Sure! I will now narrate the line at which your cursor is pointing")
        create_folder_if_not_exists()
        select_line_at_mouse_position()
