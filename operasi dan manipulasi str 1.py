# operasi dan manipulasi string 

# 1. menyambung string (concatenate)
nama_pertama = "ahmad"
nama_tengah = "hilmy"
nama_akhir = "santoso"

nama_lengkap = nama_pertama +" "+ nama_tengah +" "+ nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string (len)
panjang = len(nama_lengkap)
print("panjang dari :" + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char/string di string

d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print("string " + D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string 
print("wk"*5)
print(10*"wk")

# indexing (mulai dari 0 )
print("index ke- " + nama_lengkap[0])
print("index ke- " + nama_lengkap[9])
print("index ke- " + nama_lengkap[-1])
print("index ke- " + nama_lengkap[-7])
print("index ke- " + nama_lengkap[0:8])
print("index ke- " + nama_lengkap[9:15])
print("index ke- " + nama_lengkap[0:10:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah "+ chr(data))

# 4 operator dalam method

data = "aku sedang makan"
jumlah = data.count("a")
print("jumlah a pada " + data + " = " + str(jumlah))
