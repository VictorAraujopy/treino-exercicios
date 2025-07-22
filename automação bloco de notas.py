
import pyautogui
import subprocess
import time

sn = str(input("deseja abrir o bloco de notas? (s/n) "))

if sn == "s":
    writ = str(input("escreva o que deseja escrever: "))
    subprocess.Popen(["Notepad.exe"])
    time.sleep(2)
    pyautogui.write(writ, interval=1)
if sn == "n":
    print("ok, até mais")
else:
    print("opção inválida, tente novamente")
    
