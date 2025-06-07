"Program Manajemen Kontak"

def melihat_kontak():
    # Melihat Kontak
    print("=" * 25)
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]} ({item["nomorHp"]}, {item["email"]}) \n')
    else:
        print("Kontak masih kosong!")
        return 1


def menambah_kontak():
    # Menambahkan Kontak
    nama = input("Masukkan Nama kontak yang baru: ")
    nomorHp = input("Masukkan Nomor Hp kontak yang baru: ")
    email = input("Masukkan Email kontak yang baru: ")
    kontak_baru = {"nama": nama, "nomorHp": nomorHp, "email": email}
    kontak.append(kontak_baru)
    print("=" * 25)
    print("Kontak baru berhasil di tambahkan!")
    print("=" * 25)
    print("\n")


def menghapus_kontak():
    # Menghapus Kontak
    print("=" * 25)
    if melihat_kontak() == 1:
        return
    else:
        print("=" * 25)
        i_hapus = int(input("\nMasukkan nomor kontak yang ingin di hapus: "))
        del kontak[i_hapus - 1]
        print("=" * 25)
        print("Kontak berhasil di hapus! ")
        print("=" * 25)
        print("\n")


kontak1 = {"nama": "Luvi", "nomorHp": "+123 456 7890", "email": "luvi@python.com"}
kontak2 = {"nama": "Sinta", "nomorHp": "+123 456 7890", "email": "sinta@python.com"}
kontak3 = {"nama": "Gabriel", "nomorHp": "+123 456 7890", "email": "gabriel@python.com"}
kontak4 = {"nama": "Iyel", "nomorHp": "+123 456 7890", "email": "iyel@python.com"}
kontak = [kontak1, kontak2, kontak3, kontak4]

while True:
    print("=" * 25)
    print("Manajemen Kontak sederhana")
    print("=" * 25)
    print("1. Melihat Kontak")
    print("2. Menambahkan Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        melihat_kontak()

    elif pilihan == "2":
        menambah_kontak()

    elif pilihan == "3":
        menghapus_kontak()

    elif pilihan == "4":
        # Keluar dari program kontak
        break
    else:
        print("Berhasil keluar!")
