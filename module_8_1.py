def add_everything_up(a, b):
    """
    Функция принимает a и b, которые могут быть как числами(int, float), так и строками(str).
    """
    try:
        print(a + b)
    except TypeError:
        print(f"{a}{b}")


add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)

