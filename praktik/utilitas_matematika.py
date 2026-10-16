
def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


def faktorial(n):
    hasil = 1

    for i in range(2, n + 1):
        hasil *= i

    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (1-5): ")

        if pilihan == "1":
            p = float(input("Masukkan panjang: "))
            l = float(input("Masukkan lebar: "))

            if p < 0 or l < 0:
                print("Panjang dan lebar tidak boleh negatif.")
            else:
                hasil = luas_persegi_panjang(p, l)
                print("Luas persegi panjang =", hasil)

        elif pilihan == "2":
            a = float(input("Masukkan alas: "))
            t = float(input("Masukkan tinggi: "))

            if a < 0 or t < 0:
                print("Alas dan tinggi tidak boleh negatif.")
            else:
                hasil = luas_segitiga(a, t)
                print("Luas segitiga =", hasil)

        elif pilihan == "3":
            masukan = input("Masukkan n: ")

            try:
                n = int(masukan)

                if n >= 0:
                    print("Jumlah =", jumlah_n(n))
                else:
                    print("n harus bilangan bulat nonnegatif.")

            except ValueError:
                print("Masukkan bilangan bulat yang valid.")

        elif pilihan == "4":
            masukan = input("Masukkan n: ")

            try:
                n = int(masukan)

                if n >= 0:
                    print("Faktorial =", faktorial(n))
                else:
                    print("n harus bilangan bulat nonnegatif.")

            except ValueError:
                print("Masukkan bilangan bulat yang valid.")

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Pilih 1 sampai 5.")


if __name__ == "__main__":
    main()
