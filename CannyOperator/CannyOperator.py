import numpy as np
import cv2

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def saveImage(img, name):
    cv2.imwrite(name, img)

def CannyOperator(image):
    dst = cv2.GaussianBlur(image,(5,5),cv2.BORDER_DEFAULT) #Noise Reduction with 5 by 5 filter
    edges = cv2.Canny(dst, 10, 30) #defining max and min values for the threshold for detecting edges
    saveImage(edges, "Canny-ed.jpg")
    viewImage(edges, "HI")
    cv2.destroyAllWindows()

temp = cv2.imread("IMG_4232.jpg")
CannyOperator(temp)
print("Its saved as Canny-ed.jpg")