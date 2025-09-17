while True:
    try:
        a = input("Введіть символ (або натисніть Enter для завершення): ")
        if a == "":
            break
        print(ord(a))
    except Exception as e:
        print("Помилка:", e)
