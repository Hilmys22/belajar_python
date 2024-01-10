# Soal 1
 
# ----0++++5----8++++11----

inputuser = float(input("Masukkan angka "))
#----0++++
islebihdari = (inputuser > 0)
print("lebih dari 0 =",islebihdari)
#++++5----
iskurangdari = (inputuser < 5)
print("kurang dari 5 =", iskurangdari)

iscorect = islebihdari and iskurangdari
print("hasi 0-5 =", iscorect)

inputuser = float(input("Masukkan angka "))
#++++5----
islebihdari = (inputuser > 5)
print("lebih dari 5 =",islebihdari)
#----11++++
iskurangdari = (inputuser < 11)
print("kurang dari 11 =", iskurangdari)

iscorect = islebihdari or iskurangdari
print("hasi 5-11 =", iscorect)

inputuser = float(input("Masukkan angka "))
#----8++++
islebihdari = (inputuser > 8)
print("lebih dari 8 =",islebihdari)
#++++11----
iskurangdari = (inputuser < 11)
print("kurang dari 11 =",iskurangdari)

iscorect = islebihdari and iskurangdari
print("hasil 8-11 =", iscorect)