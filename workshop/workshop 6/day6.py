# array = []
# baru = int(input("Masukan angka : "))
# while baru >= 0 and baru <= 50:
    
#     array.append(baru)

#     print(array)


data=[]
while True:
    print("masukkan angka pada array hingga anda merasa cukup, tekan 'n' :")
    angka = input()
    if angka =='n':
        break
    data.append(int(angka))
print(data)

hasil = 0
for jumlah in data:
    hasil+=jumlah
print(hasil)

# data = []
# while True:
#     angka = input("Masukan angka pada array hingga anda merasa cukup, tekan 'n' : ")

#     data.append(int(angka))
#     if angka == 'n':
#         break 

# print(data)

# hasil = 0
# for jumblah in data:
#     hasil += jumblah
# print(hasil)

#NO13
#NO13
# data= []
# a=0
# while a != 'n' :
#     a=(input("masukkan nilai kedalam array, tekan n untuk berhenti = "))
#     data.append(a)
#     print(data)
