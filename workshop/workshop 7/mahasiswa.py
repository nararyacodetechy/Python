from models.table import Table 

tableMahasiswa = Table("Mahasiswa", "id")
tableStudi = Table("Studi", "id")

print(tableMahasiswa.table)
print(tableStudi.table)

def getMahasiswa() : 
    mahasiswa = tableStudi.getAll()

    for data in mahasiswa :
        print(data)
    mahasiswaRun = True

    while mahasiswaRun == True :
        print("ketik id mahasiswa untuk melihat studi")
        print("ketik back untuk kembali ke menu utama")
        pilihan = input()