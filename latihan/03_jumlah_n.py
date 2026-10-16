
def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


print("Jumlah 1 sampai 1 =", jumlah_n(1))
print("Jumlah 1 sampai 5 =", jumlah_n(5))
print("Jumlah 1 sampai 10 =", jumlah_n(10))
print("Jumlah 1 sampai 100 =", jumlah_n(100))
