import cv2
import os
import json

image_path='../data/images/'
file_name=os.listdir(image_path)

f=open('../data/labels/labels.json')
labels=json.load(f)

if not os.path.exists('../classification_data'):
    os.mkdir('../classification_data')

for i in range(len(file_name)):
    image=cv2.imread(image_path + file_name[i])
    for label in labels:
        if label['name']==file_name[i]:
            for l in label['labels']:
                if 'box2d' in l:
                    x1=int(l['box2d']['x1'])
                    y1=int(l['box2d']['y1'])
                    x2=int(l['box2d']['x2'])
                    y2=int(l['box2d']['y2'])
                    # 이미지 처리할 변수, 왼쪽위점, 오른쪽 아래점, bgr색깔, 선두깨
                    crop_image=image[y1:y2+1,x1:x2+1]
                    if not os.path.exists('../classification_data/' + l['category']):
                        os.mkdir('../classification_data/' + l['category'])

                    if not image is None:
                        cv2.imwrite(f'../classification_data/{l["category"]}/{str(i)}.jpg', crop_image)
                    else:
                        continue

