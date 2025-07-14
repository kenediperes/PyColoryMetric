PyColoryMetric - Program Analisis warna untuk konsistensi warna di industri percetakan.

1. Gambaran Umum
   - PyColoryMetric adalah program berbasis Python yang dirancang untuk menganalisis dan membandingkan:
   - Perbedaan warna antara gambar target dan hasil cetakan
   - Density dan Soliditas tinta CMYK
   - Keseragaman warna pada hasil cetakan

2. Fitur Utama
   - Konversi RGB ke CMYK untuk analisis percetakan
   - Delta E Measurement menggunakan standar CIE76
   - Density Analysis untuk setiap channel CMYK
   - Solidity Assessment untuk mengevaluasi konsistensi warna
   - Visual Comparison dengan breakdown channel CMYK
   - Statistical Visualization dalam bentuk grafik

3. Metrik Analisis
   - Density (nilai rata-rata)
     - Cyan Density
     - Magenta Density
     - Yellow Density
     - Black Density
   - Solidity (standard deviation)
     - Cyan Solidity
     - Magenta Solidity
     - Yellow Solidity
     - Black Solidity
   - Delta E (perbedaan warna total)

4. Cara Penggunaan
   - Jalankan script di Google Colab
   - Upload gambar target (referensi)
   - Upload gambar hasil cetakan
   - Program akan otomatis menampilkan
     - Perbandingan visual
     - Grafik density CMYK
     - Diagram perbedaan warna

5. Keunggulan
   - Menggunakan metode standar industri (CIE Lab)
   - Visualisasi komprehensif
   - Metrik kuantitatif untuk evaluasi kualitas
   - Cocok untuk quality control percetakan

6. Technical Requirements
   - Python 3.x + libraries standar
   - Google Colab environment
   - Format gambar yang didukung: JPG, PNG, dll.

7. Program ini membantu identifikasi masalah
   - Ketidakakuratan warna
   - Variasi density tinta
   - Ketidakkonsistenan hasil cetakan

8. Catatan Penting
   - Program ini dikhususkan untuk analisis hasil cetakan
   - Hasil analisis dapat digunakan sebagai acuan kalibrasi mesin cetak
   - Direkomendasikan untuk pengguna dengan pemahaman dasar color management
