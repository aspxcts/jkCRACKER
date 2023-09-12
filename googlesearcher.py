import requests
import pyautogui
import random
import sys
import time
from colorama import Fore

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTCYAN_EX
w = Fore.LIGHTWHITE_EX

def loader():
    l = ['|', '/', '-', '\\']
    for i in l + l + l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Cooking... {i}""")
        sys.stdout.flush()
        time.sleep(0.2)
def createurl():
    from main import key
    from main import engineid
    print(key, engineid)
    url = 'https://www.googleapis.com/customsearch/v1?key='
    url += key
    url += '&cx='
    url += engineid
    url += '&q=words%20that%20have%20'
    print(url)
    return url

def searchandretreive(addon):
    #loader()
    url = createurl()
    url += addon
    useablewords = []
    loweredaddon = addon.lower()
    response = requests.get(url)
    response_json = response.json()
    words = response_json['items'][0]['snippet']
    words = words.split()
    for word in words:
        if word == loweredaddon:
            index = words.index(word)
            words.pop(index)
        if loweredaddon in word:
            useablewords.append(word)
    for word in useablewords:
        if word == loweredaddon:
            index = useablewords.index(word)
            useablewords.pop(index)

    word = random.choice(useablewords)
    interval = random.uniform(0.005,0.01)
    pyautogui.moveTo(810, 1042)
    pyautogui.leftClick()
    for char in word:
        pyautogui.typewrite(char, interval=interval)
        interval = random.uniform(0.005,0.01)
    pyautogui.press('enter')
    print('typed word')

