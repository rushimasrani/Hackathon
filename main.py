import os
import time
import pyfiglet
import joblib
import sklearn
import sys

def run_PE():
    file = input("Enter the path and name of the file: ")
    os.system("python3 Extract/PE_main.py {}".format(file))

def run_URL():
    os.system('python3 Extract/url_main.py')

def exit_program():
    exit()

def start():
    print(pyfiglet.figlet_format("Malware Detector"))
    print(" Welcome to antimalware detector \n")
    print(" 1. PE scanner")
    print(" 2. URL scanner")
    print(" 3. Exit\n")

    select = int(input("Enter your choice: "))

    if select in [1, 2, 3]:
        if select == 1:
            run_PE()
        elif select == 2:
            run_URL()
        elif select == 3:
            exit_program()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

    choice = input("Do you want to perform another action? (y/n)")
    if choice.lower() == 'y':
        start()
    else:
        exit_program()

if __name__ == "__main__":
    start()
