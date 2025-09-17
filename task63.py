while True:
    n = int(input("Введіть кількість хвилин після опівночі: "))

    h = (n // 60) % 24
    m = n % 60

    print(h, m)
