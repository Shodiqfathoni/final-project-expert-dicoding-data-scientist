# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik.

### Permasalahan Bisnis
jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Cakupan Proyek
1. memuat data 

2. menganalisis permasalahan 

3. membuat dashboard untuk menganalisis data

4. membuat model machine learning 

5. mendeploy model machine learning ke streamlit cloud

### Persiapan

Sumber data: "postgresql://postgres.zyjmkzlykunzxtxdxzio:cHBjk9uP9A3kC9lq@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"

Setup environment:

1. mkdir final_project_expert_idcamp

2. cd final_project_expert_idcamp

3. pipenv install

4. pipenv shell

5. pip install numpy pandas scipy matplotlib seaborn jupyter sqlalchemy scikit-learn==1.2.2 joblib==1.3.1 streamlit==1.24.0 

6. code .

## Business Dashboard
dashboard yang saya buat membahas tentang apa yang mempengaruhi dropout rate pada institute ini sehingga menjadi tinggi, https://lookerstudio.google.com/reporting/bc0d61f2-4ce9-487c-9c86-1fb2cee140fd

## Menjalankan Sistem Machine Learning
1. mengupload semua berkas model ke github milik kita yaitu data preprocessing.py, graduation_analysis_app.py, pip file, pip file.lock,    prediction.py, requirements.txt

2. login ke akun streamlit cloud 

3. cari creat app

4. pilih repository github yang memuat semua berkas model kita tadi

5. branch - main

6. main file path kita pilih -graduation_analysis_app.py

7. tekan tombol deploy 

8. untuk lebih lengkapnya bisa dilihat pada link ini: https://final-project-idcamp-h6tcq3kfn83lp96h2gub4h.streamlit.app/

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
