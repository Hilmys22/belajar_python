# operasi logika / boolean

# not, or, and

# NOT
print("NOT")
a = False
c = not a
print('data a =',a)
print("Hasilnya")
print('data c =',c)

# OR jika salah satu true maka hasilnya true
print("OR")
a = False
b = False
c = a or b
print(a,'or',b,'=',c)
a = True
b = False
c = a or b
print(a,'or',b,'=',c)
a = False
b = True
c = a or b
print(a,'or',b,'=',c)
a = True
b = True
c = a or b
print(a,'or',b,'=',c)

# AND jika salah satu false maka hasilnya false
print("AND")
a = False
b = False
c = a and b
print(a,'and',b,'=',c)
a = True
b = False
c = a and b
print(a,'and',b,'=',c)
a = False
b = True
c = a and b
print(a,'and',b,'=',c)
a = True
b = True
c = a and b
print(a,'and',b,'=',c)

# XOR akan true jika salah satu true maka hasilnya true
print("XOR")
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'xor',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'xor',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'xor',b,'=',c)
