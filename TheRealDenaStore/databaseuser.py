#DATABASE USER
from z_execute import useradmin
import mysql.connector

from prettytable import PrettyTable
from database import db, gameshop  
        
koneksi = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_gameshop'
) 

def tampilkan(koneksi):
    print("="*107)
    print(" "*44+"MENAMPILKAN DATA:")
    print("="*107)
    tampil = koneksi.cursor()
    sql = ("SELECT * FROM tb_beli_games")   
    tampil.execute(sql)
    data = tampil.fetchall()  
    t = PrettyTable(['Nomer','Daftar_Games','Genre_Games','Platform_Games','Harga'])   
    for Row in data:  
        t.add_row(Row)         
    print(t)
    print("="*107)
    print("pilih untuk membeli game : ")
    beli_games = int(input("Masukan angka pilihan : "))
    print("="*107)
    if beli_games == 1:
        from database import db, Menambahkan
        
        print("Metode Pembayaran yang tersedia : ")
        print("1. Dana")
        print("2. Gopay")
        print("3. Cash On Delevery")
        print("Anda akan membeli Game GTA San Andreas. Inputkan data diri anda : ")
            
        namaPembeli = input("Masukan Nama : ")
        namaGames = input("Masukan Nama Games lagi : ")   
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

        print("Selesaikan Pembayaran segera... \npesanan akan dikirim segera jika anda telah melakukan pembayaran!")
    elif beli_games == 2:
        from database import db, Menambahkan
        
        print("Metode Pembayaran yang tersedia : ")
        print("1. Dana")
        print("2. Gopay")
        print("3. Cash On Delevery")
        print("Anda akan membeli Game Assassins Creed Identify. Inputkan data diri anda : ")
            
        namaPembeli = input("Masukan Nama : ")
        namaGames = input("Masukan Nama Games lagi : ")   
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

        print("Selesaikan Pembayaran segera... \npesanan akan dikirim segera jika anda telah melakukan pembayaran!")
    
    elif beli_games == 3:
        from database import db, Menambahkan
        
        print("Metode Pembayaran yang tersedia : ")
        print("1. Dana")
        print("2. Gopay")
        print("3. Cash On Delevery")
        print("Anda akan membeli Game God of War II (2007). Inputkan data diri anda : ")
            
        namaPembeli = input("Masukan Nama : ")
        namaGames = input("Masukan Nama Games lagi : ")   
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

        print("Selesaikan Pembayaran segera... \npesanan akan dikirim segera jika anda telah melakukan pembayaran!")
    elif beli_games == 4:
        from database import db, Menambahkan
        
        print("Metode Pembayaran yang tersedia : ")
        print("1. Dana")
        print("2. Gopay")
        print("3. Cash On Delevery")
        print("Anda akan membeli Game Final Fantasy X (2001). Inputkan data diri anda : ")
            
        namaPembeli = input("Masukan Nama : ")
        namaGames = input("Masukan Nama Games lagi : ")   
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

        print("Selesaikan Pembayaran segera... \npesanan akan dikirim segera jika anda telah melakukan pembayaran!")
    elif beli_games == 5:
        from database import db, Menambahkan
        
        print("Metode Pembayaran yang tersedia : ")
        print("1. Dana")
        print("2. Gopay")
        print("3. Cash On Delevery")
        print("Anda akan membeli Game Residen Evil 4 (2005). Inputkan data diri anda : ")
            
        namaPembeli = input("Masukan Nama : ")
        namaGames = input("Masukan Nama Games lagi : ")   
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

        print("Selesaikan Pembayaran segera... \npesanan akan dikirim segera jika anda telah melakukan pembayaran!")
    elif beli_games == 6:
        from database import db, Menambahkan
        
        print("Metode Pembayaran yang tersedia : ")
        print("1. Dana")
        print("2. Gopay")
        print("3. Cash On Delevery")
        print("Anda akan membeli Game Minecraft. Inputkan data diri anda : ")
            
        namaPembeli = input("Masukan Nama : ")
        namaGames = input("Masukan Nama Games lagi : ")   
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

        print("Selesaikan Pembayaran segera... \npesanan akan dikirim segera jika anda telah melakukan pembayaran!")
    elif beli_games == 7:
        from database import db, Menambahkan
        
        print("Metode Pembayaran yang tersedia : ")
        print("1. Dana")
        print("2. Gopay")
        print("3. Cash On Delevery")
        print("Anda akan membeli Game Ultimate Spiderman. Inputkan data diri anda : ")
            
        namaPembeli = input("Masukan Nama : ")
        namaGames = input("Masukan Nama Games lagi : ")   
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

        print("Selesaikan Pembayaran segera... \npesanan akan dikirim segera jika anda telah melakukan pembayaran!")
    elif beli_games == 8:
        from database import db, Menambahkan
        
        print("Metode Pembayaran yang tersedia : ")
        print("1. Dana")
        print("2. Gopay")
        print("3. Cash On Delevery")
        print("Anda akan membeli Game Real Fishing Ace Pro Wild Tropy. Inputkan data diri anda : ")
            
        namaPembeli = input("Masukan Nama : ")
        namaGames = input("Masukan Nama Games lagi : ")   
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

        print("Selesaikan Pembayaran segera... \npesanan akan dikirim segera jika anda telah melakukan pembayaran!")
    elif beli_games == 9:
        from database import db, Menambahkan
        
        print("Metode Pembayaran yang tersedia : ")
        print("1. Dana")
        print("2. Gopay")
        print("3. Cash On Delevery")
        print("Anda akan membeli Game Football Manager 2019. Inputkan data diri anda : ")
            
        namaPembeli = input("Masukan Nama : ")
        namaGames = input("Masukan Nama Games lagi : ")   
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

        print("Selesaikan Pembayaran segera... \npesanan akan dikirim segera jika anda telah melakukan pembayaran!")
    elif beli_games == 10:
        from database import db, Menambahkan
        
        print("Metode Pembayaran yang tersedia : ")
        print("1. Dana")
        print("2. Gopay")
        print("3. Cash On Delevery")
        print("Anda akan membeli Game Hitman Sniper. Inputkan data diri anda : ")
            
        namaPembeli = input("Masukan Nama : ")
        namaGames = input("Masukan Nama Games lagi : ")   
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
        print("Selesaikan Pembayaran segera... \npesanan akan dikirim segera jika anda telah melakukan pembayaran!")
    elif beli_games==0:
        exit()
    else:
        print("Tidak Tersedia")
def show_menu(koneksi):
    print(" "*45+"=== DENASTORE ==="+" "*45)
    print("="*107)
    print("1. Tampilkan Daftar Games")    
    print("0. Keluar{}")
    print("="*107)
    perintah = int(input("Masukan perintah : "))
    print("="*107)
    if perintah == 1:
        tampilkan(koneksi)
            
    elif perintah == 0:
        print("="*107)
        exit(" "*44+"=== ANDA KELUAR ==="+"\n"+"="*107)
                
    else:    
        print("perintah salah / tidak tersedia")
 
if __name__ == "__main__":
    while (True):
        show_menu(koneksi)


