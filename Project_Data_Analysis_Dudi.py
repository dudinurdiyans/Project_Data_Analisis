#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from PIL import Image
import os

# Judul aplikasi
st.title("Visualisasi Data Analisis")


# Daftar gambar yang akan ditampilkan
images = [
    "5 Kategori Produk dengan Penjualan Tertinggi.png",
    "Tren Penjualan 5 Kategori Produk Teratas Per Bulan.png",
    "5 Kategori Produk dengan Penjualan Terendah.png",
    "Tren Penjualan Seiring Waktu.png",
    "Perbandingan Jenis Pembayaran.png",
    "Perbandingan Status Pesanan.png",
    "Distribusi Customers Berdasarkan 5 Kota Teratas.png",
    "Hubungan antara Biaya Pengiriman dan Skor Ulasan per State.png",
    "Heatmap Hubungan antara Biaya Pengiriman dan Rata-rata Skor Ulasan per State.png",
    "Peta Penyebaran Seller Berdasarkan Kota.png"
]

# Menampilkan gambar
for img in images:
    img_path = os.path.join(image_folder, img)
    if os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, caption=img, use_column_width=True)
    else:
        st.error(f"Image {img} not found.")

