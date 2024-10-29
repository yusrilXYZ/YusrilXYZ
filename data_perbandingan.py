perbandingan = "i love perbandingan,belajar pyton"
print (perbandingan)
# data umur
umur_siswa = [18,21,17,20,22]

#memeriksa apakah ada siswa yang berumur lebih dari 21
if any(umur > 21 for umur in umur_siswa):
	print("ada siswa yang berumur lebih dari 21.")