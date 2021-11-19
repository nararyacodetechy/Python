 # import library PrettyTable
from prettytable import PrettyTable

# buat object dari PrettyTable()
tabel_data_mahasiswa = PrettyTable()

# isi judul tabel
tabel_data_mahasiswa_HEADER = [
    "URUTAN",
    "NIM",
    "NAMA",
    "JURUSAN"
]

# deklarasi urutan = 0
urutan = 0

# membuat judul tabel
tabel_data_mahasiswa.field_names = [h for h in tabel_data_mahasiswa_HEADER]

# mengatur align data ke kiri (default= center)
tabel_data_mahasiswa.align['NIM'] = "l"
tabel_data_mahasiswa.align['NAMA'] = "l"
tabel_data_mahasiswa.align['JURUSAN'] = "l"

# menampung data ke dalam dictionary
data_mahasiswa = []

# fitur yang tersedia
fitur = [
    {
        '1': 'tambah data',
        '2': 'hapus data',
        '3': 'ubah data',
        '4': 'lihat data\n',
        '0': 'keluar'
    }
]


def tambah_data():
    global urutan

    urutan += 1
    nim = input("NIM: ")
    nama = input("Nama: ")
    jurusan = input("Jurusan: ")

    # data_mahasiswa['urutan'] = urutan
    # data_mahasiswa['nim'] = nim
    # data_mahasiswa['nama'] = nama
    # data_mahasiswa['jurusan'] = jurusan

    data_mahasiswa.append(
        {
            'urutan':urutan,
            'nim':nim,
            'nama':nama,
            'jurusan':jurusan
        }
    )

    tabel_data_mahasiswa.add_row(
        [
            urutan, nim, nama, jurusan
        ]
    )

def hapus_data():
    print(tabel_data_mahasiswa)
    urutan_del_row = input("[-] Urutan yang akan di hapus: ")
    tanya_hapus = input("[-] Yakin ingin menghapus [Y/n]: ")
    if tanya_hapus == "Y" or tanya_hapus == 'y':
        tabel_data_mahasiswa.del_row(int(urutan_del_row))
        print("[-] Berhasil dihapus!")
    elif tanya_hapus == "n" or tanya_hapus == "N":
        main()
    else:
        print("*] Pilihan tidak tersedia!")

# def ubah_data():
#     print(tabel_data_mahasiswa)
#     urutan_ubah_data = input("[-] Urutan yang akan di ubah: ")
#     tanya_ubah = input("[-] Yakin ingin mengubah [Y/n]: ")
#     if tanya_ubah == "Y" or tanya_ubah == 'y':
#         tabel_data_mahasiswa.del_row(int(urutan_ubah_data))
#         print("[-] Berhasil dihapus!")
#     elif tanya_ubah == "n" or tanya_ubah == "N":
#         main()
#     else:
#         print("*] Pilihan tidak tersedia!")

def lihat_data():
    print(tabel_data_mahasiswa)
    
def main():
    
    print("[*] Selamat Datang di Manajemen Data Mahasiswa [*]")
    print("[*] Fitur tersedia:")
    for key, value in fitur[0].items():
        print(f"\t{key}. {value.title()}")
    print()
    pilih_fitur = input("\t[*] Pilih Fitur: ")

    while pilih_fitur != "0":
        if pilih_fitur == "0":
            break
        elif pilih_fitur == "1":
            tambah_data()
        elif pilih_fitur == "2":
            hapus_data()
        elif pilih_fitur == "4":
            lihat_data()
        else:
            print("[*] Fitur tidak tersedia!")
        print()
        pilih_fitur = input("\t[*] Pilih Fitur: ")
    else:
        print("[*] Program selesai!")

main()