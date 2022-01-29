import cv2

file_name='3b59c8a5-f0b031cc.jpg'
image=cv2.imread('../data/images/'+file_name)

cv2.rectangle(image, (10,10), (100, 100), (0,0,255), 3) #이미지 처리할 변수, 왼쪽위점, 오른쪽 아래점, bgr색깔, 선두깨

cv2.imshow('image', image)# 창의 제목, 이미지 변수
cv2.waitKey(0) #키를 입력할 때 까지 무한으로 대기


