# matematika python

a = 2
b = 3

# Penjumlahan
hasil = a + b
print(a, '+', b, '=', hasil)

# Pengurangan
hasil = a - b
print(a, '-', b, '=', hasil)

# Perkalian
hasil = a * b
print(a, '*', b, '=', hasil)

# Pembagian
hasil = a / b
print(a, '/', b, '=', hasil)

# Pangkat
hasil = a ** b
print(a, '**', b, '=', hasil)

# Modulus/sisa pembagian
hasil = a % b
print(a, '%', b, '=', hasil)

# Bagi dobel/flour devision 
hasil = a // b
print(a, '//', b, '=', hasil)

# Operasi prioritas/presedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman2 * / ** %
'''


x = 3
y = 2
z = 5

hasil = x ** y * z - x / y + z % y
print(x,'**',y,'*',z,'-',x,'/',y,'+',z,'%',y, '=', hasil)

hasil = x * (y / z)
print(x,'*(',y,'/',z,')' '=',hasil)
