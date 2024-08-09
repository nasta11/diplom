import tensorflow as tf
from tensorflow import keras

# Загрузка модели из файла
model = keras.models.load_model('C:/Users/nasta/OneDrive/Desktop/диплом/model.h5')

# Просмотр структуры модели
model.summary()
