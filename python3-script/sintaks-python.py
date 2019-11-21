# Statement
nama = "Vii"
if True:
	pass
if False:
	pass

#Multi-line Statement
angka = 	['1', '2', '3',
'4', '5', '6',
'7', '8', '9',]

jumlah = 11 + 29 + \
90 * 4 / \
22 - 12

#Pengusun Kode
#Contoh Benar
nama = "Vii"
if nama == "Vii":
	print("Selamat Datang Ravi")
else:
	print("Siapa Nama Anda ?")

#Contoh Salah
nama = "Hawa"
if nama == "Vii":
print("Selamat Datang Ravi")#Untuk memperbaikinya silakan tambahkan spasi dibaris ini
else:
	print("Siapa Nama Anda ?")

"""
Akan ada peringatan
SyntaxError: unexpected indent
"""

#Penggunaan Kalimat(string)
alamat = "Indonesia"
nama = 'wawa(n)'
isi = '''Ini dapat
berupa
beberapa
baris'''
isi2 = """Ini
juga dapat
berupa
beberapa
baris"""

#Penggunaan Komentar
print("Hai manusia") #ini menampilkan teks Hai manusia

TentangData()#Perintah ini tidak dapat dijalankan

"""TentangData() jika kamu menjalankan kode program ini, maka akan ada peringatan
NameError: name 'TentangData' is not defined"""