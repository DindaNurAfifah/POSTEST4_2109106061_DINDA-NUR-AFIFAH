#program dengan CRUD
def Tampilkan_menu() :
    print("[1] Menu produk")
    print("[2] login Menu admin")
    print("[3] login Menu pelanggan")
    print("[4] buat produk baru")
    print("[5] cari dan lihat stok produk")
    print("[6] tambah stok produk")
    print("[7] hapus produk")
    print("[8] mesin kasir")
    print("[9] keluar program")

while True:
    Tampilkan_menu()
    menu = int(input("pilih menu="))


    if menu == 1 :
        produk    = ["1. Bunga Mawar Merah/Putih= 10000",
                     "2. Bunga Mawar Pelangi    = 20000",
                     "3. Bunga Matahari         = 16000",
                     "4. Bunga Kapas            = 18000"
                    ]
        print("Inilah menu kami")
        for menu in produk :
            print(menu)

    elif menu == 2 :
        admin = str(input("Username: "))
        if admin == 'happyroof' :
            print("Username ditemukan")
        sandi = str(input("Password: "))
        if sandi == '061' :
            print("Berhasil Login")
    
        else :
            print("Username atau Passsword Anda Salah")
        
    elif menu == 3 :
        pelanggan = str(input("Username: "))
        if pelanggan == 'happyuser' :
            print("Username ditemukan")
        sandi = int(input("Password: "))
        if sandi == 210 :
            print("berhasil login")
            print("anda berhak mendapat diskon 30%")
            print("Saat memakai diskon ini, potongan harga lainnya tak berlaku")

        else :
            print("Username atau Passsword Anda Salah")

    elif menu == 4 :
        produk    = ["1. Bunga Mawar Merah  = 10000",
                     "2. Bunga Mawar Pelangi= 20000",
                     "3. Bunga Matahari     = 16000",
                     "4. Bunga Kapas        = 18000"
                    ]
        produk_baru = str(input("masukan produk dan harga= "))
        produk.append(produk_baru)
        for menu in produk :
            print(menu)

    elif menu == 5 :
        produk_baru=["1. Bunga Mawar Merah  = 10000",
                     "2. Bunga Mawar Pelangi= 20000",
                     "3. Bunga Matahari     = 16000",
                     "4. Bunga Kapas        = 18000",
                     "5. Bunga Tulip        = 10000"
                    ]
        stok_produk=["1. Bunga Mawar Merah  = 175",
                     "2. Bunga Mawar Pelangi= 100",
                     "3. Bunga Matahari     = 42",
                     "4. Bunga Kapas        = 30",
                     "5. Bunga Tulip        = 120"
                    ]
        for menu in produk_baru :
            print(menu)
        cari = int(input("Bunga apa yang anda cari? "))
        if cari == 1 :
            print(stok_produk[0])
        elif cari == 2 :
            print(stok_produk[1])
        elif cari == 3 :
            print(stok_produk[2])
        elif cari == 4 :
            print(stok_produk[3])
        elif cari == 5 :
            print(stok_produk[4])

        else :
            print("produk tidak tersedia")

    elif menu == 6 :
        stok_produk=["1. Bunga Mawar Merah = 175",
                    "2. Bunga Mawar Pelangi= 100",
                    "3. Bunga Matahari     = 42",
                    "4. Bunga Kapas        = 30",
                    "5. Bunga Tulip        = 120"
                    ]
        tambah = int(input("stok bunga apa yang akan ditambah? "))
        if tambah == 1 :
            stok= int(input("berapa banyak= "))
            hitung = 175 + stok
            print("Dari 175 Bunga Mawar Merah menjadi ",hitung)
        elif tambah == 2 :
            stok= int(input("berapa banyak= "))
            hitung = 100 + stok
            print("Dari 100 Bunga Mawar Pelangi menjadi ",hitung)
        elif tambah == 3 :
            stok= int(input("berapa banyak= "))
            hitung = 42 + stok
            print("Dari 42 Bunga Matahari menjadi ",hitung)
        elif tambah == 4 :
            stok= int(input("berapa banyak= "))
            hitung = 30 + stok
            print("Dari 30 Bunga Kapas menjadi ",hitung)
        elif tambah == 5 :
            stok= int(input("berapa banyak= "))
            hitung = 120 + stok
            print("Dari 120 Bunga Tulip menjadi ",hitung)

        else :
            print("stok tidak tersedia")
        
    elif menu == 7 :
        produk=["1. Bunga Mawar Merah  = 10000",
                "2. Bunga Mawar Pelangi= 20000",
                "3. Bunga Matahari     = 16000",
                "4. Bunga Kapas        = 18000",
                "5. Bunga Tulip        = 10000"
               ]
        for menu in produk :
            print(menu)
        hapus = int(input("produk apa yang akan di hapus? "))
        if hapus == 1 :
            produk.remove("1. Bunga Mawar Merah  = 10000")
            for menu in produk :
                print(menu)
        elif hapus == 2 :
            produk.remove("2. Bunga Mawar Pelangi= 20000")
            for menu in produk :
                print(menu)
        elif hapus == 3 :
            produk.remove("3. Bunga Matahari     = 16000")
            for menu in produk :
                print(menu)
        elif hapus == 4 :
            produk.remove("4. Bunga Kapas        = 18000")
            for menu in produk :
                print(menu)
        elif hapus == 5 :
            produk.remove("5. Bunga Tulip        = 10000")
        
        else :
            print("Produk Tidak Tersedia")

    elif menu == 8 :
        produk=["1. Bunga Mawar Merah  = 10000",
                "2. Bunga Mawar Pelangi= 20000",
                "3. Bunga Matahari     = 16000",
                "4. Bunga Kapas        = 18000",
                "5. Bunga Tulip        = 10000"
               ]
        list_diskon = ["Pembelian Bunga Mawar Merah/putih >= 10 tangkai bunga diskon 10%",
                       "Pembelian Bunga Mawar Pelang >= 10 tangkai bunga diskon 20%",
                       "Pembelian Bunga Matahari >= 5 tangkai bunga diskon 20%",
                       "Pembelian Bunga Kapas >= 10 tangkai bunga diskon 25%",
                       "Pembelian Bunga Tulip >= 10 tangkai diskon 10%"]
        for menu in produk :
            print(menu)

        beli = int(input("Masukan pilihan: "))
        if beli == 1 :
            jumlah = int(input("Masukan jumlah tangkai="))

            if jumlah <10 :
                bayar = jumlah * 10000
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            elif jumlah >= 10:
                pilih  = int(input("pilih diskon: "))
                diskon = ["1. diskon >= 10 dapat potongan 10%",
                          "2. diskon login pelanggan diskon 30%"]

            if pilih == 1 :
                hitung   = jumlah * 10000
                potongan = jumlah * 10000 * 0.1
                bayar    = hitung - potongan
                print("Anda mendapat potongan 10%")
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            elif pilih == 2 :
                hitung   = jumlah * 10000
                potongan = jumlah * 10000 * 0.3
                bayar    = hitung - potongan
                print("Anda mendapat potongan 30%")
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            else :
                print("Pilihan Diskon Tak Tersedia")
                break

        elif beli == 2 :
            jumlah = int(input("Masukan jumlah tangkai="))
            if jumlah <10 :
                bayar = jumlah * 20000
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            elif jumlah >= 10:
                pilih  = int(input("pilih diskon: "))
                diskon = ["1. diskon >= 10 dapat potongan 20%",
                          "2. diskon login pelanggan diskon 30%"
                         ]
            if pilih == 1 :
                hitung   = jumlah * 20000
                potongan = jumlah * 20000 * 0.2
                bayar    = hitung - potongan
                print("Anda mendapat potongan 10%")
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            elif pilih == 2 :
                hitung   = jumlah * 20000
                potongan = jumlah * 20000 * 0.3
                bayar    = hitung - potongan
                print("Anda mendapat potongan 30%")
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break
            
            else :
                print("Pilihan Diskon Tak Tersedia")
                break

        elif beli == 3 :
            jumlah = int(input("Masukan jumlah tangkai="))
            if jumlah <5 :
                bayar = jumlah * 16000
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            elif jumlah >= 5 :
                pilih  = int(input("pilih diskon: "))
                diskon = ["1. diskon >= 10 dapat potongan 20%",
                          "2. diskon login pelanggan diskon 30%"
                         ]
            if pilih == 1 :
                hitung   = jumlah * 16000
                potongan = jumlah * 16000 * 0.2
                bayar    = hitung - potongan
                print("Anda mendapat potongan 20%")
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break 

            elif pilih == 2 :
                hitung   = jumlah * 16000
                potongan = jumlah * 16000 * 0.3
                bayar    = hitung - potongan
                print("Anda mendapat potongan 30%")
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            else :
                print("Pilihan Diskon Tak Tersedia")
                break

        elif beli == 4 :
            jumlah = int(input("Masukan jumlah tangkai= "))
            if jumlah <10 :
                bayar = jumlah * 18000
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            elif jumlah >= 10:
                pilih  = int(input("pilih diskon: "))
                diskon = ["1. diskon >= 10 dapat potongan 25%",
                          "2. diskon login pelanggan diskon 30%"
                         ]
            if pilih == 1 :
                hitung   = jumlah * 18000
                potongan = jumlah * 18000 * 2.5
                bayar    = hitung - potongan
                print("Anda mendapat potongan 25%")
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            elif pilih == 2 :
                hitung   = jumlah * 18000
                potongan = jumlah * 18000 * 0.3
                bayar    = hitung - potongan
                print("Anda mendapat potongan 30%")
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            else :
                print("Pilihan Diskon Tak Tersedia")
                break

        elif beli == 5 :
            jumlah = int(input("Masukan jumlah tangkai="))
            if jumlah <10 :
                bayar = jumlah * 10000
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            elif jumlah >= 10:
                pilih  = int(input("pilih diskon: "))
                diskon = ["1. diskon >= 10 dapat potongan 10%",
                          "2. diskon login pelanggan diskon 30%"
                         ]
            if pilih == 1 :
                hitung   = jumlah * 10000
                potongan = jumlah * 10000 * 0.1
                bayar    = hitung - potongan
                print("Anda mendapat potongan 10%")
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            elif pilih == 2 :
                hitung   = jumlah * 10000
                potongan = jumlah * 10000 * 0.3
                bayar    = hitung - potongan
                print("Anda mendapat potongan 30%")
                print("Silahkan Lakukan Pembayaran Sebesar", "Rp.", bayar)
                print("Ditunggu pembelian berikutnya")
                break

            else :
                print("Pilihan Diskon Tak Tersedia")
                break

    elif menu == 9 :
        print("Tutup Program")
        break

    else :
        print("Pilihan menu tidak tersedia")