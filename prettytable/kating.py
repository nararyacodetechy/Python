import mysql.connector 
from prettytable import PrettyTable



koneksi = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_gameshop'
) 

gameshop_denastore = koneksi.cursor()
gameshop_denastore.execute("SELECT * FROM tb_pembelian")

data = gameshop_denastore.fetchall()
            
t=PrettyTable(['Nomer','Nama_Pembeli','Nama_Games','Nomer_Telepon','Metode_Pembayaran','Status_Pembayaran'])

for Row in data:
    t.add_row(Row)
                    
print(t) 