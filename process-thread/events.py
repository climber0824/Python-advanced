import threading
import time
from tkinter.tix import Tree

"""
### event practice
event = threading.Event()

def func():
    print("Waiting for event to triger\n")
    event.wait()
    print("Perfoming some actions\n")

t1 = threading.Thread(target=func)
t1.start()

x = input("Do you want to triger the event?(y/n)\n")
if x == 'y':
    event.set()
"""

### deamon threading
path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(3)

def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)

t1.start()
t2.start()
