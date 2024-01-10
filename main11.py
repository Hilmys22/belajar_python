# operasi bitwise, biner, dan binary

a = 8
b = 4

# bitwise or
c = a | b
print("===OR===")
print("nilai =",a, " , binary =", format(a,"08b"))
print("nilai =",b, " , binary =", format(b,"08b"))
print("===|===")
print("nilai =",c,", binary =",format(c,"08b"))

# bitwise and 
c = a & b
print("===AND===")
print("nilai =",a," , binary =",format(a,("08b")))
print("nilai =",b," , binary =",format(b,("08b")))
print("===&===")
print("nilai =",c," , binary =",format(c,("08b")))

# bitwise xor 
c = a ^ b
print("===XOR===")
print("nilai =",a," , binary =",format(a,("08b")))
print("nilai =",b," , binary =",format(b,("08b")))
print("===^===")
print("nilai =",c," , binary =",format(c,("08b")))

# bitwise not 
c = ~a
print("===NOT===")
print("nilai =",a," , binary =",format(a,("08b")))
print("===~===")
print("nilai =",c," , binary =",format(c,("08b")))
# miror (xor)
print("===^===")
d = 0b0000001001
e = 0b1111111111
print("nilai =", e^d," , binary =",format(e^d,("08b")))

# shift right >>
c = a >> 2
print("===>>===")
print("nilai =",a," , binary =",format(a,("08b")))
print("===>>===")
print("nilai =",c," , binary =",format(c,("08b")))

# shift left <<
c = a << 2
print("===<<===")
print("nilai =",a," , binary =",format(a,("08b")))
print("===<<===")
print("nilai =",c," , binary =",format(c,("08b")))

