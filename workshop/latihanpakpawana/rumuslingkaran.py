# Lingkaran
print("Saya ingin menghitung : ")
print("1. Luas lingkaran ")
print("2. Jari - jari lingkaran")
print("3. diameter lingkaran")
print("4. Keliling lingkaran")
tanya = int(input("Masukan Nomer perintah : "))

if tanya == 1:
    inputjari = int(input("Masukkan jari-jari lingkaran : "))

    luaslingkaran = 3.14 * (inputjari*inputjari)
    print(luaslingkaran)
    
elif tanya == 2:
    inputdiameter = int(input("Masukkan diameter lingkaran : "))

    jarijari = inputdiameter / 2
    print(jarijari)

elif tanya == 3:
    inputjari = int(input("Masukkan jari-jari lingkaran : "))

    diameter = inputjari + inputjari
    print(diameter)
    
elif tanya == 4:
    inputjari = int(input("Masukkan jari-jari lingkaran : "))
    kelilinglingkaran = 2 * 3.14 * inputjari
    print(kelilinglingkaran)

else:
    print('perintah salah')



# luaslingkaran = 3.14 * (inputjari * inputjari)
# jarijari = inputluaslingkaran / 3.14
# diameter = luaslingkaran / (inputjari * inputjari)