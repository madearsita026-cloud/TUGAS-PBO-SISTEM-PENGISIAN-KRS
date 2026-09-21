class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def __str__(self):
        return f"[{self.kode}] {self.nama} ({self.sks} SKS)"


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        # Enkapsulasi: private attribute untuk menyimpan list mata kuliah (KRS)
        self.__krs = []

    # Private Method: Hanya bisa dipanggil dari dalam class Mahasiswa
    def __hitung_total_sks(self):
        total_sks = 0
        for mk in self.__krs:
            total_sks += mk.sks
        return total_sks

    # Public Method: Menambahkan mata kuliah ke KRS dengan validasi isinstance
    def tambah_matakuliah(self, mata_kuliah):
        # Memvalidasi input objek sebelum dimasukkan ke dalam list
        if isinstance(mata_kuliah, MataKuliah):
            self.__krs.append(mata_kuliah)
            print(f"Berhasil menambahkan {mata_kuliah.nama} ke KRS {self.nama}.")
        else:
            print("Gagal: Objek yang dimasukkan harus merupakan instance dari class 'MataKuliah'.")

    # Public Method: Menampilkan KRS dan memanggil private method __hitung_total_sks
    def tampilkan_krs(self):
        print(f"\n================ KRS MAHASISWA ================")
        print(f"NIM  : {self.nim}")
        print(f"Nama : {self.nama}")
        print("-" * 47)
        
        if not self.__krs:
            print("Belum ada mata kuliah yang diambil.")
        else:
            for idx, mk in enumerate(self.__krs, 1):
                print(f"{idx}. {mk}")
            
            # Memanggil private method untuk mendapatkan total SKS
            total = self.__hitung_total_sks()
            print("-" * 47)
            print(f"Total SKS Diambil: {total} SKS")
        print("===============================================\n")


# ==========================================
# CONTOH PENGGUNAAN PROGRAM
# ==========================================

if __name__ == "__main__":
    # 1. Membuat beberapa objek MataKuliah
    mk1 = MataKuliah("CSP101", "Pemrograman Berbasis Objek", 3)
    mk2 = MataKuliah("CSP102", "Struktur Data", 4)
    mk3 = MataKuliah("CSP103", "Basis Data", 3)

    # 2. Membuat objek Mahasiswa
    mhs = Mahasiswa("250211060009", "Made Kirana")

    # 3. Menambahkan MataKuliah valid ke KRS
    mhs.tambah_matakuliah(mk1)
    mhs.tambah_matakuliah(mk2)
    mhs.tambah_matakuliah(mk3)

    # 4. Uji coba menambahkan data yang SALAH (bukan instance MataKuliah)
    mhs.tambah_matakuliah("Ini hanya teks biasa")  # Akan ditolak oleh isinstance()

    # 5. Menampilkan KRS beserta total SKS
    mhs.tampilkan_krs()