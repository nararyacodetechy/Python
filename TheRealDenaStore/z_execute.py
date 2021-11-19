def useradmin():
    print("="*107)
    print("Saya Ingin masuk sebagai : ")
    print("{}user")
    print("{}admin")
    print("{}exit")
    print("="*107)
    pengguna = str(input("Saya adalah : "))
    if pengguna =='user':
        print("="*107)
        print("Selamat Datang diToko Kami === DENASTORE === Silahkan memilih pilihan dibawah ini untuk menjalankan program")
        print("="*107)
        from databaseuser import koneksi, show_menu
        show_menu(koneksi)          
                
    elif pengguna =='admin':
        from database import db, password
        password(db)

    elif pengguna =='exit':
        exit()

    else:
        print("pengguna tidak tersedia")
        print("Apakah anda BOT ?")


if __name__ == "__main__":
    while (True):
        useradmin()




