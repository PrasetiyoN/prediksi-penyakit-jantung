import pickle
import numpy as np
import streamlit as st

# Load model
model = pickle.load(open('heart_model.sav','rb'))

# Judul aplikasi
st.title('❤️ Prediksi Penyakit Jantung')
st.write("Masukkan data pasien di bawah ini:")

# Layout kolom 3x3
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Umur", min_value=1, max_value=120, value=50)
    cp = st.selectbox("Tipe Nyeri Dada (0-3)", [0,1,2,3])
    fbs = st.selectbox("Gula Darah > 120 mg/dl?", options=[('Ya', 1), ('Tidak', 0)])

with col2:
    sex = st.selectbox("Jenis Kelamin", options=[('Laki-laki', 1), ('Perempuan', 0)])
    trestbps = st.number_input("Tekanan Darah Istirahat", value=120)
    restecg = st.selectbox("Hasil EKG (0-2)", [0,1,2])

with col3:
    chol = st.number_input("Kolesterol", value=200)
    thalach = st.number_input("Denyut Jantung Maksimum", value=150)
    exang = st.selectbox("Angina karena latihan?", options=[('Ya', 1), ('Tidak', 0)])

# Baris ke-2
col4, col5, col6 = st.columns(3)

with col4:
    oldpeak = st.number_input("Oldpeak", value=1.0)

with col5:
    slope = st.selectbox("Slope ST (0-2)", [0,1,2])

with col6:
    ca = st.selectbox("Jumlah pembuluh darah utama (0-3)", [0,1,2,3])
    thal = st.selectbox("Thal (0=normal, 1=fixed, 2=reversible)", [0,1,2])

# Tombol Prediksi
if st.button("Prediksi"):
    input_data = np.array([
        age, sex[1], cp, trestbps, chol, fbs[1], restecg,
        thalach, exang[1], oldpeak, slope, ca, thal
    ]).reshape(1, -1)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Pasien TERKENA penyakit jantung!")
    else:
        st.success("✅ Pasien TIDAK terkena penyakit jantung.")
