# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # adalah assignment
print("\nnilai a :", a)

a += 4 # artinya a = a + 4
print("nilai a += 4, nilai a menjadi", a)

a -= 2 # artinya a = a - 2
print("nilai a -= 2, nilai a menjadi", a)

a *= 5 # artinya a = a * 5
print("nilai a *= 5, nilai a menjadi", a)

a /= 4 # artinya a = a / 4
print("nilai a /= 4, nilai a menjadi", a)

# modulus dan floor division
b = 20
print("\nnilai b :", b)
b %= 4 # artinya b = b % 4
print("nilai b %= 4, nilai b menjadi", b)

b = 20
print("nilai b :", b)
b //= 2 # artinya b = b // 2
print("nilai b //= 2, nilai b menjadi", b)

# pangkat / eksponen
b = 20
print("nilai b :", b)
b **= 4 # artinya b = b ** 4
print("nilai b **= 4, nilai b menjadi", b)

# operasi bitwise
# OR
c = True
print("\nnilai c :", c)
c |= False 
print("nilai c |= False, nilai c menjadi", c)
c = False
print("nilai c :", c)
c |= False 
print("nilai c |= False, nilai c menjadi", c)

# AND
c = True
print("\nnilai c :", c)
c &= False 
print("nilai c &= False, nilai c menjadi", c)
c = True
print("nilai c :", c)
c &= True 
print("nilai c &= True, nilai c menjadi", c)

# XOR
c = True
print("\nnilai c :", c)
c ^= False 
print("nilai c ^= False, nilai c menjadi", c)
c = True
print("nilai c :", c)
c ^= True 
print("nilai c ^= True, nilai c menjadi", c)

# geser geser 
d = 0b0100
print("\nnilai d =",format(d,"04b"))
d >>= 2
print("nilai d >>= 2, nilai d menjadi",format(d,"04b"))
d <<= 1
print("nilai d <<= 1, nilai d menjadi",format(d,"04b"))

