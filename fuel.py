def main():
    while True:
        try:
            print(gauge(convert(input('Fraction: '))))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x, y = fraction.split("/")

    if int(y) == 0:
        raise ZeroDivisionError
    if int(x) > int(y):
        raise ValueError
    return int(int(x)/int(y) * 100)

def gauge(percentage):
    try:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        elif 1 < percentage < 99:
            return percentage + '%'
        else:
            raise TypeError
    except TypeError:
        pass


if __name__ == "__main__":
    main()
