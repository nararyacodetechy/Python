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
        print("ketik id mahasiwa untuk melihat studi")
        print("ketik back untuk kembali ke menu utama")
        pilihan = input()

def _init_(self, t, k) :
    self.table = t
    self.key = k

def get(self, id):
    konek = self.connection()
    cursor = konek.cursor()

    cursor.execute("SELECT*FROM %s WHERE %s=%s" % (self.table, self.key, id))

    data = cursor.fetchone()
    konek.close()
    return data

def getAll(self) :
    konek = self.connection()
    cursor = konek.cursor()

    cursor.execute("SELECT*FROM %s" % (self.table))

    data = cursor.fetchall()
    konek.close()
    
def deleteMahasiswa() :
    mahasiswa = tableMahasiswa.getAll()

    for row in mahasiswa :
        print(row)

    id = input("pilih id mahasiswa yang ingin dihapus : ")

    tableMahasiswa.delete(id)
