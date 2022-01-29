import cv2

file_name='3b59c8a5-f0b031cc.jpg'
image=cv2.imread('../data/images/'+file_name)

cv2.putText(image,'python', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 2, cv2.LINE_AA)
#이미지 변수, 이름, 위치(왼쪽 아래점 기준), 폰트, 폰트 크기, 컬러(B,G,R)

cv2.imshow('image', image)# 창의 제목, 이미지 변수
cv2.waitKey(0) #키를 입력할 때 까지 무한으로 대기