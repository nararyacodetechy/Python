from models.table import Table

tableMahasiswa = Table('Mahasiswa', 'id')

print(tableMahasiswa.table)

def getStudi():
    

def getMahasiswa():
    for data in tableMahasiswa.getAll() :
        print(data)

        while mahasiswaRun == True:
            print("ketik 'id mahasiswa' untuk melihat studi mahasiswa ")
            print("ketik 'back' untuk kembali ke menu utama")
            pilihan = input()

            if pilihan == 'back':
                mahasiswaRun = False
            else:
                getStudi(pilihan)

def deleteMahasiswa():
    for data in tableMahasiswa.getAll():
        print(data)

    id = input("Masukan id mahasiswa yang ingin dihapus : ")

    tableMahasiswa.delete(id)

    print("data mahasiswa tersebut berhasil dihapus!")
    addMahasiswaRun = True

    while addMahasiswaRun == True:
        print("Hapus data Lagi ? (y/n) : ")
        pilihan = input("pilihan : ")

        if pilihan == 'y':
            deleteMahasiswa()
        else:
            addMahasiswaRun == False


    
            
