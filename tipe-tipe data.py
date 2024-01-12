# a = 10 , a adalah variabel dengan nilai 10
# tipe data angka stauan yang tidak ada koma = integer

data_integer = 1111
print("data :", data_integer)
print("-bertipe :", type(data_integer))

# tipe data angaka dengan koma = float
data_float = 2.5
print("data :", data_float)
print("-bertipe :", type(data_float))

# tipe data kumpulan karakter = string
data_string = "ahma"
print("data :", data_string)
print("-bertipe :", type(data_string))

# tipe data benar/salah = boolean
data_bool = False;
print("data :", data_bool)
print("-bertipe :", type(data_bool))

# tipe data khusus = complex
data_complex = complex(1,2)
print("data :", data_complex)
print("-bertipe :", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double 
data_c_double = c_double(12.6)
print("data :", data_c_double)
print("- bertipe :", type(data_c_double))
