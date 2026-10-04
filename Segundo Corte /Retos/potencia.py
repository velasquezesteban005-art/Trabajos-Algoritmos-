import time
import sys
sys.setrecursionlimit(10000)

llamadas = {"lineal": 0, "rapida": 0}


def potencia_lineal(a, b):
    """a^b = a * a^(b-1).  O(b) llamadas."""
    llamadas["lineal"] += 1
    if b == 0:
        return 1
    return a * potencia_lineal(a, b - 1)


def potencia_rapida(a, b):
    """b par   -> a^b = (a^(b/2))^2
       b impar -> a^b = a * (a^(b//2))^2
       O(log b) llamadas."""
    llamadas["rapida"] += 1
    if b == 0:
        return 1
    mitad = potencia_rapida(a, b // 2)    # <-- UNA sola llamada
    if b % 2 == 0:
        return mitad * mitad
    return a * mitad * mitad


if __name__ == "__main__":
    a, b = 1.0000001, 5000

    t0 = time.perf_counter()
    r1 = potencia_lineal(a, b)
    t1 = time.perf_counter()
    r2 = potencia_rapida(a, b)
    t2 = time.perf_counter()

    print(f"Lineal : {r1:.10f} | llamadas = {llamadas['lineal']:6d} | {(t1-t0)*1e6:10.2f} us")
    print(f"Rapida : {r2:.10f} | llamadas = {llamadas['rapida']:6d} | {(t2-t1)*1e6:10.2f} us")