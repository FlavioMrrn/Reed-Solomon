def exponentiationRapide(a,x,n):
    r = 1
    e = x
    b = a % n
    while e > 0:
        y = e % 2
        r = (r * pow(b,y) % n)
        b = (b*b)%n
        e = e//2
    return [r, b, e]


def main():
    print(exponentiationRapide(6, 17, 13))

if __name__ == "__main__":
    main()
