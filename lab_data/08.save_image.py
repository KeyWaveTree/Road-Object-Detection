import cv2
import os

file_name='9b975a41-1b150816.jpg'

image=cv2.imread('../data/images/'+ file_name)

resize_image=cv2.resize(image, (100, 200))

if not os.path.exists('resize_image'):
    os.mkdir('resize_image')
#이미지 저장
cv2.imwrite('resize_image/0.jpg', resize_image)

