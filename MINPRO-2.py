import os
from prettytable import PrettyTable

os.system("cls")

# Stock Barang
tampungan_barang = []
user_role = None  # (iyas)tambah user_role

def clear_console():
    os.system("cls")

credentials = {
    "admin": "admin123",
    "karyawan": "karyawan123"
}

def login():
    global user_role #global
    clear_console()
    print("LOGIN".center(40, "="))
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    
    if username in credentials and credentials[username] == password:
        print("Anda Berhasil Login!")
        user_role = username  # Store the role globally
        if username == "admin":
            admin_menu()
        else:
            karyawan_menu()
    else:
        print("Username atau Password Anda salah!")
        retry = input("Apakah Anda ingin mencoba lagi (y/t): ")
        if retry.lower() == 'y':
            login()
        elif retry.lower() == 't':
            logout()
        else:
            print("Terima Kasih!")
            logout()

def admin_menu():
    while True:
        print('-'*40)
        print(" PROGRAM BARANG".center(40, "="))
        print('-'*40)

        print('''
    1. Tambah Barang
    2. Hapus Barang
    3. Cek Barang
    4. Edit
    5. Cek Ketersediaan Barang
    6. Logout
        ''')
        print('-'*40)
        pilihan = input('Masukkan Pilihan Menu: ')
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            cek_barang()
        elif pilihan == '4':
            edit()
        elif pilihan == '5':
            cek_ketersediaan_barang()
        elif pilihan == '6':
            print("Logout Berhasil!")
            logout()
        else:
            print("Pilihan Anda tidak valid")

def karyawan_menu():
    while True:
        print('-'*40)
        print("PROGRAM KARYAWAN".center(40, "="))
        print('-'*40)

        print('''
1. Cek Barang
2. Cek Ketersediaan Barang
3. Logout
        ''')
        print('-'*40)
        pilihan = input("Masukkan Pilihan Menu: ")
        if pilihan == '1':
            cek_barang()
        elif pilihan == '2':
            cek_ketersediaan_barang()
        elif pilihan == '3':
            print("Anda Berhasil Logout")
            logout()
        else:
            print("Pilihan tidak valid!")


# TAMBAH BARANG
def tambah_barang():
    print('-'*40)
    print(" TAMBAH BARANG".center(40, "="))
    print('-'*40)
    while True:
        tambah_barang = input('Masukkan Nama Barang: ')
        tampungan_barang.append(tambah_barang)
        print("\nLIST BARANG")
        for i in tampungan_barang:
            print("Barang: ", i)
        lanjut = input('Apakah Anda Ingin Lanjut? (y/t): ')
        if lanjut.lower() == 'y':
            pass
        else:
            admin_menu()

def hapus_barang():
    print('-'*40)
    print(" HAPUS BARANG".center(40, "="))
    print('-'*40)
    while True:
        hapus_barang = input('Masukkan Nama Barang yang Akan Dihapus: ')
        if hapus_barang in tampungan_barang:
            tampungan_barang.remove(hapus_barang)
            print("\nBARANG TERSISA")
            for i in tampungan_barang:
                print("Barang: ", i)
            lanjut = input('Apakah Anda Ingin Lanjut? (y/t): ')
            if lanjut.lower() == 'y':
                pass
            else:
                admin_menu()
        else:
            print('Barang tidak tersedia!')
            lanjut = input('Apakah Anda Ingin Lanjut? (y/t): ')
            if lanjut.lower() != 'y':
                admin_menu()

def cek_barang():
    print("\nBARANG TERSISA: ")
    tabel = PrettyTable()
    tabel.field_names = ["KODE BARANG", "NAMA BARANG"]
    for i, barang in enumerate(tampungan_barang, start=1):
        tabel.add_row([i, barang])
    print(tabel)
    
    input('Tekan Enter untuk kembali ke menu :')
    if user_role == "admin":
        admin_menu()
    else:
        karyawan_menu()

def edit():
    print('-'*40)
    print(" EDIT BARANG".center(40, "="))
    print('-'*40)
    while True:
        print("\nKODE BARANG".center(15), "NAMA BARANG".center(20))
        for i, barang in enumerate(tampungan_barang, start=1):
            print(f"+  {i}  | {barang.center(15)}  +")
        print('-'*40)
        
        edit = input('Masukkan nama barang yang ingin di edit: ')
        if edit in tampungan_barang:
            ubah = input('Ubah nama barang ke: ')
            tampungan_barang[tampungan_barang.index(edit)] = ubah
            lanjut = input('Apakah Anda Ingin Lanjut? (y/t): ')
            if lanjut.lower() != 'y':
                admin_menu()
        else:
            print('BARANG TIDAK TERSEDIA!')

def cek_ketersediaan_barang():
    print('-'*40)
    print(" CEK KETERSEDIAAN BARANG".center(40, "="))
    print('-'*40)
    cek_barang = input('Masukkan nama barang: ')
    if cek_barang in tampungan_barang:
        print(f"{cek_barang} Tersedia!")
    else:
        print(f"{cek_barang} Tidak Tersedia!")
    lanjut = input('Lanjut mengecek barang (y/t): ')
    if lanjut.lower() != 'y':
        if user_role == "admin":
            admin_menu()
        else:
            karyawan_menu()

def logout():
    exit()

login()
