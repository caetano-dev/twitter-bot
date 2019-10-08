from pyautogui import click, locateOnScreen, locateAllOnScreen, scroll
from time import sleep

# Dark Mode

def seguir():
    for location in locateAllOnScreen('./seguir.png', confidence=0.85):
        click(location)
        sleep(1)

    scroll(-200)
    seguir()


def deseguir():
    for location in locateAllOnScreen('./deseguir.png', confidence=0.85):
        click(location)
        sleep(1)
        click(locateOnScreen('./confirm.png', confidence=0.9))
        sleep(1)

    scroll(-200)
    deseguir()
