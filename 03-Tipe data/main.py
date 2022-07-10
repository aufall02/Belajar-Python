
#menampilkan tiipe data sebuah variable : type(nama_variable)

#Tipe data : angka satuan (integer)
from operator import truediv
from tkinter.tix import Form


data_integer = 1 
print("data integer :",data_integer,",bertipe :", type(data_integer))



#Tipe data : angka dengan (float)
data_float = 1.5
print("data float :",data_float,",bertipe :", type(data_float))


#Tipe data : kumpulan karakter (string)
data_string = "karakter"
print("data string :",data_string,",bertipe :", type(data_string))


#Tipe data : binner true/false (boolean)
data_bool = True
print("data bool :",data_bool,",bertipe :", type(data_bool))

#Tipe data : khusus



#bilangan compleks
data_compleks = complex(2,6)
print("data compleks :",data_compleks,",bertipe :", type(data_compleks))



#tipe data bahasa C

from ctypes import c_double
data_c_double = c_double(12.09)
print("data c_double :",data_c_double,",bertipe :", type(data_c_double))