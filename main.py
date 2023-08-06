import os
import time
import subprocess
import webbrowser

def run(self, cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

time.sleep(2)
print(" ")
print("Activation list:")
print(" ")
print(" ")
time.sleep(0.5)
print("1. Windows / Office Activator - credit to massgravel")
time.sleep(1)
print("| 1.1 - Open the activator")
time.sleep(0.5)
print("| 1.2 - Go to the developer's GitHub site of this tool")
print(" ")
time.sleep(0.5)
print("2. IDM (Internet Download Manager) Activator - credit to lstprjct")
time.sleep(1)
print("| 2.1 - Open the activator")
time.sleep(0.5)
print("| 2.2 - Go to the developer's GitHub site of this tool")


choice = input("-- Enter your choice: ")

if choice == "1.1":
    subprocess.Popen(["powershell","irm https://massgrave.dev/get | iex"])

if choice == "1.2":
    webbrowser.open("https://github.com/massgravel/Microsoft-Activation-Scripts")

#-----------------------------------

if choice == "2.1":
    subprocess.Popen(["powershell", "iwr -useb https://raw.githubusercontent.com/lstprjct/IDM-Activation-Script/main/IAS.ps1 | iex"])

if choice == "2.2":
    webbrowser.open("https://github.com/lstprjct/IDM-Activation-Script")