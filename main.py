import sys, time, os, ctypes
from colorama import Fore
from scanner import scan

with open('key.txt', 'r') as f:
    mainkey = f.read()
    print("found key ", mainkey)
with open('id.txt', 'r') as f2:
    mainengineid = f2.read()
    print("found id ", mainengineid)

key = mainkey
engineid = mainengineid

THIS_VERSION = "1.3.0"

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTCYAN_EX
w = Fore.LIGHTWHITE_EX


def hometitle():
    print(f"""\n\n   
                            ██╗██╗  ██╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
                            ██║██║ ██╔╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
                            ██║█████╔╝ ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
                       ██   ██║██╔═██╗ ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
                       ╚█████╔╝██║  ██╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
                        ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                          
                                                                                               \n""".replace('█',
                                                                                                             f'{b}█{y}'))


def loader():
    l = ['|', '/', '-', '\\']
    for i in l + l + l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Cooking... {i}""")
        sys.stdout.flush()
        time.sleep(0.2)


def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - made by aspect")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} - made by aspect\x07")
    else:
        pass


def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n' * 120)
    return


def transition():
    clear()
    loader()
    clear()

def credits():
    print(
        f"""{y}------------------------------------------------------------------------------------------------------------------------\n{w}  ub.com/aspxcts {b}|{w} https://github.com/aspxcts {b}|{w} https://github.com/aspxcts {b}|{w} https://github.com/aspxcts {b}|{w} https://gith\n{y}------------------------------------------------------------------------------------------------------------------------\n""")

string = 'hi'
# hometitle()
# setTitle(string)
# loader()


def main():
    clear()
    setTitle(f"JKCRACK Menu v{THIS_VERSION}")
    hometitle()
    print(f"""      {y}[{b}-{y}]{w} Main Options:           
    \n          {y}[{w}01{y}]{w} Auto Play               
    \n          {y}[{w}02{y}]{w} SOON™️             
    \n          {y}[{w}03{y}]{w} SOON™️             
    \n          {y}[{w}04{y}]{w} SOON™️                                      
    \n          {y}[{w}05{y}]{w} SOON™️                                 
    \n                                                                     
    \t\t\t\t\t\t\t\t\t\t\t\t\t""")
    global choice
    choice = input(f"""{y}[{b}#{y}]{w} Choice: """).lstrip("0")
    if choice == '1':
        transition()
        hometitle()
        credits()
        scan()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} I massacred this tool while trying to fix something, (it dont work).")
        main()
    elif choice == '2':
        transition()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '3':
        transition()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '4':
        transition()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} This tool is under development, so it is not yet usable.")
        main()
    elif choice == '5':
        transition()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} This tool is under development, so it is not yet usable.")

if __name__ == "__main__":
    main()