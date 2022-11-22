#Retourne [PGCD, BachetBezout1, BachetBezout2]
def pgcd_bezout(a, b):
    r0 = a
    r1 = b
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1
    x = 0
    y = 0
    r = 1
    while(r != 0):
        q = r0 // r1
        r = r0 - q * r1
        x = x0 - q * x1
        y = y0 - q * y1
        x0 = x1
        x1 = x
        y0 = y1
        y1 = y
        r0 = r1
        r1 = r
    return [r0, x0, y0]

def main():
    print(pgcd_bezout(2869, 235))

if __name__ == "__main__":
    main()
