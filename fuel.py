def main():
    fraction = input('Fraction: ').strip()


def process():
    while True:
        s = fraction.split('/')
        x = int(s[0])
        y = int(s[1])

        if x > y:
            fraction = input('Fraction: ').strip()
        else:
            break

    percentage = (x/y)*100

if __name__ == "__main__":
    main()