a = float(input("sisi a: "))
b = float(input("sisi b: "))
c = float(input("sisi c: "))

if (a + b <= c or b + c <= a or c + a <= b):
    print("Segitiga tidak valid")
elif (a == b and b == c):
    print("Segitiga sama sisi")
elif (a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2):
    print("Segitiga siku-siku")
elif (a == b or b == c or c == a):
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang") 