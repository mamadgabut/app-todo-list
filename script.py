def lihat_tugas(tugas):
    # Mengecek apakah list 'tugas' kosong. 
    # Di Python, list kosong ([]) dianggap bernilai False secara logika.
    # 'if not tugas' secara bahasa berarti "jika list tugas tidak ada isinya".
    if not tugas:
        print("Tidak ada tugas yang tersedia.")
        return  # Kata kunci 'return' di sini digunakan untuk langsung keluar dari fungsi
                # agar perintah-perintah di bawahnya tidak dijalankan.
 
    # Jika list ada isinya, maka program akan lanjut ke baris ini
    print("Daftar Tugas:")

    # 'for' digunakan untuk mengulang (looping) setiap elemen di dalam list 'tugas'.
    # Setiap elemen (yang berbentuk dictionary) akan disimpan sementara di variabel 'tugas_item'.
    for tugas_item in tugas:
        # Menggunakan f-string (huruf 'f' di depan tanda kutip) untuk mencetak teks yang
        # digabungkan dengan isi variabel di dalam kurung kurawal {}.
        
        # Mengambil data dari dictionary berdasarkan nama kunci (key) seperti 'id' dan 'title'
        print(f"- {tugas_item['id']}. {tugas_item['title']}")
        
        # Memberikan spasi di awal string agar tampilan deskripsi terlihat menjorok ke dalam
        print(f"  Deskripsi: {tugas_item['description']}")
        
        print(f"  Status: {tugas_item['status']}")
        
        print(f"  Estimasi Waktu: {tugas_item['estimasi_waktu_pengerjaan']} menit")
        
        # Melakukan operasi perkalian pada string. 
        # "-" * 20 akan mencetak tanda hubung sebanyak 20 kali untuk pemisah visual.
        print("-" * 20)
 
def tambah_tugas(tugas):
    # 'tugas' adalah parameter berupa LIST yang akan menampung kumpulan dictionary data tugas
    
    # --- BAGIAN INPUT JUDUL ---
    while True:  # Menggunakan perulangan agar jika salah, user diminta input ulang
        title = input("Masukkan judul tugas: ")
        if title:  # Mengecek apakah input tidak kosong (Python menganggap string kosong sebagai False)
            break  # Keluar dari loop jika input sudah benar
        print("Judul tugas tidak boleh kosong. Silakan coba lagi.")
 
    # --- BAGIAN INPUT DESKRIPSI ---
    while True:
        description = input("Masukkan deskripsi tugas: ")
        if description:  # Memastikan deskripsi diisi
            break
        print("Deskripsi tugas tidak boleh kosong. Silakan coba lagi.")
 
    # --- BAGIAN INPUT STATUS ---
    while True:
        # .lower() mengubah input user (misal: 'SELESAI') menjadi huruf kecil ('selesai') 
        # agar lebih mudah dibandingkan
        status = input("Masukkan status tugas (Selesai/Belum Selesai): ").lower()
        
        # Mengecek apakah input user ada di dalam daftar pilihan yang valid
        if status in ["selesai", "belum selesai"]:
            break
        print("Status tugas harus 'Selesai' atau 'Belum Selesai'. Silakan coba lagi.")
 
    # --- BAGIAN INPUT ESTIMASI WAKTU (Angka) ---
    while True:
        try:
            # input() selalu menghasilkan teks (string), maka harus diubah ke angka (int)
            estimasi_waktu = int(input("Masukkan estimasi waktu pengerjaan (menit): "))
            
            if estimasi_waktu > 0:  # Memastikan angka yang dimasukkan positif
                break
            print("Estimasi waktu harus lebih dari 0. Silakan coba lagi.")
            
        except ValueError:
            # Jika user memasukkan huruf (bukan angka), fungsi int() akan error.
            # Bagian ini menangkap error tersebut agar program tidak berhenti (crash).
            print("Estimasi waktu harus berupa angka. Silakan coba lagi.")
 
    # --- BAGIAN PENYIMPANAN DATA ---
    # Membuat sebuah Dictionary untuk membungkus satu data tugas yang baru
    new_task = {
        # ID dibuat otomatis berdasarkan jumlah data yang ada di list + 1
        "id": len(tugas) + 1,  
        "title": title,
        "description": description,
        "status": status,
        "estimasi_waktu_pengerjaan": estimasi_waktu
    }
    
    # Memasukkan dictionary 'new_task' ke dalam list utama bernama 'tugas'
    tugas.append(new_task)
    
    # Memberi notifikasi bahwa proses berhasil
    print("Tugas berhasil ditambahkan!")
 
def tandai_selesai(tugas):
    # --- BAGIAN INPUT & VALIDASI ---
    # Kita menggunakan blok try-except untuk menangani kesalahan input
    try:
        # input() mengambil teks, int() mengubahnya menjadi angka bulat.
        # Jika user memasukkan huruf, proses int() akan memicu "ValueError".
        id_tugas = int(input("Masukkan ID tugas yang ingin ditandai selesai: "))
    except ValueError:
        # Bagian ini berjalan hanya jika user memasukkan sesuatu yang bukan angka.
        print("ID tugas harus berupa angka.")
        return  # Menghentikan fungsi di sini agar tidak lanjut ke proses pencarian.
 
    # --- BAGIAN PENCARIAN DATA ---
    # 'for' digunakan untuk memeriksa setiap item (tugas_item) di dalam list 'tugas'.
    for tugas_item in tugas:
        # Kita membandingkan ID yang ada di dalam dictionary dengan ID dari input user.
        if tugas_item["id"] == id_tugas:
            
            # --- BAGIAN PEMBARUAN DATA ---
            # Jika ID cocok, kita ubah nilai pada key "status" menjadi "Selesai".
            # Karena dictionary bersifat 'mutable' (bisa diubah), data asli di list akan ikut terupdate.
            tugas_item["status"] = "Selesai"
            
            print("Tugas berhasil diperbarui menjadi selesai!")
            
            # Kita gunakan 'return' untuk langsung keluar dari fungsi.
            # Mengapa? Karena ID bersifat unik, jadi tidak perlu lagi mencari di sisa list.
            return
    
    # --- BAGIAN JIKA TIDAK DITEMUKAN ---
    # Baris ini HANYA akan dijalankan jika perulangan 'for' selesai (sampai item terakhir)
    # namun tidak ada satupun ID yang cocok (tidak pernah memicu 'return' di atas).
    print("ID tugas tidak ditemukan.")
 
def hapus_tugas(tugas):
    # Memanggil fungsi lain yang sudah dibuat sebelumnya.
    # Ini membantu user melihat ID tugas sebelum memilih mana yang akan dihapus.
    lihat_tugas(tugas)
    
    # Validasi input untuk memastikan user memasukkan angka
    try:
        id_tugas = int(input("Masukkan ID tugas yang ingin dihapus: "))
    except ValueError:
        print("ID tugas harus berupa angka.")
        return # Berhenti jika input salah
 
    # Mencari tugas yang cocok dengan ID yang diinputkan
    for tugas_item in tugas:
        if tugas_item["id"] == id_tugas:
            # .remove() adalah fungsi bawaan list untuk menghapus item tertentu.
            # Kita mengirim 'tugas_item' (seluruh isi dictionary tugas tersebut) untuk dihapus.
            tugas.remove(tugas_item)
            
            print("Tugas berhasil dihapus!")
            
            # Sangat penting: Langsung keluar dari fungsi setelah menghapus.
            # Selain efisiensi, ini menghindari error saat list berubah ukuran di tengah loop.
            return
            
    # Jika seluruh list sudah diperiksa dan ID tidak ada yang cocok
    print("ID tugas tidak ditemukan.")
 
# List untuk menyimpan tugas
tugas = [
    {
        "id": 1,
        "title": "Mengerjakan PR Matematika",
        "description": "Halaman 20-25",
        "status": "Belum Selesai",
        "estimasi_waktu_pengerjaan": 30
    },
    {
        "id": 2,
        "title": "Membeli bahan makanan",
        "description": "Daftar belanja ada di catatan",
        "status": "Selesai",
        "estimasi_waktu_pengerjaan": 60
    },
    {
        "id": 3,
        "title": "Mencuci mobil",
        "description": "Gunakan sabun khusus",
        "status": "Selesai",
        "estimasi_waktu_pengerjaan": 60
    },
    {
        "id": 4,
        "title": "Membaca buku",
        "description": "Bab 3 dan 4",
        "status": "Belum Selesai",
        "estimasi_waktu_pengerjaan": 45
    },
    {
        "id": 5,
        "title": "Menulis esai",
        "description": "Tema bebas, minimal 3 halaman",
        "status": "Selesai",
        "estimasi_waktu_pengerjaan": 60
    },
    {
        "id": 6,
        "title": "Pergi ke gym",
        "description": "Lakukan latihan kardio",
        "status": "Belum Selesai",
        "estimasi_waktu_pengerjaan": 45
    }
]
 
def menu():
    print("Selamat Datang di Aplikasi To-Do List")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")
 
def main():
 
    while True:
        menu()
        choice = input("Masukkan pilihan Anda: ")
 
        if choice == '1':
            # Logika untuk menampilkan tugas
            lihat_tugas(tugas)
        elif choice == '2':
            # Logika untuk menambahkan tugas
            tambah_tugas(tugas)
        elif choice == '3':
            # Logika untuk menandai tugas selesai
            tandai_selesai(tugas)
        elif choice == '4':
            # Logika untuk menghapus tugas
            hapus_tugas(tugas)
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
 
if __name__ == "__main__":
    main()
