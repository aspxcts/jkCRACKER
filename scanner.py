import easyocr
import mss
import numpy
import pyautogui
from colorama import Fore
import time


reader = easyocr.Reader(['en'])
sep = ""
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTCYAN_EX
w = Fore.LIGHTWHITE_EX
multipler = 1


def set_instant_answer_mode():
    from main import clear
    from main import transition
    from main import hometitle
    from main import credits
    clear()
    transition()
    hometitle()
    credits()
    print(f"""      {y}[{b}-{y}]{w} Instant Answer Mode? (not very legit):           
                        \n          {y}[{w}01{y}]{w} Yes            
                        \n          {y}[{w}02{y}]{w} No                                             
                        \n                                                                     
                        \t\t\t\t\t\t\t\t\t\t\t\t\t""")
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """).lstrip("0")
    if choice == '1':
        delay = False
    elif choice == '2':
        delay = True
    else:
        delay = True

    return delay


def scan():
    print(f"""      {y}[{b}-{y}]{w} Choose Your Resolution:           
            \n          {y}[{w}01{y}]{w} 1920x1080               
            \n          {y}[{w}02{y}]{w} 1920x1200                                             
            \n                                                                     
            \t\t\t\t\t\t\t\t\t\t\t\t\t""")
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """).lstrip("0")
    if choice == '1':
        multipler = 1
    elif choice == '2':
        multipler = 1.111111111111111
    else:
        multipler = 1

    delay = set_instant_answer_mode()

    keywordlocation = {'left': 771, 'top': 543 * multipler, 'width': 100, 'height': 100 * multipler}
    playerturnlocation = {'left': 655, 'top': 1013 * multipler, 'width': 400, 'height': 100 * multipler}
    with mss.mss() as sct:
        while True:
            playerturn = numpy.asarray(sct.grab(playerturnlocation))
            playerturnresult = reader.readtext(playerturn, detail=0)
            joinbutton = sep.join(playerturnresult)
            if joinbutton == "Join game":
                pyautogui.moveTo(810, 1042)
                pyautogui.leftClick()
            if len(playerturnresult) == 0:
                keyword = numpy.asarray(sct.grab(keywordlocation))
                keywordresult = reader.readtext(keyword, detail=0)
                addon = sep.join(keywordresult)
                from googlesearcher import searchandretreive
                searchandretreive(addon, delay)

            time.sleep(0.1)
