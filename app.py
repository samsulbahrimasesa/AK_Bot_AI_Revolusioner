import streamlit as st
import pandas as pd
import time
import random

# --- Konfigurasi Awal ---
st.set_page_config(layout="wide")
st.title("AK-Bot ADMIN DASHBOARD: Monitoring & Penetapan Angka Kredit")
st.subheader("Tim: AI Revolusioner - Solusi Digitalisasi Kinerja ASN untuk Administrator")
st.markdown("---")

# DATA SIMULASI PEGAWAI (DUMMY DATABASE BKN)
data_pegawai = {
    'Nama ASN': ['Winand Liburtemar, S.E., M.Si.', 'Lourenza R. Radjabaycolle, S.T.', 'Ajon Rambing, M.Hum.', 'Joko Susanto, S.Pd.'],
    'Pangkat/Jabatan': ['Analis Kebijakan Muda', 'Pranata Komputer Madya', 'Arsiparis Pertama', 'Guru Ahli Muda'],
    'No. WA': ['+62812xxxxxx', '+62856xxxxxx', '+62878xxxxxx', '+62896xxxxxx'],
    'AK Saat Ini': [85.0, 95.0, 70.0, 80.0],
    'AK Target': [100.0, 150.0, 100.0, 150.0]
}
df = pd.DataFrame(data_pegawai)

# DATA BOT
NO_WA_BOT = "+62 812 3456 7890" 
NAMA_BOT = "BKN AK-Bot Assistant"
AK_DUMMY_PENETAPAN = 8.0 # Nilai AK tetap (Simulasi hasil OCR/CV)

# --- FUNGSI INTI: SIMULASI PROSES AK-BOT ---
def run_ak_bot_process(pegawai_data, new_ak_value, doc_status):
    """Mensimulasikan alur kerja end-to-end AK-Bot untuk pegawai yang dipilih."""
    
    st.markdown(f"### Proses AK-Bot untuk: {pegawai_data['Nama ASN']} ({pegawai_data['No. WA']})")
    st.info(f"AK Awal: **{pegawai_data['AK Saat Ini']} AK** | Target: **{pegawai_data['AK Target']} AK**")
    
    # 1. Simulasi Forgery Detector (DFD)
    st.header("1. Validasi Dokumen (DFD & NLP Validator)")
    if doc_status == "RISIKO TINGGI":
        st.error("⚠️ STATUS: RISIKO TINGGI Dideteksi oleh Forgery Detector.")
        st.markdown("Dokumen **DITOLAK** dan ditahan untuk Verifikasi Manual. Proses AK dihentikan.")
        return 

    st.success("✅ Verifikasi Dokumen Administratif: DFD Lolos (SAH)")
    st.markdown("Dokumen Lolos pemeriksaan Computer Vision. Lanjut ke Perhitungan Angka Kredit.")
    time.sleep(1) 
    st.markdown("---")

    # 2. Simulasi Perhitungan dan Penetapan AK
    st.header("2. Perhitungan Angka Kredit (Rule-Based Engine)")
    with st.spinner('AK-Bot sedang menghitung dan memperbarui data di Server SIASN BKN...'):
        time.sleep(3) 

    ak_total_baru = pegawai_data['AK Saat Ini'] + new_ak_value
    ak_dibutuhkan = pegawai_data['AK Target'] - ak_total_baru
    
    # Tampilan Metrik
    st.markdown("### 📊 Hasil Akhir Angka Kredit (AK) dan Integrasi SIASN")
    st.metric(
        label=f"Total AK Terbaru", 
        value=f"{ak_total_baru:.1f} AK", 
        delta=f"+{new_ak_value:.1f} AK (Penetapan AI)"
    )
    
    wa_message = ""
    if ak_total_baru >= pegawai_data['AK Target']:
        st.balloons()
        st.success(f"🎉 SELAMAT! AK Mencapai {ak_total_baru:.1f} AK (Target Terpenuhi).")
        st.warning("🔥 **AUTOMATIC TRIGGER AKTIF:** Sistem mengirimkan usulan kenaikan pangkat ke SIASN!")
        wa_message = "SK Kenaikan Pangkat Anda sedang diproses. Detail akan dikirim ke WhatsApp Anda dalam 24 jam. Selamat!"
    else:
        st.info(f"AK Anda: {ak_total_baru:.1f} AK. Sisa AK yang Dibutuhkan: **{ak_dibutuhkan:.1f} AK**.")
        wa_message = f"Penambahan AK +{new_ak_value:.1f} berhasil. Total AK Anda: {ak_total_baru:.1f} AK. Sisa {ak_dibutuhkan:.1f} AK menuju target."

    # 3. Simulasi Notifikasi Instan via WhatsApp
    st.markdown("---")
    st.header("📲 Notifikasi Instan (WhatsApp Communication Agent)")
    st.success(f"✅ Notifikasi WA Terkirim ke {pegawai_data['No. WA']} dalam 5 Detik.") 
    
    st.markdown(f"""
    <div style="border: 2px solid #25D366; padding: 15px; border-radius: 8px; background-color: #E6FFEC; margin-top: 10px;">
        **[Simulasi WhatsApp Outbound - Dari {NAMA_BOT} ({NO_WA_BOT})]**
        <p style='color:#075E54; margin-top: 10px; font-weight: bold;'>Kepada Yth. Sdr/i {pegawai_data['Nama ASN']} ({pegawai_data['No. WA']}).</p>
        <p style='color:#075E54; margin-top: 5px;'>{wa_message}</p>
    </div>
    """, unsafe_allow_html=True)


# --- STRUKTUR UTAMA (MAIN APP) ---
st.header("🔬 Dashboard Monitoring Angka Kredit Pegawai")

# Tampilkan tabel data pegawai
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("---")

# Input Admin: Memilih Pegawai untuk Diproses
selected_name = st.selectbox(
    "Pilih ASN yang Berkasnya Ingin Diproses (Simulasi Admin BKN):",
    df['Nama ASN']
)

# Ambil data pegawai yang dipilih
selected_pegawai = df[df['Nama ASN'] == selected_name].iloc[0].to_dict()

st.info(f"Anda memilih: **{selected_pegawai['Nama ASN']}** (AK Awal: {selected_pegawai['AK Saat Ini']} AK)")

# INPUT UTAMA: FILE UPLOADER 
st.subheader("Trigger AK-Bot: Upload Dokumen Kinerja (Simulasi Kiriman WA)")
uploaded_file = st.file_uploader(
    f"Upload Dokumen untuk {selected_name}",
    type=['pdf', 'jpg', 'png']
)

# Logic Trigger: Proses berjalan otomatis HANYA ketika file diunggah
if uploaded_file is not None:
    st.markdown("---")
    
    # ------------------------------------------------------------------------------------------------
    # --- LOGIKA DFD & TRIGGER UTAMA: MEMILIH STATUS DFD & NILAI OTOMATIS BERDASARKAN FILE ---
    # ------------------------------------------------------------------------------------------------
    
    # DFD Logic: Simulasi DFD (Gunakan radio button untuk demo DFD)
    st.markdown("#### 1A. Simulasi Status Forgery Detector (Admin Override)")
    doc_status_radio = st.radio(
        "Apakah DFD AI mendeteksi RISIKO TINGGI pada file ini?",
        ("TIDAK RISIKO (Lolos)", "RISIKO TINGGI (Tolak)"),
        index=0,
        horizontal=True
    )
    
    doc_status_simulasi = "RISIKO TINGGI" if doc_status_radio == "RISIKO TINGGI (Tolak)" else "SAH"

    st.success(f"✅ Dokumen '{uploaded_file.name}' berhasil diunggah.")
    st.markdown(f"**AI OCR/CV:** Sedang mengekstrak data dan menetapkan nilai AK sebesar **{AK_DUMMY_PENETAPAN} AK**...")
    
    time.sleep(1) 
    
    # Memanggil fungsi utama dengan data pegawai yang dipilih
    run_ak_bot_process(
        pegawai_data=selected_pegawai, 
        new_ak_value=AK_DUMMY_PENETAPAN, 
        doc_status=doc_status_simulasi
    )
