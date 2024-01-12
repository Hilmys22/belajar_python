# soal 2

# ++++0----5++++8----11++++

inputuser = float(input("masukkan angka ="))
#++++0----
iskurangdari = (inputuser < 0)
print("kurang dari 0 =", iskurangdari)
#----5++++
islebihdari = (inputuser > 5)
print("lebih dari 5 =", islebihdari)

iscorect = iskurangdari or islebihdari
print("hasil 0-5 =", iscorect)

inputuser = float(input("masukkan angka ="))
#----5++++
islebihdari = (inputuser > 5)
print("lebih dari 5 =",islebihdari)
#++++8----
iskurangdari = (inputuser < 8)
print("kurang dari 8 =",iskurangdari)

iscorect = islebihdari and iskurangdari
print("hasil 5-8 =",iscorect)

inputuser = float(input("masukkan angka "))
#++++8----
iskurangdari = inputuser < 8
print("kurang dari 8 =", iskurangdari)
#----11++++
islebihdari = inputuser > 11 
print("lebih dari 11 =", islebihdari)

iscorect = iskurangdari or islebihdari
print("hasil 8-11 =", iscorect)
