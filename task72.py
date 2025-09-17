while True:
    n = int(input("Введи число: "))
    b = bin(n)[2:]
    b = b.zfill(8)
    print(b)
