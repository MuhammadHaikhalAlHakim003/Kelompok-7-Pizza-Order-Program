# Layanan Pemesanan Pizza Dengan Memilih Topping Crust dan Ukuran Pizza
def pesan_pizza():
    print("Selamat datang di layanan pemesanan Pizza!")
    
    # Pilih Topping Secara Pilih Topping
    while True:
        print("\nPilih Topping:")
        print("1. Frankfurter BBQ (Rp. 20.000)")
        print("2. Meat Monsta (Rp. 25.000)")
        print("3. Super supreme chicken (Rp. 30.000)")
        topping_choice = input("Masukkan pilihan topping (1/2/3): ")
        
        if topping_choice == "1":
            topping = "Frankfurter BBQ"
            harga_topping = 20000
            break
        elif topping_choice == "2":
            topping = "Meat Monsta"
            harga_topping = 25000
            break
        elif topping_choice == "3":
            topping = "Super supreme chicken"
            harga_topping = 30000
            break
        else:
            print("Pilihan topping tidak valid. Silakan coba lagi.")
    
    # Pilih Crust Secara Masukkin Angka
    while True:
        print("\nPilih jenis Crust Pizza:")
        print("1. Thin Crust (Rp. 10.000)")
        print("2. Thick Crust (Rp. 12.000)")
        print("3. Stuffed Crust (Rp. 15.000)")
        crust_choice = input("Masukkan pilihan crust (1/2/3): ")
        
        if crust_choice == "1":
            crust = "Thin Crust"
            harga_crust = 10000
            break
        elif crust_choice == "2":
            crust = "Thick Crust"
            harga_crust = 12000
            break
        elif crust_choice == "3":
            crust = "Stuffed Crust"
            harga_crust = 15000
            break
        else:
            print("Pilihan crust tidak valid. Silakan coba lagi.")
    
    # Pilih Ukuran Secara Masukkin Angka
    while True:
        print("\nPilih ukuran Pizza:")
        print("1. Kecil (Rp. 20.000)")
        print("2. Sedang (Rp. 30.000)")
        print("3. Besar (Rp. 50.000)")
        ukuran_choice = input("Masukkan pilihan ukuran (1/2/3): ")
        
        if ukuran_choice == "1":
            ukuran = "Kecil"
            harga_ukuran = 20000
            break
        elif ukuran_choice == "2":
            ukuran = "Sedang"
            harga_ukuran = 30000
            break
        elif ukuran_choice == "3":
            ukuran = "Besar"
            harga_ukuran = 50000
            break
        else:
            print("Pilihan ukuran tidak valid. Silakan coba lagi.")
    
    # Tambah Keju Secara Pilih Y/N
    cheese_choice = input("Apakah Anda ingin menambahkan keju ekstra seharga Rp. 13.000? (Y/N): ")
    
    if cheese_choice.lower() == 'y':
        tambah_keju = True
        harga_keju = 13000
    else:
        tambah_keju = False
        harga_keju = 0
    
    # Rumus Hitungan Dari Semua Pilihan
    total_harga = harga_topping + harga_crust + harga_ukuran + harga_keju
    
    # Detail Pesanan dan Tampilan Total Harga
    print("\nDetail Pesanan Anda:")
    print(f"Topping: {topping} (Rp. {harga_topping})")
    print(f"Crust: {crust} (Rp. {harga_crust})")
    print(f"Ukuran: {ukuran} (Rp. {harga_ukuran})")
    if tambah_keju:
        print(f"Tambahan: Keju ekstra (Rp. {harga_keju})")
    print(f"Total Harga: Rp. {total_harga}")
    
    print("\nTerima kasih telah memesan pizza!")

# Memanggil fungsi (def) Untuk Memulai Program
pesan_pizza()
