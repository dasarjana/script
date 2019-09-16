import catatan, tugas, ratatan, time
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
	print("                                     #HOME              ")
	print("1. Lihat Catatan Ravi")
	print("2. Lihat Semua Catatan")
	print("3. Lihat Semua Tugas")
	print("0. Keluar            ")
	print("======================================================================")

	pilih = str(input("Pilihan anda : #"))
	if pilih == "1":
		time.sleep(2)
		ratatan.main()
	elif pilih == "2":
		time.sleep(2)
		catatan.main()
	elif pilih == "3":
		time.sleep(2)
		tugas.main()
	elif pilih == "0":
		exit()
	else:
		print("Jangan asal ngetik oii")	
		main2()

if __name__== "__main__":
  main()