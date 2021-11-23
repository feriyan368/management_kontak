#contoh program management kontak

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("===================")
        print(f"Nama : {kontak['nama']}")
        print(f"Nama : {kontak['email']}")
        print(f"Nama : {kontak['telepon']}")
#tambah kontak
def new_kontak():
    nama = input("nama :")
    email = input("email :")
    telepon = input("telepon :")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak
#hapus kontak
def hapus_kontak(daftar_kontak):
    telepon = input("no yang akan di hapus :")

    index =-1

    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index= i
            break

    if index == -1:
        print("data tidak ditemukan")        
    else:
        del daftar_kontak[index]
        print("data berhasil dihapus")
    

#cari kontak
def cari_kontak(daftar_kontak):
    nama_yg_dicari = input("nama yang dicari :")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print("==============")
            print(f"Nama : {kontak['nama']}")
            print(f"Nama : {kontak['email']}")
            print(f"Nama : {kontak['telepon']}")