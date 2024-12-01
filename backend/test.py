from geopy.distance import geodesic

# Список координат известных причалов на реке Москва (пример)
docks = [
    {'name': 'Причал 1', 'coordinates': (55.751244, 37.618423)},  # Пример координат
    {'name': 'Причал 2', 'coordinates': (55.749024, 37.617734)},  # Пример координат
    {'name': 'Причал 3', 'coordinates': (55.741914, 37.630679)},  # Пример координат
    # Добавьте остальные причалы по аналогии
]

def nearest_dock(city_coordinates):
    """
    Функция для нахождения ближайшего причала на реке Москва.

    :param city_coordinates: Кортеж координат города (широта, долгота)
    :return: Название ближайшего причала и его координаты
    """
    closest_dock = None
    min_distance = float('inf')  # Начальная минимальная дистанция (бесконечность)

    for dock in docks:
        distance = geodesic(city_coordinates, dock['coordinates']).km  # Расстояние в километрах
        if distance < min_distance:
            min_distance = distance
            closest_dock = dock

    return closest_dock['name'], closest_dock['coordinates'], min_distance

# Пример использования
city_coordinates = (55.7558, 37.6173)  # Координаты Москвы
dock_name, dock_coordinates, distance = nearest_dock(city_coordinates)

print(f"Ближайший причал: {dock_name}")
print(f"Координаты причала: {dock_coordinates}")
print(f"Расстояние до причала: {distance:.2f} км")
