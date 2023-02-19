from ultralytics import YOLO
import time
from PIL import ImageGrab
import pyautogui
import sys

cls = ["Youtube_logo"]
region = [0, 0, pyautogui.size()[0], pyautogui.size()[1]]


def load_model(mp="./best.pt"):
    model = YOLO(mp)
    return model


def parse_results(result):
    r = result[0]
    res = r.boxes
    print("Number of objects detected: ", len(res))

    output = []
    if len(res) > 0:
        print("boxes array", res.xywh)
        print("cls array", res.cls)
        print("conf array", res.conf)
        output.append([res.xywh, res.cls, res.conf])
    else:
        print("No objects detected")

    return output


def contains_youtube(output):
    if len(output) > 0:
        return True
    else:
        return False


def close_chrome():
    if len(pyautogui.getWindowsWithTitle("Google")) == 0:
        print("Chrome is not open? Could be IE or Firefox... bruh.")

    else:
        pyautogui.getWindowsWithTitle("Google")[0].activate()
        # close window with pyautogui
        pyautogui.hotkey('alt', 'f4')


def main():
    model = load_model()

    for i in range(100):
        img = ImageGrab.grab([region[0], region[1], region[0] +
                             region[2], region[1] + region[3]])

        results = model.predict(img, conf=0.2)

        output = parse_results(results)

        if contains_youtube(output):
            print("Youtube is open")
            close_chrome()
        else:
            pass
        time.sleep(1.5)


if __name__ == '__main__':
    main()
