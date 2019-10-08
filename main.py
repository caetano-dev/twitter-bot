from pyautogui import click, locateAllOnScreen, scroll
from time import sleep

sleep(5)

def seguir():
    for location in locateAllOnScreen('seguir.png', confidence=0.85):
        click(location)
        sleep(1)
    scroll(-200)
    sleep(1)
    seguir()

seguir()
