import cv2
flag1=cv2.imread("flag1.jpg")
smriti=cv2.imread("smriti.jpg")
flag1=cv2.resize(flag1,(512,512))
smriti=cv2.resize(smriti,(512,512))
fin_img=cv2.add(flag1,smriti)
cv2.imshow("smriti",fin_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
