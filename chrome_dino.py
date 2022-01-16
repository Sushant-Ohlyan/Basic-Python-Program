import pyautogui
from PIL import Image,ImageGrab
#from numpy import asarray
import time
def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
#rectangle for bird
    for i in range(220,260):
        for j in range(230,395):
            if data[i,j] < 100:
                hit("down")
                return 
    for i in range(220,260):
        for j in range(400,472):
            if data[i,j] < 100:
                hit("up")
                return 
    return 
if __name__ == "__main__":
    print("hey..Dino game about to start in 3 seconds")
    time.sleep(3)
    hit('up')

    while True:
        image=ImageGrab.grab().convert('L')
        data= image.load()
        isCollide(data)
    
        #print(asarray(image))

    ''' #rectangle for cactus
        for i in range(220,260):
            for j in range(400,472):
                data[i,j] = 0
        #rectangle for bird
        for i in range(220,260):
            for j in range(230,395):
                data[i,j] = 171
        image.show()
        break'''