## Tim: AI Revolusioner
### Proyek: AK-Bot (Angka Kredit Otomatis Berbasis AI)

#### 🏆 Inovasi AI Revolusioner untuk Efisiensi Penilaian Kinerja ASN

| Kategori Hackathon | Fokus Utama | Target Kemenangan |
| :--- | :--- | :--- |
| **Penilaian Kinerja ASN** | Otomatisasi Angka Kredit (AK) dan Percepatan Kenaikan Pangkat JF | Solusi **High-Impact** dengan eliminasi *bottleneck* birokrasi dan peningkatan integritas dokumen. |

### 1. 🎯 Latar Belakang Masalah (The Pain Point)

Proses penetapan Angka Kredit (AK) bagi Jabatan Fungsional (JF) saat ini adalah hambatan besar dalam efisiensi kepegawaian:

* **Waktu Pemrosesan Lambat:** Rata-rata membutuhkan **3-6 bulan** untuk verifikasi dan penetapan AK.
* **Risiko Integritas Dokumen:** Verifikasi dokumen (laporan, sertifikat) yang manual rentan terhadap manipulasi atau pemalsuan.
* **Keterlambatan Karir:** Proses lambat menghambat kenaikan pangkat, menurunkan motivasi, dan menghilangkan **Kepastian Karir** bagi ASN.

### 2. 💡 Solusi: AK-Bot (The AI Revolution)

**AK-Bot** adalah sistem AI yang mengubah penetapan AK dari proses birokrasi yang membebani menjadi fungsi **otomatik, *real-time*, dan terverifikasi** dalam ekosistem ASN Digital.

#### A. Arsitektur Inti AK-Bot (Integrasi End-to-End)

| Modul AI | Fungsi dan Inovasi | Integrasi Kunci |
| :--- | :--- | :--- |
| **1. WhatsApp In-take & CV/NLP Validator** | **Fungsi Revolusioner:** ASN mengirim dokumen (foto/PDF) via WhatsApp. **AI menggunakan OCR/CV** untuk ekstraksi data dan **NLP Forgery Detector** untuk memverifikasi keabsahan substansi dan integritas dokumen. | **Input:** WhatsApp Business API & **Lookup NIP Otomatis** dari nomor WA terdaftar di Server BKN. |
| **2. Rule-Based Allocation Engine** | Menerapkan aturan AK (PermenPAN-RB/Peraturan BKN) secara konsisten untuk mengalokasikan nilai AK secara instan. | **Data BKN:** Mengakses *database* butir kegiatan JF resmi (via API SIASN). |
| **3. Automatic Trigger & Dashboard** | Memantau akumulasi AK *real-time*. Saat AK minimum terpenuhi, sistem **otomatis** menghasilkan usulan kenaikan pangkat. | **Output ke Layanan BKN:** Mengirim *trigger* dan *payload data* otomatis ke sistem layanan SIASN. |
| **4. WhatsApp Communication Agent** | Mengirim notifikasi krusial **secara instan** (status *upload*, status validasi, pemberitahuan SK) langsung ke WA ASN. | **Output:** WhatsApp Business API untuk notifikasi personal. |

#### B. Fitur Unggulan (The Value Proposition)

* **WhatsApp End-to-End:** ASN mengajukan dokumen dan menerima pengumuman (termasuk SK) tanpa perlu *login* portal web.
* **Zero-Wait Policy:** Waktu penetapan AK berkurang dari bulan menjadi **kurang dari 7 hari**.
* **AI Integrity Check:** Mengeliminasi dokumen berisiko (duplikasi/pemalsuan) berkat fitur **Forgery Detector**.
* **Kenaikan Pangkat Otomatis:** Sistem yang proaktif mendorong promosi tanpa menunggu pengajuan manual dari ASN.

### 3. 📈 Dampak & Kelayakan Implementasi 

AK-Bot siap diimplementasikan karena dirancang untuk **Plug-and-Play** dengan API BKN:

| Metrik Dampak Kinerja | Target Implementasi (Skenario 1 Tahun) |
| :--- | :--- |
| **Efisiensi Waktu** | Mengurangi waktu penetapan AK dari 6 bulan menjadi **< 7 hari**. |
| **Peningkatan Integritas** | **Menurunkan insiden dokumen berisiko** berkat *filter* DFD AI. |
| **Kesiapan Integrasi** | Dirancang sebagai **Modul AI** yang dapat di-*deploy* langsung di **Server SIASN BKN**, menjamin keamanan dan akses data. |


---
**Tim AI Revolusioner:**
[Samsulbahri Masesa, Winand Liburtemar Lololuan, Lourenza R. Radjabaycolle]
