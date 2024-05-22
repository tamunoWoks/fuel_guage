def main():
    while True:
        fraction = input('Fraction: ').strip()
        try:
            process(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass
        continue




def process(fraction):
    while True:
        s = fraction.split('/')
        x = int(s[0])
        y = int(s[1])

        if x > y:
            fraction = input('Fraction: ').strip()
        else:
            break

    percentage = (x/y)*100

    if percentage <= 1:
        print('E')
    elif percentage >= 99:
        print('F')
    else:
        print(f'{round(percentage)}%')

if __name__ == "__main__":
    main()