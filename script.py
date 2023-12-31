import pyautogui
import mouse
import keyboard
import time
import os
import logging
import playsound

def quit(event = None):
    os._exit(0)

def click(x, y):
    mouse.move(x, y)
    mouse.click()
    return

def playFile(filename):
    logging.info('Playing %s', filename)
    if (not os.path.exists(filename)):
        logging.info('No such file')
        return
    playsound.playsound(filename)
    return

# check if needed heroes are on the screen
def checkHeroes(winBox, images):
    logging.info('Checking for heroes')
    for image in images:
        logging.info('\t%s', image)
        try:
            pyautogui.locateOnScreen('heroes/' + image, region=winBox, grayscale=True, confidence=0.8)
            logging.info('\t\tFound')
        except pyautogui.ImageNotFoundException:
            logging.info('\t\tNot found')
            return False
        
    logging.info('All heroes were found')
    return True

# set quit on 'q' key
keyboard.on_press_key('q', quit)

# set logger
logging.basicConfig(filename='trace.log', filemode='w', format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.INFO, encoding='utf-8')

# first click
print('Waiting for first click...')
logging.info('Waiting for first click')
mouse.wait(button=mouse.LEFT, target_types=mouse.DOWN)
x1, y1 = pyautogui.position()
logging.info('First click position: %s', (x1, y1))
color1 = pyautogui.pixel(x1, y1)
logging.info('First click color: %s', color1)

# second click
print('Waiting for second click...')
logging.info('Waiting for second click')
mouse.wait(button=mouse.LEFT, target_types=mouse.DOWN)
x2, y2 = pyautogui.position()
logging.info('Second click position: %s', (x2, y2))

# third click
print('Waiting for third click...')
logging.info('Waiting for third click')
mouse.wait(button=mouse.LEFT, target_types=mouse.DOWN)
x3, y3 = pyautogui.position()
logging.info('Third click position: %s', (x3, y3))

print('Bot is running...')
# get active window
win = pyautogui.getActiveWindow()
winBox = (max(0, win.box[0]), max(0, win.box[1]), win.box[2], win.box[3])
logging.info('Active window title: "%s"', win.title)
logging.info('Active window area: %s', winBox)

# scan all image names from 'heroes' directory
if not os.path.exists('heroes'):
    logging.error('"heroes" directory is missing!')
    exit(1)

files = os.listdir('heroes')
images = []
for file in files:
    if file.endswith('.png'):
        images.append(file)
logging.info('Scanned images: %s', images)

# main loop
terminate = False
while not terminate:
    # wait for first button to be available
    logging.info('Waiting for first button to appear')
    while not pyautogui.pixelMatchesColor(x1, y1, color1, tolerance=3):
        time.sleep(0.1)
    terminate = checkHeroes(winBox, images)
    if terminate:
        break;
    click(x1, y1)
    logging.info('Clicked at first button')
    time.sleep(2)
    click(x2, y2)
    logging.info('Clicked at second button')
    time.sleep(0.8)
    click(x3, y3)
    logging.info('Clicked at third button')

playFile('alert.mp3')
logging.info('Terminating the program')
