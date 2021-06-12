import cv2
import numpy
cimage=numpy.zeros((600,600,3))
for i in range(80,601,80):
    cv2.rectangle(cimage,(80+i,80+i),(550-i,550-i),[90,25,1],2)
for i in range(70,601,80):
    cv2.rectangle(cimage,(70+i,70+i),(550-i,550-i),[29,2,15],2)
for i in range(60,601,80):
    cv2.rectangle(cimage,(60+i,60+i),(550-i,550-i),[20,250,14],2)
for i in range(50,601,80):
    cv2.rectangle(cimage,(50+i,50+i),(550-i,550-i),[209,0,154],2)
for i in range(40,601,80):
    cv2.rectangle(cimage,(40+i,40+i),(550-i,550-i),[0,0,154],2)
for i in range(100,601,80):
    cv2.rectangle(cimage,(100+i,100+i),(550-i,550-i),[209,250,154],2)

for i in range(300,601,80):
    cv2.rectangle(cimage,(30+i,30+i),(550-i,550-i),[255,0,0],5)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(cimage,'LINES',(250,300),font,2,[51,226,240],8,cv2.LINE_AA)
cv2.imshow("own",cimage)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("ownimg.jpg",cimage)
