import easyocr
import mss
import numpy
from colorama import Fore
import time

reader = easyocr.Reader(['en'])
sep = ""
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTCYAN_EX
w = Fore.LIGHTWHITE_EX
multipler = 1

def scan():
    print(f"""      {y}[{b}-{y}]{w} Choose Your Resolution:           
    \n          {y}[{w}01{y}]{w} 1920x1080               
    \n          {y}[{w}02{y}]{w} 1920x1200                                             
    \n                                                                     
    \t\t\t\t\t\t\t\t\t\t\t\t\t""")
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """).lstrip("0")
    if choice == '1':
        multipler = 1
        print(multipler)
    elif choice == '2':
        multipler = 1.111111111111111
        print(multipler)
    else:
        multipler = 1
    keywordlocation = {'left': 771, 'top': 543*multipler, 'width': 100, 'height': 100*multipler}
    playerturnlocation = {'left': 655, 'top': 1013*multipler, 'width': 400, 'height': 100*multipler}
    with mss.mss() as sct:
        while True:
            keyword = numpy.asarray(sct.grab(keywordlocation))
            keywordresult = reader.readtext(keyword, detail=0)
            playerturn = numpy.asarray(sct.grab(playerturnlocation))
            playerturnresult = reader.readtext(playerturn, detail=0)
            addon = sep.join(keywordresult)
            if len(playerturnresult) == 0:
                print("found addon ", addon)
                from googlesearcher import searchandretreive
                searchandretreive(addon)


            time.sleep(2)