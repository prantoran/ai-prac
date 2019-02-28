import time
import webbrowser

bc = 0

print("this program started on " + time.ctime())

while (bc < 3):
    time.sleep(10) # in sec
    webbrowser.open("https://www.deeplearningbook.org/")
    bc += 1