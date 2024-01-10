data = 'ini adalah string'
print(data)
print(type(data))
# 1. cara membuat string (str)

'''
    1. dengan menggunakan singgle quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'dengan menggunakan singgle quote'
print(data)
data = "dengan menggunakan double quote"
print(data)

print('"Hai bagaimana kabarmu?"')
print("'Hai bagaimana kabarmu?'")
print("sekarang adalah hari jum'at")

# 2. menggunakan tanda |

# membuat tanda ' menjadi string (str)
print('mari sholat jum\'at')
print('g\'day isn\'t it?')

# backslash
print("C:\\user\\Ahmad")

# tab 
print("fajar\t\t\t\t\twulan, semakin berjauhan")

# backspcace
print("dimas \bsakit")

# newline
print('baris pertama \nbaris kedua') # LF line feed -> unix, macos, linux
print('baris pertama \rbaris kedua') # CR carriage return -> commodore, acorn, lisp
print('baris pertama \r\nbaris kedua') # CRLF line feed carriage return -> windows

# string literal / raw
print('C:\new folder') # akan salah pathnya

# menggunakan raw
print(r'C:\new \t\b\nfolder') # menulis sesuka hati 

# multiline string
print("""
Nama : ahmad
Kelas: 12 
""")

# multiline string dan raw
print("""
Nama    : ahmad hilmy s
Kelas   : xii 12 tkj 2
website : www.ahmad.com/portofolio    
""")
