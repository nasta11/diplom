from sklearn.preprocessing import MinMaxScaler

# Пример данных
dataset = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]

# Создание и применение MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

# Вывод масштабированных данных
print(scaled_data)

