from pyautogui import click, locateOnScreen, locateAllOnScreen, scroll
from time import sleep


def follow():
    for location in locateAllOnScreen('./follow.png', confidence=0.85):
        click(location)
        sleep(1)

    scroll(-200)
    follow()


def unfollow():
    for location in locateAllOnScreen('./unfollow.png', confidence=0.85):
        click(location)
        sleep(1)
        click(locateOnScreen('./confirm.png', confidence=0.9))
        sleep(1)

    scroll(-200)
    unfollow()
