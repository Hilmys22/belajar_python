# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,/=,is,is not

x = 8
y = 6

# lebih besar dari >
print("Lebih Besar Dari")
hasil = x > 3
print(x,'>',3,'=',hasil)
hasil = y > 6
print(y,'>',6,'=',hasil)

# kurang dari <
print("Kurang Dari")
hasil = x < 3
print(x,'<',3,'=',hasil)
hasil = y < 6
print(y,'<',6,'=',hasil)

# lebih dari sama dengan >=
print("Lebih Dari Sama Dengan")
hasil = x >= 3
print(x,'>=',3,'=',hasil)
hasil = y >= 6
print(y,'>=',6,'=',hasil)

# tidak lebih dari sama dengan <=
print("tidak lebih Dari Sama Dengan")
hasil = x <= 3
print(x,'<=',3,'=',hasil)
hasil = y <= 6
print(y,'<=',6,'=',hasil)

# sama dengan ==
print(" Sama Dengan")
hasil = x == 3
print(x,'==',3,'=',hasil)
hasil = y == 6
print(y,'==',6,'=',hasil)

# tidak sama dengan ==
print(" tidak Sama Dengan")
hasil = x != 3
print(x,'!=',3,'=',hasil)
hasil = y != 6
print(y,'!=',6,'=',hasil)

# is sebagai komparasi object identity

x = 5 # ini adalah assigment membuat object
y = 7
print('nilai x =',x, 'id =',hex(id(x)) )
print('nilai x =',y, 'id =',hex(id(y)) )
hasil = x is y
print('x is y =',hasil)

x = 5 # ini adalah assigment membuat object
y = 6
print('nilai x =',x, 'id =',hex(id(x)) )
print('nilai x =',y, 'id =',hex(id(y)) )
hasil = x is not y
print('x is y =',hasil)
