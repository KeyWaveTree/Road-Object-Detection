import tensorflow as tf

#데이터 셋 불러오기
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',#데이터를 불러오는 경로
    image_size=(224, 224),  #균일한 크기로 변경
    label_mode='categorical',
    #label_mode='',
)

data = train_dataset.take(1) #데이터 셋을로 부터 덩어리를 가지고 온다.
for images, labels in data:
    print(images.shape, labels.shape)

print(train_dataset.class_names)