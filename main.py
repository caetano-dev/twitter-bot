from sys import argv
from time import sleep

from pyautogui import click, locateOnScreen, locateAllOnScreen, scroll


def follow() -> None:
    running = 0

    while running < 5:
        locations = list(locateAllOnScreen(
            './img/follow.png', confidence=0.8))

        if not locations:
            running += 1

        for location in locations:
            click(location)

            sleep(1)
        scroll(-200)


def unfollow() -> None:
    running = 0

    while running < 5:
        locations = list(locateAllOnScreen(
            './img/unfollow.png', confidence=0.85))

        if not locations:
            running += 1

        for location in locations:
            click(location)
            sleep(1)

            click(locateOnScreen('./img/confirm.png', confidence=0.9))

            sleep(1)
        scroll(-200)


def main():
    if argv[1] == 'follow':
        follow()

    elif argv[1] == 'unfollow':
        unfollow()

    else:
        print("Wrong argument (follow/unfollow).\nRead the README for more information.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    except IndexError:
        print("Missing argument (follow/unfollow).\nRead the README for more information.")
