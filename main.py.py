import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time


def hit (key):
    pyautogui .keyDown(key)

def isCollide(data):
    # Rectangle for the bird
    for i in range(445,560):
            for j in range(452,605):
                if data[i,j]==171 :
                    hit("down")
                    return True

    for i in range(445,560):
            for j in range(605,685):
                if data[i,j]<100:
                    hit("up")
                    # Less than 100 is done because we consider the color code for black is less than 100 and here black is our obstacle.
                    return True
    return False            

if __name__ == "__main__":
    print("Hey.. Dino game ids about to start in 5 second")
    time.sleep(2)
    hit('up')
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        isCollide(data)
            
        '''
        # print(asarray(image))
        # Draw the rectangle for cactus
        for i in range(445,570):
            for j in range(605,685):
                data[i,j]=0   
                #  here 0 denotes the black color of the obstacle because the pixel color for the black is zero 
                # And pixel color for white is 255
        # Draw the rectangle for Bird
        for i in range(445,570):
            for j in range(452,605):
                data[i,j]=171   
        image.show()
        break
        '''