from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Пример создания модели
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(60, 1)),
    LSTM(50),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Сохранение модели
model.save(r'C:\Users\nasta\OneDrive\Desktop\model.h5')


