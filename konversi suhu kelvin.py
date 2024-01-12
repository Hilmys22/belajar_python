# Konversi Kelvin Ke Yang Lain

kelvin = float(input("Masukkan Suhu :"))
print("Suhu adalah :", kelvin,"K")

reumur = 4/5 * (kelvin - 273)
print("Suhu dalam reumur :", reumur,"R")

farenheit = (9/5 * (kelvin - 273)) + 32
print("Suhu dalam farenheit :",farenheit,"F")

celcius = kelvin - 273
print("Suhu dalam celcius :", celcius,"C")
