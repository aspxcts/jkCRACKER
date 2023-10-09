from colorama import Fore
import pyautogui
import random
import sys
import time
import re
from scanner import scan

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTCYAN_EX
w = Fore.LIGHTWHITE_EX


def find_words(word_index, letters):
    idx = tuple(sorted(letters))
    return word_index[idx]


def loader():
    l = ['|', '/', '-', '\\']
    for i in l + l + l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Cooking... {i}""")
        sys.stdout.flush()
        time.sleep(0.2)


def searchandretreive(addon, delay):
    loweredaddon = addon.lower()
    from main import word_dict
    found_words = [word for word in word_dict if re.search(loweredaddon, word)]
    word = random.choice(found_words)

    if loweredaddon in word:

        wordindex = found_words.index(word)
        interval = random.randint(1, 10)
        interval = interval / 1000
        pyautogui.moveTo(810, 1042)
        pyautogui.leftClick()
        if delay:
            print("delay")
            for char in word:
                pyautogui.typewrite(char, interval=interval)
                interval = random.randint(1, 10)
                interval = interval / 1000
            pyautogui.press('enter')
        if not delay:
            print("no delay")
            pyautogui.write(word)
            pyautogui.press('enter')
        found_words.pop(wordindex)
    else:
        wordindex = found_words.index(word)
        found_words.pop(wordindex)
        searchandretreive(addon)
