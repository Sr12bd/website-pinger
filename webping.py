import pyfiglet
import subprocess
import time
import colorama
from colorama import*
text=pyfiglet.figlet_format("website pinger")
print (Fore.BLUE+text)
print("connecting ............")
time.sleep(3)
print(Fore.GREEN+"Enter an IP or Website name ")



i = input()
print(Fore.BLUE+"pinging ................")
time.sleep(2)
print(Fore.BLUE+"reading stats............")
time.sleep(4)

subprocess.call("ping "+ i ,shell=True)
time.sleep(1)

final=pyfiglet.figlet_format("Blue Hat")
print(Fore.BLUE+"""couperation of
"""+final)

