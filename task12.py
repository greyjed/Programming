while True:
    try:
        n = input()
        if not n:
            break
        print(f"{int(n)};")
    except EOFError:
        break
