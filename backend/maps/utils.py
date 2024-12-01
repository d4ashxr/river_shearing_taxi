from geopy.distance import geodesic

docks = [
    {'name': 'Парк Горького', 'coordinates': (55.73013, 37.597184)},
    {'name': 'Нескучный сад', 'coordinates': (55.722427, 37.590694)},
    {'name': 'Крымский мост', 'coordinates': (55.732427, 37.596061)},
    {'name': 'Марьино', 'coordinates': (55.641785, 37.725065)},
    {'name': 'Печатники', 'coordinates': (55.683699, 37.714149)},
    {'name': 'Меловой', 'coordinates': (55.69106, 37.696817)},
    {'name': 'Южный речной вокзал', 'coordinates': (55.689415, 37.675846)},
    {'name': 'Кленовый бульвар', 'coordinates': (55.686457, 37.67215)},
    {'name': 'Воробьевы горы', 'coordinates': (55.711738, 37.546826)},
    {'name': 'Киевский', 'coordinates': (55.743672, 37.571839)},
    {'name': 'Красный октябрь', 'coordinates': (55.745129, 37.610627)},
    {'name': 'Сити – Экспоцентр', 'coordinates': (55.748745, 37.546796)},
    {'name': 'Новоспасский', 'coordinates': (55.730281, 37.653392)},
    {'name': 'Китай-город', 'coordinates': (55.748462, 37.635886)},
    {'name': 'Патриарший', 'coordinates': (55.743972, 37.608138)},
    {'name': 'Лужники – Северный', 'coordinates': (55.726423, 37.545615)},
    {'name': 'Третьяковский', 'coordinates': (55.744502, 37.618414)},
    {'name': 'Кутузовский', 'coordinates': (55.744387, 37.538187)},
    {'name': 'Троице-Лыково', 'coordinates': (55.79192, 37.409289)},
    {'name': 'Парк Фили', 'coordinates': (55.749486, 37.475581)},
    {'name': 'Захарково', 'coordinates': (55.849065, 37.459077)},
    {'name': 'Трёхгорный', 'coordinates': (55.754254, 37.56394)},
    {'name': 'Сити – Багратион', 'coordinates': (55.746481, 37.545233)},
    {'name': 'Лужники - Центральный', 'coordinates': (55.713129, 37.549501)},
    {'name': 'Северный речной вокзал', 'coordinates': (55.851125, 37.466138)},
    {'name': 'Андреевский', 'coordinates': (55.711646, 37.572238)},
    {'name': 'Зарядье', 'coordinates': (55.749528, 37.629242)},
    {'name': 'Серебряный бор-2', 'coordinates': (55.785823, 37.424496)},
    {'name': 'Серебряный бор-3', 'coordinates': (55.785127, 37.444882)},
    {'name': 'Сити – Центральный', 'coordinates': (55.746589, 37.541693)},
    {'name': 'Автозаводский мост', 'coordinates': (55.702836, 37.626632)},
    {'name': 'Химки', 'coordinates': (55.886542, 37.458891)},
    {'name': 'Сердце Столицы', 'coordinates': (55.76049721, 37.51224589)},
    {'name': 'ЗИЛ', 'coordinates': (55.6999347, 37.628875)},
    {'name': 'Нагатинский затон', 'coordinates': (55.685878, 37.701144)},
    {'name': 'Береговой', 'coordinates': (55.758389, 37.512611)},
]

def nearest_docks(city_coordinates, top_n=3):

    distances = []

    # Рассчитываем расстояние до каждого причала
    for dock in docks:
        distance = geodesic(city_coordinates, dock['coordinates']).km  # Расстояние в километрах
        distances.append({'name': dock['name'], 'coordinates': dock['coordinates'], 'distance': distance})

    # Сортируем по расстоянию
    distances.sort(key=lambda x: x['distance'])

    # Возвращаем top_n ближайших причалов
    return distances[:top_n]


