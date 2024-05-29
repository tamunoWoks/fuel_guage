def main():
    while True:
        try:
            print(gauge(convert(input("Fraction: "))))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    
    percentage = int((float(x)/y) * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
            return "{}%".format(percentage)


if __name__ == "__main__":
    main()
