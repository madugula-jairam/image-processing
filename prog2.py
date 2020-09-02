
import cv2
import numpy as np
img = cv2.imread("one.jpg") 
img1 = cv2.imread("two.jpg") 
cv2.imshow('first image',img)
cv2.imshow("second image",img1)

add = img + img1
sub = img - img1
AND = img & img1
OR = img | img1
xoroperator = img ^ img1
onesoperator = ~ img
leftshift =  img << 2
rightshift =  img >> 2


concat = np.concatenate((add, sub), axis=1)
cv2.imshow('add & sub images', concat)

concat1 = np.concatenate((AND, OR), axis=1)
cv2.imshow('ANDed & ORed images', concat1)

concat2 = np.concatenate((xoroperator,onesoperator), axis=1)
cv2.imshow('XOR and NEGATION', concat2)

concat3 = np.concatenate((leftshift,rightshift), axis=1)
cv2.imshow('Shifthing Operation', concat3)

cv2.waitKey(0)
cv2.destroyAllWindows()
