nama = str(input('MASUKAN NAMA SISWA = '))
umur = int(input('MASUKAN UMUR SISWA = '))
list_pekerjaan = ['petani', 'pengangguran', 'nelayan', 'kapal laut']
pekerjaan_orang_tua = str(input('MASUKAN PEKERJAAN AYAH = '))
if pekerjaan_orang_tua not in list_pekerjaan:
    print("ORANG TUA ANDA TIDAK MASUK DALAM KATEGORI")
else:
    print("ORANG TUA ANDA MASUK DALAM KATEGORI")    
gaji_orangtua = int(input('MASUKAN GAJI ORANG TUA = '))
ipk = float(input('MASUKAN IPK ANDA = '))
if gaji_orangtua < 1000000 and ipk >= 2.7 and umur < 25 and pekerjaan_orang_tua in list_pekerjaan:
    print ("ANDA DAPAT BEASISWA")
else:
    print("ANDA TIDAK DAPAT BEASISWA") 