"Program Manajemen Kontak"
class Kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        # Melihat Kontak
        print("=" * 25)
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["nomorHp"]}, {item["email"]}) \n')
        else:
            print("Kontak masih kosong!")
            return 1


    def menambah_kontak(self):
        # Menambahkan Kontak
        nama = input("Masukkan Nama kontak yang baru: ")
        nomorHp = input("Masukkan Nomor Hp kontak yang baru: ")
        email = input("Masukkan Email kontak yang baru: ")
        kontak_baru = {"nama": nama, "nomorHp": nomorHp, "email": email}
        self.kontak.append(kontak_baru)
        print("=" * 25)
        print("Kontak baru berhasil di tambahkan!")
        print("=" * 25)
        print("\n")


    def menghapus_kontak(self):
        # Menghapus Kontak
        print("=" * 25)
        if self.melihat_kontak() == 1:
            return
        else:
            print("=" * 25)
            i_hapus = int(input("\nMasukkan nomor kontak yang ingin di hapus: "))
            del self.kontak[i_hapus - 1]
            print("=" * 25)
            print("Kontak berhasil di hapus! ")
            print("=" * 25)
            print("\n")

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

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
        kontak_kantor.melihat_kontak()

    elif pilihan == "2":
        kontak_kantor.menambah_kontak()

    elif pilihan == "3":
        kontak_kantor.menghapus_kontak()

    elif pilihan == "4":
        # Keluar dari program kontak
        break
    else:
        print("Berhasil keluar!")
