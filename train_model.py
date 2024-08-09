import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Пример данных
data = np.array([[i] for i in range(1, 81)])  # Массив данных от 1 до 80

def min_max_scaler(data, feature_range=(0, 1)):
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    range_val = feature_range[1] - feature_range[0]
    
    scaled_data = (data - min_val) / (max_val - min_val) * range_val + feature_range[0]
    return scaled_data

# Применение масштабирования
scaled_data = min_max_scaler(data)

# Установите длину тренировочных данных
training_data_len = len(scaled_data) - 1

# Создание тренировочных данных
train_data = scaled_data[0:int(training_data_len), :]
x_train = []
y_train = []

# Создание последовательностей данных
for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])

# Преобразование в массивы NumPy
x_train, y_train = np.array(x_train), np.array(y_train)

# Изменение формы данных для RNN или LSTM
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Строим LSTM модель
model = Sequential()
model.add(LSTM(128, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# Компиляция модели
model.compile(optimizer='adam', loss='mean_squared_error')

# Обучение модели
model.fit(x_train, y_train, batch_size=1, epochs=10)

print("Model trained successfully.")

