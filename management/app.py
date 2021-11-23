#contoh program management kontak
import function
#list dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama" : "fery",
    "email" : "feriyan368@gmail.com",
    "telepon" : " 0880000"
    

})

#menu
while True:
    print("# menu")
    print("1. Daftar kontak")
    print("2. Tambah kontak")
    print("3. Hapus kontak")
    print("4. cari kontak")
    print("0. Keluar program")

    menu = input("pilih menu :")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("menu tidak tersedia") 

print("program selesai")
