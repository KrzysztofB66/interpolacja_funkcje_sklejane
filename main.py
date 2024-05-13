class Punkt:
    def __init__(self, x, f_x):
        self.x = x
        self.f_x = f_x


def eliminacja_gausa(A, b):
    n = len(A)
    M = A

    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        for j in range(k+1, n):
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] = round(float(M[n-1][n])/M[n-1][n-1], 3)
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z = z + float(M[i][j])*x[j]
        x[i] = round(float(M[i][n] - z)/M[i][i], 3)
    return x


def W_3(x):
    lista = []
    for i in range(0, 4):
        if i == 0:
            lista.append(1)
        else:
            lista.append(x**i)
    return lista


def W_3_prim(x):
    lista = []
    for i in range(0, 4):
        if i == 0:
            lista.append(0)
        else:
            lista.append((i)*x**(i-1))
    return lista


def calculate_summation(a, x, n):
    return sum(a[s] * (x - s)**3 for s in range(1, n))

# ----------------------------------------------------------------------------------------------
# to podane
punkty = [Punkt(-4, -524), Punkt(-2,-36), Punkt(0,-4), Punkt(2,-44), Punkt(4,-540)]
pochodne_krancow_punkty = [Punkt(-4,518), Punkt(4,-522)]
x = 3

A = []
B = []
index = 0
for punkt in punkty:
    if index < 2:
        A.append(W_3(punkt.x))
    else:
        A.append(W_3(punkt.x))
        for s in range(1, index):
            A[index].append((punkt.x - punkty[s].x) ** 3)
    index += 1
    B.append(punkt.f_x)


# obliczanie węzłów krańcowych
A.append(W_3_prim(pochodne_krancow_punkty[0].x))
B.append(pochodne_krancow_punkty[0].f_x)
A.append(W_3_prim(pochodne_krancow_punkty[1].x))
for s in range(1, len(punkty)-1):
    A[len(punkty)+1].append(3 * (pochodne_krancow_punkty[1].x - punkty[s].x) ** 2)
B.append(pochodne_krancow_punkty[1].f_x)


# dodawanie zer tam gdzie nie ma

for lista in A:
    while len(lista) < len(punkty)+2:
        lista.append(0)

a = eliminacja_gausa(A, B)


def rozwiazanie_w_punkcie(x, a, punkty):
    wynik = 0
    if x < punkty[0].x:
        print("niema wyniku")
    else:
        wynik += a[0] + a[1] * x + a[2] * (x ** 2) + a[3] * (x ** 3)
        if x > punkty[1].x:
            for i in range(1, len(punkty)-1):
                if x > punkty[i].x:
                    wynik += (a[i+3] * ((x - punkty[i].x) ** 3))
    return round(wynik, 3)


print(rozwiazanie_w_punkcie(x, a, punkty))


