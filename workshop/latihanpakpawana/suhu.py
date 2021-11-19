# tayo = (input("Masukan Code akses Anda : "))
# if tayo == 'hacker0220':
#     print("="*100)
#     print("anda adalah hacker! silahkan mengakses")
#     print("="*100)

   
# else:
#     print("="*100)
#     print("maaf... anda bukan golongan kami!")
#     print("="*100)

    

print("Saya ingin mengkonversi suhu derajat:\n1. Celcius ke Fahrenheit\n2. Fahrenheit ke Celcius")
tanya = int(input("Masukan Nomer perintah : "))

if tanya == 1:
    celcius = int(input("Masukan suhu Celcius : "))
    fahrenheit = (celcius * (9/5)) + 32
    print(fahrenheit,"`F")

elif tanya == 2:
    fahrenheits = int(input("Masukan suhu Fahrenheit : "))
    celciuss = (fahrenheits - 32) * (5/9)
    print((celciuss),"`C")

else:
    print("Perintah Salah !")