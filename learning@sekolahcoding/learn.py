# 1
uang = input("berapa uang anda? ")

hutang = 100000

hasil = int(hutang - int(uang))


if int(uang) == int(hutang):
    print("terima kasih telah membayar... sekarang hutang anda sudah lunas!")
elif int(uang) >= int(hutang):
    print("terima kasih telah membayar... \nsisa uang kamu adalah = ",int(hasil))
else :
    print("jumblah yang kamu bayarkan belum memenuhi jublah hutang yang ada, mohon menyesuaikan jumblah uang dengan jumblah hutang anda! ")





# 2
# count = 0

# while count < 5:
#     print("yeyy")
#     count = count++1

# orang = ['agus', 'erina', 'roger']

# for nama in orang:
#     print("namanya adalah ",nama)
    
# text = "python"

# for huruf in text:
#     print("namanya adalah ",huruf)



# 3
# a = 1

# while a < 5:
#     b = 0
#     while b < a:
#         print("*", )
#         b = b + 1
#     print("")
#     a = a+1 


# 4

# for a in range(1,5):
#     for b in range(1,5):
#         c = a * b
#         print(c, end=" ")
#     print("")


# 5
# nama = ['agus','roki','tina']
# umur = [10,20,40,30]
# mixed = [2,'editor','gaming',3.6]

# nama.append('thomson')   #menambah data
# del umur[2]              #menghapus data
# nama[0]= "austin"        #mengganti data

# print(nama)



#6 
# dictionary 
# data = {'name': 'agus',
#         'age' : 18,
#         'hobby' : 'sing'}

# #menambah data dictionary
# data ['dream'] = 'singer'

# print("mimpinya adalah",data['dream'])   



#7 ngeloops data dictionary
# data = {'name': 'agus',
#         'age' : '18',
#         'hobby' : 'sing'}

# for key , value in data.items():
#     print(key + " - " + value + " - ")   



#8 dictionary bercabang
# data = {1 :{'name': 'agus','age' : '18','hobby' : 'sing'},
#         2 :{'name': 'roger','age' : '38','hobby' : 'drawing'}}

# print(data[2]['name'])



#9 ngeloops dictionary
# data = {1 :{'name': 'agus','age' : '18','hobby' : 'sing'},
#         2 :{'name': 'roger','age' : '38','hobby' : 'drawing'}}

# for key, value in data.items():
#     print("\nkeynya adalah", key)

#     for valuenya in value:
#         print(valuenya + " - ",value )


#10
# angka1 = {1,2,3,4,5}

# angka2 = {4,5,6,7,8}

# print(angka1 ^ angka2)



#11

# def yori(text = 'kosong'):
#     print('-------')
#     print(text)
#     print('-------')

# yori('belajar yuk')
# yori('jam pertama python')
# yori('jam kedua css')
# yori()


# #12
# def hitung(a, b):
#     print("hasil tambahnya adalah :", a + b)

# hitung(20,10)
# hitung(30,29)


# 13 parameter
# def printdata(name, hobby):
#     print("name="+name + " - hobby="+hobby)

# printdata(hobby = 'menyanyi',name = 'hilman')


# # 14
# def printdata(*name):
#     print(name)

# printdata('granger','hilman')




# 15
# def printdata(*args):
#     for name in args:
#         print(name)

# printdata('roger','hilman','surya','mona','arki')



# # 16
# def printdata(**kwargs):
#     for key, value in kwargs.items():
#         print(key + " - " + value)

# printdata(name = 'roger',age = '19',hobby = 'sing')



# #17 module import data

# person = {
#     "name":"hilman",
#     "age" : 20
# } 

# def printnama(name):
#     print("nama kamu adalah " + name)
