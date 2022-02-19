import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',
    image_size=(224, 224),
    label_mode='categorical',
)

data = train_dataset.take(1)

plt.figure(0) #내가 지금 그길 그림(아나콘다 activate)
plt.title('data')

for images, labels in data:
    for i in range(5):
        plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype('uint8'))
        plt.title(train_dataset.class_names[np.argmax(labels[i])])
        plt.axis('off')

plt.show()