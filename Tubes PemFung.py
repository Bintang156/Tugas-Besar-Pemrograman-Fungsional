import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/rumah/Downloads/covid19App_check-master/covid_19_indonesia_time_series_all.csv')


def menu():
    clear_screen()
    print("SELAMAT DATANG DI APLIKASI CEK COVID-19")
    print("1. KASUS COVID-19")
    print("2. URUTAN KASUS COVID-19")
    print("3. GRAFIK KASUS COVID-19")
    print("4. Exit")
    selected_menu = input("PILIH MENU : ")
    if selected_menu == "1":
        cari_data()
    elif selected_menu == "2":
        urutkan_data()
    elif selected_menu == "3":
        grafik_data()
    elif selected_menu == "4":
        print("keluar program")
        exit
    else:
        print("PILIHAN MENU SALAH!")
        kembali_ke_menu()


def kembali_ke_menu():
    print("\n")
    input("TEKAN ENTER UNTUK KEMBALI KE MENU")
    menu()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def cari_data():
    clear_screen()
    print("CEK KASUS BERDASARKAN :")
    print("1. TANGGAL (JANUARI)")
    print("2. PROVINSI")
    sub_menu = input("PILIH MENU : ")
    if sub_menu == "1":
        try:
            waktu_tanggal = int(input("MASUKAN Tanggal : "))
            if waktu_tanggal in range(1, 21):
                kolom = df.groupby("Date").TotalCases.sum().reset_index()
                dict = kolom.to_dict('Records')
                fungsi = list(filter(lambda x: x['Date'] == int(waktu_tanggal), dict))
                hasil = pd.DataFrame.from_dict(fungsi)
                print(hasil)
            else:
                print('DATA BELUM TERSEDIA')
        except ValueError:
            print("INPUTAN SALAH")
            kembali_ke_menu()
    elif sub_menu == "2":
        tempat_provinsi = input("MASUKKAN NAMA PROVINSI:")
        lokasi = df.groupby("Location").TotalCases.max().reset_index()
        dict = lokasi.to_dict('Records')
        fungsi = list(filter(lambda x: x['Location'] == tempat_provinsi.capitalize(), dict))
        hasil = pd.DataFrame.from_dict(fungsi)
        print(hasil)
    else:
        print("INPUTAN SALAH")
        kembali_ke_menu()

    kembali_ke_menu()


# ---------------------------------------------------------------------------------------------
def urutkan_data():
    clear_screen()
    print("URUTAN DATA BERDASARKAN :")
    print("1. TOTAL KEMATIAN")
    print("2. TOTAL KESEMBUHAN")
    print("3. TOTAL KASUS")
    sub_menu = input("PILIH MENU : ")
    if sub_menu == "1":
        lokasi = df.groupby("Location").TotalDeaths.max().reset_index()
        dict = lokasi.to_dict('Records')
        fungsi = list(sorted(dict, key=lambda x: x['TotalDeaths'], reverse=True))
        hasil = pd.DataFrame.from_dict(fungsi)
        print(hasil)
    elif sub_menu == "2":
        lokasi = df.groupby("Location").TotalRecovered.max().reset_index()
        dict = lokasi.to_dict('Records')
        fungsi = list(sorted(dict, key=lambda x: x['TotalRecovered'], reverse=True))
        hasil = pd.DataFrame.from_dict(fungsi)
        print(hasil)
    elif sub_menu == "3":
        lokasi = df.groupby("Location").TotalCases.max().reset_index()
        dict = lokasi.to_dict('Records')
        fungsi = list(sorted(dict, key=lambda x: x['TotalCases'], reverse=True))
        hasil = pd.DataFrame.from_dict(fungsi)
        print(hasil)
    else:
        print("INPUTAN SALAH")
        kembali_ke_menu()
    kembali_ke_menu()


# -----------------------------------------------------------------------------------------
def grafik_data():
    clear_screen()
    print("LIHAT GRAFIK :")
    print("1. TOTAL KASUS")
    print("2. PENAMBAHAN KASUS PERHARI")
    sub_menu = input("PILIHAN MENU : ")
    if sub_menu == "1":
        kolom = df.groupby("Date").TotalCases.sum().reset_index()
        dict = kolom.to_dict('Records')
        date = list(map(lambda x: x.get('Date'), dict))
        kasus = list(map(lambda x: x.get('TotalCases'), dict))
        # grafik matplotlib
        ax = plt.subplot()
        plt.xlabel("tanggal (Januari)")
        plt.ylabel("jumlah kasus")
        plt.title("Grafik Jumlah Kasus Covid-19")
        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        plt.plot(date, kasus)
        plt.show()
    elif sub_menu == "2":
        kolom = df.groupby("Date").NewCases.sum().reset_index()
        dict = kolom.to_dict('Records')
        date = list(map(lambda x: x.get('Date'), dict))
        kasus = list(map(lambda x: x.get('NewCases'), dict))
        # grafik matplotlib
        ax = plt.subplot()
        plt.xlabel("tanggal (Januari)")
        plt.ylabel("jumlah kasus")
        plt.title("Grafik Penambahan Kasus Harian Covid-19")
        ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
        plt.plot(date, kasus)
        plt.show()
    else:
        print("INPUTAN SALAH!")
        kembali_ke_menu()
    kembali_ke_menu()


if __name__ == "__main__":
    while True:
        menu()
