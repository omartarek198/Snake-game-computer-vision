import numpy as np
import mediapipe
import cv2
import cvzone
from cvzone.HandTrackingModule import  HandDetector
import random


import snake

def drawSnake(img, snake):

    for i in range(len(snake.points)-1):

        cv2.line(img,snake.points[i],snake.points[i+1],(0, 0, 255), 20)

def genFoodCordinates():
    x = random.randint(100,1100)
    y = random.randint(100,600)
    return x,y


cap = cv2.VideoCapture(2)
cap.set(3,1228)
cap.set(4,720)
FoodEaten = True
snake = snake.Snake()
print (snake.n)

detector = HandDetector(detectionCon=0.8,maxHands=1)

FoodPoint =genFoodCordinates()
Width = 30
FoodPoint2 = [FoodPoint[0] + Width, FoodPoint[1] + Width]
font = cv2.FONT_HERSHEY_SIMPLEX
score = 0

while True:
    success,img = cap.read()
    img = cv2.flip(img,1)
    hands,img = detector.findHands(img,flipType=False)
    cv2.rectangle(img,FoodPoint,FoodPoint2,(0,255,0),20)
    drawSnake(img,snake)

    img = cv2.putText(img, 'Score: ' + str(score), (50,50) , font,
                        1, (0,0,0), 2, cv2.LINE_AA)

    # Displaying the image
    if hands:
        points = hands[0]['lmList']
        TargetPoint = points[8][0:2]
        cv2.circle(img,TargetPoint,20, (0,0,0),cv2.FILLED)
        snake.MoveSnake(TargetPoint)
        if snake.IsFoodEaten(FoodPoint,FoodPoint2   ):
            snake.GrowSnake()
            FoodPoint = genFoodCordinates()
            FoodPoint2 = [FoodPoint[0] + Width, FoodPoint[1] + Width]
            score = score+1



    cv2.imshow("Image",img)
    cv2.waitKey(1)




