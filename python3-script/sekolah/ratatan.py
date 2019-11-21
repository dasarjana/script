import home, time, getpass
def ratat():
	catats = open("ratat.txt", "r+")
	catat = catats.read()
	print (catat)

	pwd = getpass.getpass("Maaf,, disini terdapat Password.(Enter) #")
	if pwd == "vii":
		isi = str(input("Menulis catatan.\n"))

		data = ("\nNama: {}\nCatatan: {}\n---".format(nama, isi))

		catats.write(data)

		catats.close()

		main()
	elif pwd == "":
		main()
	else:
		ratat()

def main2():
	pilih = str(input("Pilihan anda : #"))

	if pilih == "1":
		catat()
	elif pilih == "2":
		home.main()
	elif pilih == "0":
		exit()
	else:
		print("Jangan asal ngetik oii")	
		main3()

def main3():
	pilih = str(input("Pilihan anda : #"))

	if pilih == "1":
		catat()
	elif pilih == "2":
		home.main()
	elif pilih == "0":
		exit()
	else:
		print("Jangan asal ngetik oii")	
		main()

def main():
	print("===================================================================")
	print("             Selamat Datang Di Aplikasi GGG	(Guna Ga Guna)")
	print("===================================================================")
	print("                                Catatan Ravi              ")
	print("1. Buat Tugas Baru")
	print("2. Kembali Ke Home")	
	print("0. Keluar            ")
	print("======================================================================")

	pilih = str(input("Pilihan anda : #"))

	if pilih == "1":
		ratat()
	elif pilih == "2":
		time.sleep(1)
		home.main()
	elif pilih == "0":
		exit()
	else:
		print("Jangan asal ngetik oii")	
		main2()
  
	# print ("Selamat datang di Program Biodata")
	# print "================================="

	# # buka file untuk dibaca dan ditulis
	# file_bio = open("biodata.txt", "r+")

	# teks = file_bio.read()

	# # cetak isi file
	# print teks

	# # Ambil input dari user
	# nama = raw_input("Nama: ")
	# umur = input("Umur: ")
	# alamat = raw_input("Alamat: ")

	# # format teks
	# teks = "\nNama: {}\nUmur: {}\nAlamat: {}\n---".format(nama, umur, alamat)

	# # tulis teks ke file
	# file_bio.write(teks)

	# # tutup file
	# file_bio.close()