def main():
    while True:
        try:
            print(gauge(convert(input("Fraction: "))))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x, y = fraction.split("/")

    if int(y) == 0:
        raise ZeroDivisionError
    if int(x) > int(y):
        raise ValueError
    
    percentage = int((x/y) * 100)
    return percentage


def gauge(percentage):
    try:
        if percentage <= 1:
            return "E"
        elif percentage >= 99:
            return "F"
        else:
            return str(percentage) + '%'
    except TypeError:
        pass


if __name__ == "__main__":
    main()
