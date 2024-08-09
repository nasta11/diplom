from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Input

# Пример создания модели
model = Sequential([
    Input(shape=(60, 1)),  # Используем Input для определения формы входных данных
    LSTM(50, return_sequences=True),
    LSTM(50),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Сохранение модели в формате .keras
model.save('C:\\Users\\nasta\\OneDrive\\Desktop\\model.keras')



