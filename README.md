PyColoryMetric - Program Analisis Warna.

1. Gambaran Umum
PyColoryMetric adalah Program berbasis Python yang dirancang untuk menganalisis dan membandingkan antara dua gambar cetakan (target dan hasil). Program ini memberikan pengukuran kuantitatif perbedaan warna, Density warna, dan soliditas warna untuk mengevaluasi kualitas hasil output produksi.

2. Fitur Utama
a. Konversi warna, Mengubah gambar RGB ke ruang warna CMYK untuk analisis percetakan
b. Pengukuran Warna, Menghitung Delta E (CIE76) antara gambar target dan hasil
c. Analisis Density, Mengukur Soliditas tinta untuk setiap channel CMYK
d. Analisis Soliditas, Mengevaluasi Soliditas warna di setiap channel CMYK pada gambar
f. Perbandingan Visual,  Menampilkan perbandingan gambar dan saluran CMYK secara berdampingan
g. Visualisasi Statistik,  Menghasilkan grafik batang dan garis untuk membandingkan perbedaan

3. Cara Kerja
a. Upload Gambar, Alat akan meminta pengguna untuk mengunggah dua gambar:
b. Gambar target, (referensi/hasil yang diharapkan, Color Range)
c. Gambar hasil, (cetakan Saat ini atau produksi saat ini)
d. Konversi Ruang Warna, Kedua gambar dikonversi dari RGB ke CMYK

4. Metrik Analisis:
a. Perbedaan warna Delta E (standar CIE76)
b. Density channel CMYK (persentase rata-rata)
c. Soliditas warna (standar deviasi dalam persentase)

5. Output Visual:
a. Perbandingan gambar dengan pembagian channel CMYK
b. Grafik garis perbandingan kepadatan CMYK
c. Diagram batang perbedaan statistik

6. Penggunaan
a. Jalankan skrip di Google Colab
b. Upload Gambar target produksi
c. Upload Gambar hasil produksi saat ini.
d. Program akan secara otomatis memproses gambar dan menampilkan
   - Gambar diproses dengan memecahkan menjadi channel CMYK
   - Grafik perbandingan Density dan Soliditas warna
   - Visualisasi perbedaan statistik
  
7. Detail Teknis
a. Konversi Warna, Menggunakan OpenCV untuk pengolahan gambar dan konversi warna.
b. Perbedaan Warna, Menerapkan perhitungan ΔE* CIELAB menggunakan scikit-image
c. Visualisasi, Menggunakan Matplotlib untuk semua output grafis
d. Perhitungan Density, Menghitung nilai rata-rata untuk setiap Channel CMYK
e. Pengukuran Soliditas, Menggunakan standar deviasi untuk menilai konsistensi warna

8. Metrik Output
a. Density Warna (persentase rata-rata untuk setiap saluran):
- Cyan
- Magenta
- Yellow
- Black (Key)

b. Soliditas Warna (standar deviasi dalam persentase):
- Mengukur keseragaman setiap saluran warna

c. Delta E
- Rata-rata perbedaan warna antara gambar target dan hasil

9. Persyaratan
a. Python 3.x
b. OpenCV
c. NumPy
d. Matplotlib
e. scikit-image
f. Google Colab (penggunaan berbasis web)

Alat ini sangat berguna untuk pengendalian kualitas dalam proses percetakan, membantu mengidentifikasi masalah reproduksi warna dan memastikan hasil cetakan yang konsisten.
