import cv2

file_name='9b975a41-1b150816.jpg'

image=cv2.imread('../data/images/'+ file_name)

resize_image=cv2.resize(image, (100, 200))

cv2.imshow('image', resize_image)
cv2.waitKey(0)
