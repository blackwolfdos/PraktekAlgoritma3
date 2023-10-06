import math

a = int(input("Nilai A: "))
b = int(input("Nilai B: "))
c = int(input("Nilai C: "))

if a == 0:
    print("Bukan persamaan kuadrat karena A = 0")
else:
    Diskriminan = b**2 - 4*a*c
    print(f"persamaan kuadrat: {a}x² + {b}x + {c}")
    print("Diskriminan: ", Diskriminan)

    if Diskriminan == 0:
        print("Merupakan akar kembar")
        print("akar = ", (-b + math.sqrt((b**2) - (4*a*c))) / 2*a)
    elif Diskriminan < 0:
        print("Merupakan akar imaginer")
        print(f"x1 = {-b} + √{(b**2)-(4*a*c)}/2*{a}")
        print(f"x2 = {-b} - √{(b**2)-(4*a*c)}/2*{a}")
    else:
        print("Merupakan akar berbeda")
        print("x1 = ", (-b + math.sqrt((b**2) - (4*a*c))) / 2*a)
        print("x2 = ", (-b - math.sqrt((b**2) - (4*a*c))) / 2*a) 