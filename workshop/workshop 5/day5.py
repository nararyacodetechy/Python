# IF ELSE STATEMENT

# Nomer 1
# input_angka = input("masukan angka : ")
# if int(input_angka) % 2 == 0 :
#     print("angka yang anda masukan adalah angka genap")
# else:
#     print("angka yang anda masukan adalah angka ganjil")


# nomer 2
# input_angka_untuk_bulan = int(input("masukan angka untuk menentukan bulan: "))

# if input_angka_untuk_bulan == 1 :
#     print("januari")
# elif input_angka_untuk_bulan == 2 :
#     print("februari")
# elif input_angka_untuk_bulan == 3 :
#     print("maret")
# elif input_angka_untuk_bulan == 4 :
#     print("april")
# elif input_angka_untuk_bulan == 5 :
#     print("mei")
# elif input_angka_untuk_bulan == 6 :
#     print("juni")
# elif input_angka_untuk_bulan == 7 :
#     print("juli")
# elif input_angka_untuk_bulan == 8 :
#     print("agustus")
# elif input_angka_untuk_bulan == 9 :
#     print("september")
# elif input_angka_untuk_bulan == 10 :
#     print("oktober")
# elif input_angka_untuk_bulan == 11:
#     print("november")
# elif input_angka_untuk_bulan == 12:
#     print("desember")
# else:
#     print("nama bulan tidak diketahui")
    

# Nomer 3

# a = int(input("masukan jam untuk menentukan salam: "))

# if a >= 3 and a <= 10 :
#     print("Selamat Pagi")
# elif a >= 11 and a <= 14  :
#     print("Selamat Siang")
# elif a >= 15  and a <= 18  :
#     print("Selamat Sore")
# else:
#     print("Selamat Malam")



# Nomer 4
# input_pelanggan = str(input("apakah anda adalah pelanggan ?(Y / X) : "))

# if input_pelanggan == 'Y':
#     n = int(input("inputkan jumblah fotocopy : "))
#     lembar = 75 * n
#     print("anda hanya perlu membayar : ",lembar)

# elif input_pelanggan == 'X':
#     n = int(input("inputkan jumblah fotocopy : "))
    
#     if n >= 0 and n < 100:
#         harga = 150 * n
#         print("anda perlu membayar : ",harga)
#     elif n >= 100  and n <= 200:
#         harga = 100 * n
#         print("anda perlu membayar : ",harga)
#     elif n > 200:
#         harga = 80 * n
#         print("anda perlu membayar : ",harga)
#     else:
#         print("lembar tidak tersedia")




# NUMERIC ARRAY


# Nomer 1 menampilkan isi data
# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# print("Banyaknya nama mahasiswa dalam data adalah : ", len(data_mahasiswa))

# Nomer 2 
# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# print(data_mahasiswa[3])

# data_mahasiswa = ['Nama-nama Mahasiswa :','1.) Bagus Nararya','2.) Tomi','3.) Franky','4.) Tasya','5.) Rhara']
# for i in data_mahasiswa:
#     print(i)
# banyak = len(data_mahasiswa)
# inputuser = int(input("masukan indeks mahasiswa : "))

# if inputuser >= 1 and inputuser <  banyak:
#     print(data_mahasiswa[inputuser])
# else:
#     print("tidak ada")


# Nomer 3 menambahkan data baru
# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# data_mahasiswa.append('Tatsumi')
# print(data_mahasiswa)

# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# for i in data_mahasiswa:
#     print(i)
# print("="*100)
# print("tambahkan mahasiswa baru : ")

# baru = input()
# data_mahasiswa.append(baru)
# print("="*100)

# for j in data_mahasiswa:
#     print(j)
# print("="*100)



# Nomer 4 menghapus isi data lama
# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# data_mahasiswa.remove('Tomi')
# print(data_mahasiswa)

# cara menghapus menggunakan string(nama):
# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# for i in data_mahasiswa:
#     print(i)
# print("="*100)
# print("masukan mahasiswa yang akan dihapus : ")

# lama = str(input())
# data_mahasiswa.remove(lama)
# print("="*100)

# for j in data_mahasiswa:
#     print(j)
# print("="*100)



# cara menghapus menggunakan integer(indeks):
# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# for i in data_mahasiswa:
#     print(i)
# print("="*100)
# print("masukan indeks mahasiswa yang akan dihapus : ")

# lama = str(input())
# data_mahasiswa.pop(0)
# print("="*100)

# for j in data_mahasiswa:
#     print(j)
# print("="*100)

# Nomer 5 mengganti isi data 
# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# data_mahasiswa[2]=('franko')
# print(data_mahasiswa)

# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# for i in data_mahasiswa:
#     print(i)
# baru = str(input("masukan nama baru : "))
# indeks_baru = int(input("masukan indeks baru : "))
# data_mahasiswa[indeks_baru] = (baru)
# print(data_mahasiswa)

# Nomer 6
# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# ascending = sorted(data_mahasiswa)
# print(ascending)

# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# descending = sorted(data_mahasiswa, reverse=True)
# print(descending)

# data_mahasiswa = ['Bagus Nararya','Tomi','Franky','Tasya','Rhara']
# print("="*100)
# print("Ubah urutan Data")
# print("="*100)

# for i in data_mahasiswa:
#     print(i)
# print("="*100)
# print("ascending = 1")
# print("descending = 2")
# print("="*100)

# pilihan = int(input("Masukan angka untuk menentukan ASC atau DESC :"))
# if pilihan == 1 :
#     ascending = sorted(data_mahasiswa)
#     for i in ascending:
#         print(i)
#     print("="*100)
# elif pilihan == 2:
#     descending = sorted(data_mahasiswa, reverse=True)
#     for i in descending:
#         print(i)
#     print("="*100)
# else:
#     print("="*100)
#     print("Gagal mengurutkan data!")
#     print("="*100)



# ASSOSIATIVE ARRAY

#Nomer 1
data_mahasiswa ={   'Bagus Nararya' :  {'Nama':'Bagus Nararya','NIM':'42030064','Jurusan':'Teknologi Informasi'}, 
                    'Tomi': {'Nama':'Tomi','NIM':'42030065','Jurusan':'Teknologi Informasi'}, 
                    'Franky' : {'Nama':'Franky','NIM':'42030066','Jurusan':'Teknologi Informasi'}, 
                    'Tasya' : {'Nama':'Tasya','NIM':'42030067','Jurusan':'Teknologi Informasi'}, 
                    'Rhara' : {'Nama':'Rhara','NIM':'42030068','Jurusan':'Teknologi Informasi'}
                }     
print("masukan nama yang akan dirubah : ")
indeksRubah = input()
print("nama yang diinginkan : ")
namaRubah = input()

# print("ingin merubah NIM dan Jurusan ? 'Ya' atau 'Tidak'")
# jika = input()

# if (jika == 'Ya'):
#     print("umurnya : ")
#     nimRubah = int(input())
#     print("jurusannya : ")
#     jurusanRubah = str(input())
#     data_mahasiswa[indeksRubah] = {"nama": namaRubah, "NIM": nimRubah, "jurusan":jurusanRubah}
# elif(jika == 'Tidak'):
#     data_mahasiswa[indeksRubah]['nama'] = namaRubah

# print(data_mahasiswa)


# data_mahasiswa ={'Bagus Nararya' :  {'Nama':'Bagus Nararya','NIM':'42030064','Jurusan':'Teknologi Informasi'}, 
#     'Tomi': {'Nama':'Tomi','NIM':'42030065','Jurusan':'Teknologi Informasi'}, 
#     'Franky' : {'Nama':'Franky','NIM':'42030066','Jurusan':'Teknologi Informasi'}, 
#     'Tasya' : {'Nama':'Tasya','NIM':'42030067','Jurusan':'Teknologi Informasi'}, 
#     'Rhara' : {'Nama':'Rhara','NIM':'42030068','Jurusan':'Teknologi Informasi'}
#     }    


# print(data_mahasiswa)

#Nomer 2



