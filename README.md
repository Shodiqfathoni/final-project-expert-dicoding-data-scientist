# Proyek Akhir: Menyelesaikan Permasalahan institute jaya jaya maju

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik.

### Permasalahan Bisnis
permasalahan dari institute jaya jaya maju adalah jumlah dropout yang tinggi bahkan mencapai 30% lebih, ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu peran kita sebagai data scientist dibutuhkan untuk membuat sebuah solusi atau alat yang bisa mendiagnosa awal untuk mengetahui mahasiswa mana yang terindikasi dropout sehingga pihak institut bisa mengambil langkah pencegahan berupa diberi arahan atau solusi sehingga dropout rate pada institute jaya jaya maju bisa berkurang 

### Cakupan Proyek
1. memuat data 

2. menganalisis permasalahan 

3. membuat dashboard untuk menganalisis data

4. membuat model machine learning 

5. mendeploy model machine learning ke streamlit 

### Persiapan

Sumber data: "postgresql://postgres.zyjmkzlykunzxtxdxzio:cHBjk9uP9A3kC9lq@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"

Setup environment:

1. mkdir final_project_expert_idcamp2

2. cd final_project_expert_idcamp2

3. pipenv install

4. pipenv shell

5. pip install -r requirements.txt 

## Business Dashboard
dashboard yang saya buat membahas tentang apa yang mempengaruhi dropout rate pada institute ini tapi sebelum itu saya harus membuat rumus dropout rate terlebih dahulu menggunakan rumus SUM(CASE WHEN Status = "Dropout" THEN 1 ELSE 0 END) / COUNT(Status),setelah itu baru saya bisa menganalisis seperti jurusan mana yang mempunyai dropoput tertinggi, diantara evening dan daytime ternyata mahasiswa yang kehadirannya evening terindikasi dropout, mahasiswa yang mempunyai hutang terindikasi dopout daripada yang tidak mempunyai hutang, kemudian apakah diantara mahasiswa pemegang beasiswa dan mahasiswa tidak pemegang beasiswa ternyata yang pemegang beasiswa justru dropratenya lebih rendah untuk selengkapnya bisa akses https://lookerstudio.google.com/reporting/bc0d61f2-4ce9-487c-9c86-1fb2cee140fd

## Menjalankan Sistem Machine Learning
ada dua cara untuk menjalankan machine learning yaitu local maupun cloud

1.menjalankan machine learning secara lokal dimulai dengan cara memilih berkas graduation_analysis_app.py, kemudian run code tersebut nanti di terminal akan mucul Warning: to view this Streamlit app on a browser, run it with the following command,setelah itu ikuti command yang ditunjukkan oleh warning tersebut dan run command tersebut di terminal,kemudian akan muncul tulisan local url dan juga network url,kemudian pilih local url,kemudian anda akan muncul sebuah app prediksi

2.menjalankan machine learning lewat cloud anda harus mempunyai akun streamlit cloud dan github kemudian deploy lewat creat app isi apa saja yang diminta oleh creat app kemudian pencet deploy dan tunggu hingga proses selesai,nanti akan muncul di bagian your app untuk menjalankannya tinggal klik app yang baru dibuat tadi atau bisa langsung mengakses link ini: https://final-project-idcamp-h6tcq3kfn83lp96h2gub4h.streamlit.app/

3.cara menggunakan prototype tersebut cukup mudah,anda hanya perlu memilih parameter yang anda inginkan sudah tersedia dimasing masing kolom tersebut,jika sudah memilih parameter tersebut kemudian pada bagian bawah ada view the raw data,ini adalah tampilan parameter anda yang sudah dipilih dari kolom yang diatas, silahkan periksa apakah data yang tercantum di view raw data tersebut sesuai dengan pilihan anda,kemudian tekan predict dan data yang tadi anda pilih akan diproses, anda bisa melihat prosesnya di kolom view preprocesed data kemudian paling bawah akan muncul status prediction salah satu dari graduate,enrolled,dan dropout kemudian tahapan pun selesai

## Conclusion
kesimpulan dari hasil analisis proyek ini adalah dropout rate yang tinggi disebabkan banyak faktor tapi faktor yang paling penting yaitu mahasiswa yang mempunyai hutang cenderung untuk dropout dan juga mahasiswa yang mempunyai hutang menjadi penyumbang tinggi dropout rate untuk itu kampus harus lebih memperhatikan mahasiswa yang mempunyai hutang agar bisa menekan angka dropout rate

### Rekomendasi Action Items
1. menganalisis mahasiswa yang terindikasi dropout menggunakan machine learning yang telah dibuat
2. setelah tau mahasiswa yang terindikasi dropout, baru dilakukan konfirmasi kepada mahasiswa yang bersangkutan apakah ada indikasi dropout 
3. jika benar teridikasi dropout maka kampus harus segera melakukan tindakan untuk menyelesaikan masalah dari mahasiswa tersebut
4. untuk kasus ini misalkan mahasiswa terindikasi dropout karena mempuyai hutang, kampus bisa melakukan tindakan seperti :    
    -Bimbingan Keuangan:
        Berikan konseling keuangan kepada mahasiswa yang memiliki masalah hutang. Ini bisa mencakup bantuan dalam mengatur anggaran, memahami pinjaman mahasiswa, dan merencanakan pembayaran hutang.

    -Bantuan Keuangan:
        Tawarkan beasiswa, hibah, atau bantuan keuangan lainnya yang dapat membantu meringankan beban keuangan mahasiswa yang berisiko drop out.

    -Fleksibilitas Pembayaran:
        Sediakan opsi pembayaran yang fleksibel, seperti rencana pembayaran yang dapat disesuaikan atau penundaan pembayaran untuk mahasiswa yang mengalami kesulitan keuangan.

    -Dukungan Akademik:
        Berikan dukungan akademik seperti bimbingan belajar, program mentor, dan lokakarya keterampilan belajar untuk membantu mahasiswa tetap berprestasi meskipun menghadapi masalah keuangan.

    -Pekerjaan Kampus:
        Sediakan peluang pekerjaan di kampus yang dapat membantu mahasiswa mendapatkan penghasilan tambahan tanpa harus meninggalkan lingkungan akademis.

    -Program Pengelolaan Stres:
        Tawarkan program yang membantu mahasiswa mengelola stres, seperti konseling psikologis, workshop manajemen stres, dan aktivitas rekreasi.

    -Keterlibatan Orang Tua:
        Libatkan orang tua atau wali dalam proses pendidikan dan keuangan mahasiswa, sehingga mereka dapat memberikan dukungan tambahan.

    -Komunikasi Proaktif:
        Lakukan komunikasi proaktif dengan mahasiswa yang menunjukkan tanda-tanda kesulitan keuangan, dan tawarkan bantuan serta solusi sebelum masalah tersebut menjadi terlalu besar.

    -Monitoring dan Evaluasi:
        Pantau secara berkala status keuangan mahasiswa dan evaluasi efektivitas program dukungan yang ada untuk memastikan mereka tetap relevan dan efektif.

    -Kemitraan dengan Lembaga Keuangan:
        Jalin kemitraan dengan lembaga keuangan yang dapat memberikan program manajemen hutang atau konsolidasi hutang yang menguntungkan bagi mahasiswa.
