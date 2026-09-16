from alphabet import Alphabet
from cli import get_alphabet

def f(i: str):
    n = len(i)
    if n == 0:
        print("   ", end="|")
    if n == 1:
        print(f"{i}  ", end="|")
    if n == 2:
        print(f"{i} ", end="|")
    if n == 3:
        print(f"{i}", end="|")

alphabet: Alphabet = get_alphabet()
n: int = alphabet.get_size()

print("   ", end="|")
for x in range(n):
    f(str(x))
print()
print("===|"*n)
for y in range(n):
    f(str(y))
    for x in range(n):
        f(alphabet.get_symbol((x+y)%n))
    print()