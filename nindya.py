def cari_tiket():
    print("----------------------------------------------------")
    print("|               🔎 CARI TIKET PERJALANAN           |")
    print("----------------------------------------------------")
    kota_asal = input("🏙️ Kota Asal          : ")
    kota_tujuan = input("🏙️ Kota Tujuan        : ")
    tanggal = input("📅 Tanggal Keberangkatan (dd-mm-yyyy) : ")
    
    print("\n----------------------------------------------------")
    print("|               🎫 PILIH KELAS PERJALANAN          |")
    print("----------------------------------------------------")
    print("   [1] Ekonomi")
    print("   [2] Bisnis")
    print("   [3] Eksekutif")
    
    while True:
        try:
            pilihan_kelas = int(input("\n> Pilih kelas dengan mengetik nomor: "))
            if pilihan_kelas not in [1, 2, 3]:
                raise ValueError("Nomor yang dimasukkan harus 1, 2, atau 3.")
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}")
    
    kelas = {1: "Ekonomi", 2: "Bisnis", 3: "Eksekutif"}[pilihan_kelas]
    
    print("\n----------------------------------------------------")
    print("[ Cari Tiket ]                              [ Batal ]")
    print("----------------------------------------------------")
    
    while True:
        konfirmasi = input("\n> Ketik 'Cari' untuk melanjutkan atau 'Batal' untuk membatalkan: ").strip().lower()
        if konfirmasi == "cari":
            print("\nPencarian tiket sedang diproses...")
            print(f"Kota Asal         : {kota_asal}")
            print(f"Kota Tujuan       : {kota_tujuan}")
            print(f"Tanggal Keberangkatan : {tanggal}")
            print(f"Kelas Perjalanan  : {kelas}")
            break
        elif konfirmasi == "batal":
            print("\nPencarian tiket dibatalkan.")
            break
        else:
            print("Input tidak valid. Harap ketik 'Cari' atau 'Batal'.")

# Jalankan program
cari_tiket()
