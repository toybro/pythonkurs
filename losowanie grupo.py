import random

uczniowie = {
    "Arkadiusz Binder": 1,
    "Kacper Weprzędz": 0,
    "Krzysztof Formella": 1,
    "Maksym Buka": 1,
    "Marcin Węsierski": 1,
    "Rafał Szopa": 1,
    "Sebastian Kornet": 1,
    "Sebastian Miłkowski": 0,
    "Stanisław Witkowski": 0,
    "Yana Kurochka": 1
}

obecni = [u for u, status in uczniowie.items() if status == 1]
random.shuffle(obecni)

grupy = [obecni[i:i+2] for i in range(0, len(obecni), 2)]

for grupa in grupy:
    print(grupa)
