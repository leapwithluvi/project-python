def tambah_agenda(agenda, agenda_baru):
    agenda.append(agenda_baru)
    print("Agenda berhasil ditambahkan!")

def lihat_agenda(agenda):
    print("Daftar AgendaKU:")
    for index, item in enumerate(agenda):
        print(f"{index+1}. {item}")

def main():
    agenda = []

    while True:
        print("\nWelcome to AgendaKu!")
        print("1. Menambah Agenda")
        print("2. Melihat Agenda")
        print("3. Keluar dari Agenda")

        pilihan = input("Masukkan pilihan dari antara (1/2/3): ")

        if pilihan == '1':
            agenda_baru = input("Masukkan agenda baru: ")
            tambah_agenda(agenda, agenda_baru)
        elif pilihan == '2':
            lihat_agenda(agenda)
        elif pilihan == '3':
            break
        else:
            print("Pilihan anda salah, masukkan pilihan yang tepat (1, 2 atau 3)")

    print("Anda berhasil keluar dari program AgendaKU!")

if __name__ == "__main__":
    main()
