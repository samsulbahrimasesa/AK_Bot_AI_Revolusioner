import streamlit as st
import random
import time

st.set_page_config(layout="wide")
st.title("AK-Bot: Angka Kredit Otomatis Berbasis AI")
st.subheader("Tim: AI Revolusioner - Solusi Digitalisasi Kinerja ASN")
st.markdown("---")

NAMA_ASN = "Krisna Dian, S.E., M.Si."
PANGKAT = "Analis Kebijakan Muda"
AK_SAAT_INI = 85.0
AK_TARGET = 100.0

def run_ak_bot_process(current_ak, new_ak_value, doc_status):

    if doc_status == "RISIKO TINGGI":
        st.error("⚠️ STATUS: RISIKO TINGGI Dideteksi oleh Forgery Detector.")
        st.markdown("Dokumen **DITOLAK** dan ditahan untuk Verifikasi Manual. Proses AK dihentikan.")
        return 

    st.success("✅ Verifikasi Dokumen Administratif: DFD Lolos (SAH)")
    st.markdown("Dokumen Lolos pemeriksaan Computer Vision. Lanjut ke Perhitungan Angka Kredit.")
    time.sleep(1) 
    st.markdown("---")

    with st.spinner('AK-Bot sedang menghitung dan memperbarui data di Server SIASN BKN...'):
        time.sleep(3) 

    ak_total_baru = current_ak + new_ak_value
    ak_dibutuhkan = AK_TARGET - ak_total_baru
    
    st.header("📊 Hasil Akhir Angka Kredit (AK) dan Integrasi SIASN")
    st.metric(
        label=f"Total AK Terbaru (Diperbarui di DB BKN)", 
        value=f"{ak_total_baru:.1f} AK", 
        delta=f"+{new_ak_value:.1f} AK (Penetapan AI)"
    )
    
    wa_message = ""
    if ak_total_baru >= AK_TARGET:
        st.balloons()
        st.success(f"🎉 SELAMAT! AK Mencapai {ak_total_baru:.1f} AK (Target Terpenuhi).")
        st.warning("🔥 **AUTOMATIC TRIGGER AKTIF:** Sistem mengirimkan usulan kenaikan pangkat ke SIASN!")
        wa_message = "SK Kenaikan Pangkat Anda sedang diproses. Detail akan dikirim ke WhatsApp Anda dalam 24 jam. Selamat!"
    else:
        st.info(f"AK Anda: {ak_total_baru:.1f} AK. Sisa AK yang Dibutuhkan: **{ak_dibutuhkan:.1f} AK**.")
        wa_message = f"Penambahan AK +{new_ak_value:.1f} berhasil. Total AK Anda: {ak_total_baru:.1f} AK. Sisa {ak_dibutuhkan:.1f} AK menuju target."

    st.markdown("---")
    st.header("📲 Notifikasi Instan (WhatsApp Communication Agent)")
    st.success("✅ Notifikasi WA Terkirim dalam 5 Detik.")
    
    st.markdown(f"""
    <div style="border: 2px solid #25D366; padding: 15px; border-radius: 8px; background-color: #E6FFEC; margin-top: 10px;">
        **[Simulasi WhatsApp Outbound - Dari BKN Layanan AK-Bot]**
        <p style='color:#075E54; margin-top: 10px; font-weight: bold;'>Kepada Yth. Sdr/i {NAMA_ASN}.</p>
        <p style='color:#075E54; margin-top: 5px;'>{wa_message}</p>
    </div>
    """, unsafe_allow_html=True)


st.header("🔬 Demo Simulasi AK-Bot (Input Fungsional)")
st.info(f"Demo untuk ASN: **{NAMA_ASN}** | Pangkat: **{PANGKAT}** | AK Awal: **{AK_SAAT_INI} AK**")
st.markdown("---")

doc_upload_status = st.radio(
    "Simulasi Status Dokumen yang Di-Upload (DFD Check):",
    ("Dokumen BERSIH", "RISIKO TINGGI"),
    index=0,
    horizontal=True
)

ak_input_value = st.slider("Nilai AK yang Ditetapkan (Simulasi Rule-Based Engine):", 0.0, 15.0, 5.0, 0.5)

st.markdown("---")

if st.button("Jalankan AK-Bot End-to-End Process", type="primary"):
    run_ak_bot_process(
        current_ak=AK_SAAT_INI, 
        new_ak_value=ak_input_value, 
        doc_status="RISIKO TINGGI" if doc_upload_status == "RISIKO TINGGI" else "SAH"
    )
