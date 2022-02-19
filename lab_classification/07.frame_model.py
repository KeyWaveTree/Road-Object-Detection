import tensorflow as tf
import os

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../classification_data/',#데이터를 불러오는 경로
    image_size=(224, 224),  #균일한 크기로 변경
    label_mode='categorical',
    #batch_size=4
    #label_mode='',
)

model = tf.keras.models.load_model('../models/mymodel.h5')
model.summary()

if not os.path.exists('../logs'):
    os.mkdir('../logs')

tensorboard = tf.keras.callbacks.TensorBoard(log_dir='../logs')

learning_rate=0.0075
model.compile(
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.RMSprop(learning_rate=learning_rate),
    metrics=['accuracy']
)

model.fit(train_dataset, epochs=100, callbacks=[tensorboard])

model.save('../models/classification_model_trained.h5')