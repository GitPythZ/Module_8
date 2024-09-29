def add_everything_up(a, b):
    """
    Функция принимает a и b, которые могут быть как числами(int, float), так и строками(str).
    """
    try:
        print(a + b)
    except TypeError:
        print(f"{a}{b}")


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))