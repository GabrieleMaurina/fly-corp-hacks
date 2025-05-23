import os.path
import PIL.Image
import pyautogui


DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(DIR, 'images')
CHECK_IMG = os.path.join(IMAGES_DIR, 'check.png')
X_IMG = os.path.join(IMAGES_DIR, 'x.png')
FAST_IMG = os.path.join(IMAGES_DIR, 'fast.png')

check_img = PIL.Image.open(CHECK_IMG)
x_img = PIL.Image.open(X_IMG)
fast_img = PIL.Image.open(FAST_IMG)
images = x_img, check_img, fast_img

def find_images():
    screen = pyautogui.screenshot()
    for image in images:
        try:
            location = pyautogui.locate(image, screen)
        except pyautogui.ImageNotFoundException:
            pass
        else:
            x = location[0] + location[2] // 2
            y = location[1] + location[3] // 2
            return x, y
    return None

def main():
    while True:
        location = find_images()
        if location is not None:
            pyautogui.click(*location)


if __name__ == "__main__":
    main()
