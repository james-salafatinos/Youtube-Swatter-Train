import pyautogui
import os
import time


def data_set_creator():
    cwd = os.getcwd()
    if not (os.path.exists(cwd + "/images")):
        os.mkdir(cwd + "/images")
    os.chdir(cwd + "/images")

    for i in range(200):
        pyautogui.screenshot("image" + str(i) + ".png",
                             region=(0, 0, pyautogui.size()[0], pyautogui.size()[1]))
        time.sleep(1)


def main():
    data_set_creator()


if __name__ == '__main__':
    main()
