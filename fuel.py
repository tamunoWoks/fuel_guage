def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            print(guage(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            raise
        continue


def convert(fraction):
    while True:
        s = fraction.split("/")
        x = int(s[0])
        y = int(s[1])

        if x > y:
            fraction = input("Fraction: ").strip()
        else:
            break

    percentage = (x / y) * 100
    return percentage

def guage(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{round(percentage)}%")


if __name__ == "__main__":
    main()
