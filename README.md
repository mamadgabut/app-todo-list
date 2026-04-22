📝 Task Management System (Python CLI)
Sistem Manajemen Tugas sederhana berbasis baris perintah (CLI) yang dibuat menggunakan bahasa pemrograman Python. Proyek ini dirancang untuk membantu pengguna mengelola daftar tugas harian mereka dengan fitur dasar CRUD (Create, Read, Update, Delete).

🚀 Fitur Utama

Tambah Tugas (tambah_tugas): Memasukkan judul, deskripsi, status, dan estimasi waktu pengerjaan.
Lihat Tugas (lihat_tugas): Menampilkan daftar seluruh tugas yang tersimpan dengan format yang rapi.
Tandai Selesai (tandai_selesai): Mengubah status tugas tertentu menjadi "Selesai" berdasarkan ID.
Hapus Tugas (hapus_tugas): Menghapus tugas dari daftar secara permanen berdasarkan ID.

🛠️ Struktur Data

Sistem ini menggunakan List untuk menampung kumpulan data, di mana setiap tugas disimpan di dalam sebuah Dictionary.
Contoh format data:

{

    "id": 1,
    
    "title": "Belajar Python",
    
    "description": "Mempelajari fungsi dan list",
    
    "status": "belum selesai",
    
    "estimasi_waktu_pengerjaan": 60
}

📖 Penjelasan Fungsi
1. Tambah Tugas
Fungsi ini melakukan validasi input untuk memastikan:
Judul dan deskripsi tidak boleh kosong.
Status harus berupa "Selesai" atau "Belum Selesai".
Estimasi waktu harus berupa angka dan lebih dari 0.
ID dibuat secara otomatis (Auto-increment).

3. Lihat Tugas
Menampilkan informasi tugas kepada pengguna. Jika daftar kosong, sistem akan memberikan notifikasi bahwa tidak ada tugas tersedia.

5. Tandai Selesai
Fungsi ini mencari tugas berdasarkan ID yang dimasukkan. Menggunakan blok try...except untuk mencegah program crash jika pengguna memasukkan input selain angka.

7. Hapus Tugas
  Menampilkan daftar tugas terlebih dahulu agar pengguna bisa melihat ID, kemudian menghapus tugas yang dipilih menggunakan metode .remove().

💻 Cara Menjalankan
1. Pastikan Anda memiliki Python terinstal (Versi 3.6 ke atas).
2. Siapkan sebuah variabel list kosong di awal program:

tugas_saya = []

3. Panggil fungsi yang diinginkan, misalnya:

🎓 Konsep Python yang Dipelajari

Proyek ini mencakup beberapa materi fundamental Python:

- List & Dictionary: Penyimpanan data terstruktur.
- Looping (while, for): Pengulangan untuk validasi dan pencarian data.
- Control Flow (if-else, break, return): Logika pengambilan keputusan.
- Error Handling (try-except): Menangani kesalahan input pengguna agar program stabil.
- String Formatting (f-strings): Menampilkan output yang lebih cantik dan dinamis.
