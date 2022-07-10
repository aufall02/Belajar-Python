#Casting data 
#Merubah dari satu tipe ke tipe data lain
#tipe data -> int,float,str,bool
#INTEGER
print("============INTEGER=========")
data_int = 9
print("data :",data_int,",type :",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)#akan false jika nilai int = 0
print("data :",data_float,",type :",type(data_float))
print("data :",data_str,",type :",type(data_str))
print("data :",data_bool,",type :",type(data_bool))


print("============FLOAT=========")
data_float = 0
print("data :",data_float,",type :",type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)#akan false jika nilai float = 0
print("data :",data_float,",type :",type(data_float))
print("data :",data_str,",type :",type(data_str))
print("data :",data_bool,",type :",type(data_bool))


print("============BOLLEAN=========")
data_bool = True
print("data :",data_bool,",type :",type(data_bool))

data_int   = int(data_bool)
data_str   = str(data_bool)
data_float = float(data_bool)
print("data :",data_float,",type :",type(data_float))
print("data :",data_str,",type :",type(data_str))
print("data :",data_float,",type :",type(data_float))



print("============STRING=========")
data_str = "10"
print("data :",data_str,",type :",type(data_str))

data_int   = int(data_str)#string harus angka
data_float = float(data_str)#string harus angka
data_bool  = bool(data_str)#jika string kosong maka akan false
print("data :",data_float,",type :",type(data_float))
print("data :",data_float,",type :",type(data_float))
print("data :",data_bool,",type :",type(data_bool))
