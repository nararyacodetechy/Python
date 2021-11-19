# DATABASE ADMIN
import mysql.connector

from prettytable import PrettyTable  
  
db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_gameshop' 
) 

def Menampilkan(db):
    print("="*107)
    print(" "*44+"MENAMPILKAN DATA:")
    print("="*107)
    tampil = db.cursor()
    sql = ("SELECT * FROM tb_pembelian")   
    tampil.execute(sql)
    data = tampil.fetchall()  
    t = PrettyTable(['Nomer','Nama_Pembeli','Nama_Games','Nomer_Telepon','Metode_Pembayaran','Status_Pembayaran'])   
    for Row in data:  
        t.add_row(Row)         
    print(t)
    print("="*107)
    
    

def Menambahkan(db):
    print("="*107)
    print(" "*46+"MENAMBAHKAN DATA:")
    print("="*107)
    Menampilkan(db)
    # nomer = int(input("Masukan Nomer urutan data berikutnya : "))
    
    namaPembeli = input("Masukan Nama : ")
    namaGames = input("Masukan Nama Games : ")   
    nomerTelepon = input("Masukkan Nomer Telepon : ") 
    metodePembayaran = input("Masukkan metode pembayaran yang dipilih : ")
    statusPembayaran = input("Berikan informasi status pembayaran : ")
        
    val = (namaPembeli,namaGames,nomerTelepon,metodePembayaran,statusPembayaran)
    tambah = db.cursor()
    sql = ("INSERT INTO tb_pembelian (Nama_Pembeli,Nama_Games,Nomer_Telepon,Metode_Pembayaran,Status_Pembayaran) values (%s,%s,%s,%s,%s)")   
    tambah.execute(sql, val)  
    db.commit()
    print("="*107)
    print("{} Data berhasil Di Input !".format(tambah.rowcount)) 
    print("="*107)

def Ubah(db):
    ubah = db.cursor()
    Menampilkan(db)
    nomer = int(input("Masukan pilihan nomer urutan data yang ingin diubah :"))
    print("1. Mengganti Nama saja")
    print("2. Mengganti Nama Game saja")
    print("3. Mengganti Nomer Telepon saja")
    print("4. Mengganti Metode Pembayaran saja")
    print("5. Mengganti Status Pembayaran saja")
    print("6. Mengganti seluruh bagian dari 1 data")
    beriPerintah = int(input("Masukkan perintah : "))
    if beriPerintah == 1:
        namaBaru = input("Masukkan Nama baru : ")

        val = (namaBaru, nomer)
        sql = ("UPDATE tb_pembelian SET Nama_Pembeli = %s WHERE Nomer = %s")
        ubah.execute(sql, val)
        db.commit()
        print("="*107)
        print("{} Data berhasil di Ubah !".format(ubah.rowcount))
        print("="*107)

    elif beriPerintah == 2:
        namaGame = input("Masukkan Nama Game baru : ")

        val = (namaGame, nomer)
        sql = ("UPDATE tb_pembelian SET Nama_Games = %s WHERE Nomer = %s")
        ubah.execute(sql, val)
        db.commit()
        print("="*107)
        print("{} Data berhasil di Ubah !".format(ubah.rowcount))
        print("="*107)

    elif beriPerintah == 3:
        nomerTelepon = input("Masukkan Nomer Telepon baru : ")

        val = (nomerTelepon, nomer)
        sql = ("UPDATE tb_pembelian SET Nomer_Telepon = %s WHERE Nomer = %s")
        ubah.execute(sql, val)
        db.commit()
        print("="*107)
        print("{} Data berhasil di Ubah !".format(ubah.rowcount))
        print("="*107)

    elif beriPerintah == 4:
        metodePembayaran = input("Masukkan Metode Pembayaran baru : ")

        val = (metodePembayaran, nomer)
        sql = ("UPDATE tb_pembelian SET Metode_Pembayaran = %s WHERE Nomer = %s")
        ubah.execute(sql, val)
        db.commit()
        print("="*107)
        print("{} Data berhasil di Ubah !".format(ubah.rowcount))
        print("="*107)

    elif beriPerintah == 5:
        statusPembayaran = input("Masukkan Status Pembayaran baru : ")

        val = (statusPembayaran, nomer)
        sql = ("UPDATE tb_pembelian SET Status_Pembayaran = %s WHERE Nomer = %s")
        ubah.execute(sql, val)
        db.commit()
        print("="*107)
        print("{} Data berhasil di Ubah !".format(ubah.rowcount))
        print("="*107)

    elif beriPerintah == 6:
        namaBaruy = input("Masukkan Nama baru : ")
        namaGamey = input("Masukkan Nama Game baru : ")
        nomerTelepony = input("Masukkan Nomer Telepon baru : ")
        metodePembayarany = input("Masukkan Metode Pembayaran baru : ")
        statusPembayarany = input("Masukkan Status pembayaran baru : ")

        val = (namaBaruy,namaGamey,nomerTelepony,metodePembayarany,statusPembayarany,nomer)
        sql = ("UPDATE tb_pembelian SET Nama_Pembeli = %s, Nama_Games = %s, Nomer_Telepon = %s, Metode_Pembayaran = %s, Status_Pembayaran = %s WHERE Nomer = %s")
        
        ubah.execute(sql,val)
        db.commit()
        print("="*107)
        print("{} Data berhasil di Ubah !".format(ubah.rowcount))
        print("="*107)

    else:
        print("Perintah Salah")
        Ubah(db)

def Hapus(db):
    hapus = db.cursor()
    print("="*107)
    print(" "*45+"MENGHAPUS DATA :")
    print("="*107)
    Menampilkan(db)
    nomer = int(input("Masukan Nomer urutan data yang akan dihapus : "))
    perintah = str(input("Apakah Anda yakin akan menghapus data tersebut ? (y/n) : "))
    
    if perintah == 'y':
        val = (nomer,)
        sql = ("DELETE FROM tb_pembelian WHERE Nomer = %s")
    
        hapus.execute(sql, val) 
        db.commit()
        print("="*107)
        print("{} Data berhasil Di Hapus !".format(hapus.rowcount))
        print("="*107)

    elif perintah == 'n':
        sql = ("DELETE FROM tb_pembelian WHERE Nomer = '%s'")
        val = (nomer)
        hapus.execute(sql, val) 
        db.commit()
        print("="*107)
        print("{} Data berhasil Di Hapus !".format(hapus.rowcount))
        print("="*107)

    else:
        print("perintah salah !")

def gameshop(db):
    print("\n\n\n")
    print("="*107)
    print(" "*45+"=== DATABASE ==="+" "*45)
    print("="*107)
    print("1. Tampilkan data pembeli")    
    print("2. Tambah data pembeli")
    print("3. Ubah data pembeli")
    print("4. Hapus data pembeli")
    print("0. Keluar{}")
    print("="*107)
    perintah = int(input("Masukan perintah : "))
    print("="*107)
    if perintah == 1:
        Menampilkan(db)
        
    elif perintah == 2:
        Menambahkan(db)
        
    elif perintah == 3:
        Ubah(db)

    elif perintah == 4:
        Hapus(db)
    
    elif perintah == 0:
        print("="*107)
        exit(" "*44+"=== ANDA KELUAR ==="+"\n"+"="*107)
        
    else:    
        print("perintah salah / tidak tersedia")

#ADMIN
# if __name__ == "__main__":
#     while (True):
#         gameshop(db)
def password(db):
    password = input("Masukkan Password : ")
    if password == 'hacker98':
        print("Anda adalah Admin !")
        print("="*107)
        gameshop(db)
        
    else:
        print("password anda salah !")
        


if __name__ == "__main__":
    while (True):
        gameshop(db)

   

    

        


    # gameshop_denastore = koneksi.cursor()
    # gameshop_denastore.execute("SELECT * FROM tb_pembelian")

    # data = gameshop_denastore.fetchall()
            
    # t=PrettyTable(['Nomer','Nama_Pembeli','Nama_Games','Nomer_Telepon','Metode_Pembayaran','Status_Pembayaran'])

    # for Row in data:
    #     t.add_row(Row)
                    
    #     print(t)       
    