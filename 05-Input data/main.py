#belajar inpu =t data user

data = input("masukkan data: ")
print("data : ",data,",tipe data = ",type(data))

#jika kita ingin mengambil data int
angka1 = int(input("masukkan angka1 :"))
angka2 = float(input("masukkan angka2 :"))
print("angka1 : ",angka1,",tipe data : ",type(angka1))
print("angka2 : ",angka2,",tipe data : ",type(angka2))

#boolean 
binner = bool(int(input("masukkan binner : ")))#untuk boollean harus di ubah ke integer dulu
print("binner : ",binner,",tipe data : ",type(binner))