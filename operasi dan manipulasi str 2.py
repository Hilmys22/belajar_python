# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

pagi = "selamat pagi"
print("normal = " + pagi)
pagi = pagi.upper()
print("upper = " + pagi)

# merubah semua ke lower case
siang = "SeLaMaT SianG"
print("normal = " + siang)
siang = siang.lower()
print("lower = " + siang)

## pengecekan dengan isX method

# contoh pengecekan lower case dan upper case
sapaan = "hai"
apakah_lower = sapaan.islower() # hasilnya boolean
print(sapaan + " is lower = " + str(apakah_lower))
apakah_upper = sapaan.isupper() # hasilnya boolean
print(sapaan + " is upper = " + str(apakah_upper))

jawaban = "HAI JUGA"
apakah_upper = jawaban.isupper() # hasilnya bool
print(jawaban + " is upper = " + str(apakah_upper))
apakah_lower = jawaban.islower() # hasilnya bool
print(jawaban + " is lower = " + str(apakah_lower))

# isalpha() <-- untuk mengecek semua huruf

alpha = "agusjuaralombamenyanyi".isalpha()
print("is alpha = " + str(alpha))

# isalnum() <-- untuk mengecek huruf dan angka

alnum = "juara01".isalnum()
print("is alnum = " + str(alnum))

# isdecimal() <-- untuk mengecek angka saja

decimal = "125".isdecimal()
print("is decimal = " + str(decimal))

# isspace() <-- untuk mengecek spasi, tab, newlin (\n)
space = "apakah ada orang disini".isspace()
print("is space = " + str(space))

# istitle() <-- semua kata dimulai dengan huruf besar

judul = "Yo Wis Ben"
cek_judul = judul.istitle() # hasilnya bool
print(judul + " is title = " + str(cek_judul))

## mengecek komponen startwith() endwitdh() 
cek_start = "jagoan neon".startswith("jagoan")
print("start = " + str(cek_start))

cek_end = "jagoan neon".endswith("neon")
print("start = " + str(cek_end))

## penggabungan komponen join() splith()
pisah = ['aku','suka','sama','kamu'] # intinya list adalah kumpulan data
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuemmtidakemmsuka" 
print(gabungan.split('emm'))

# alokasi karakter rjust(), ljust(), center()

right = "right".rjust(10)
print("'"+right+"'") 

left = "left".ljust(10,"=")
print("'"+left+"'") 

center = "center".center(10)
print("'"+center+"'") 

# kebalikannya -> strip()
left = "left".strip("=") # menghilangkan tanda 
print("'"+left+"'") 

