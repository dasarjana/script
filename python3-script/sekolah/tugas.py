import home, time
def tugas():
	catats = open("tugas.txt", "r+")
	catat = catats.read()
	print (catat)
	sapa = input("Enter Untuk Melanjutkan #")
	if sapa == "" :
		nama = str(input("Sebutkan nama kamu :"))
		isi = str(input("Tulis tugas.\n"))

		data = ("\nNama: {}\nTugas: {}\n---".format(nama, isi))

		catats.write(data)

		catats.close()

		main()
	else:
		main()

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
	print("                                 Semua Tugas              ")
	print("1. Buat Tugas Baru")
	print("2. Kembali Ke Home")
	print("0. Keluar            ")
	print("======================================================================")

	pilih = str(input("Pilihan anda : #"))

	if pilih == "1":
		tugas()
	elif pilih == "2":
		time.sleep(1)
		home.main()
	elif pilih == "0":
		exit()
	else:
		print("Jangan asal ngetik oii")
		main2()