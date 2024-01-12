# belajar casting 
# merubah dari satu tipe ke tipe lain
# tipe data = int, float, str, bool

# INTREGER
print("INTREGER")
data_int = 11
print("data =", data_int, "type =", type(data_int))

data_float  = float(data_int) 
data_str    = str(data_int)
data_bool   = bool(data_int) # akan false jika = 0
print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

## Float
print("FLOAT")
data_float = 3.5
print("data =", data_float, "type =", type(data_float))

data_int    = int(data_float) # akan dibulatkan ke bawah
data_str    = str(data_float)  
data_bool   = bool(data_float) # akan false jika = 0
print("data =", data_int, "type =", type(data_int))
print("data =", data_str, "type =", type(data_str))
print("data =", data_bool, "type =", type(data_bool))

# STRING
print("STRING")
data_str = "10"
print("data =", data_str, "type =", type(data_str))

data_float  = float(data_str) # str harus angka
data_int    = int(data_str) # str harus angka
data_bool   = bool(data_str) # akan false jika = 0/kosong
print("data =", data_float, "type =", type(data_float))
print("data =", data_int, "type =", type(data_int))
print("data =", data_bool, "type =", type(data_bool))

# BOOLEAN
print("BOOLEAN")
data_bool = True;
print("data =", data_bool, "type =", type(data_bool))

data_float  = float(data_bool) 
data_str    = str(data_bool)
data_int   = int(data_bool) 
print("data =", data_float, "type =", type(data_float))
print("data =", data_str, "type =", type(data_str))
print("data =", data_int, "type =", type(data_int))
