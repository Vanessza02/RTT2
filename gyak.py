"""Ez a fájl a faktoriális számítását végzi egy adott számra."""

def faktorialis(n):
    """Kiszámítja egy szám faktoriálisát."""
    if n in (0, 1):
        return 1
    return n * faktorialis(n - 1)

try:
    szam = int(input("Adj meg egy pozitív egész számot: "))
    if szam < 0:
        print("A faktoriális csak nemnegatív egész számokra értelmezett!")
    else:
        print(f"A {szam}! értéke: {faktorialis(szam)}")
except ValueError:
    print("Kérlek, egész számot adj meg!")

#véhge