import pyautogui
import random
import sys
import time
import re
from colorama import Fore

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


def searchandretreive(addon):
    loweredaddon = addon.lower()
    from main import word_dict
    found_words = [word for word in word_dict if re.search(loweredaddon, word)]
    word = random.choice(found_words)

    if loweredaddon in word:
        wordindex = found_words.index(word)
        interval = float(0.0006)
        pyautogui.moveTo(810, 1042)
        pyautogui.leftClick()
        #pyautogui.write(word)
        for char in word:
            pyautogui.typewrite(char, interval=interval)
            interval = float(0.0005)
        pyautogui.press('enter')
        found_words.pop(wordindex)
    else:
        wordindex = found_words.index(word)
        found_words.pop(wordindex)
        searchandretreive(addon)
