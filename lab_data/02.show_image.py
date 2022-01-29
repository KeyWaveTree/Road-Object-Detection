import cv2

file_name='3b59c8a5-f0b031cc.jpg'
image=cv2.imread('../data/images/'+file_name)

#이미지 띄우기
cv2.imshow('image', image)# 창의 제목, 이미지 변수
cv2.waitKey(0) #키를 입력할 때 까지 무한으로 대기


