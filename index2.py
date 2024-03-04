import pandas as pd
import streamlit as st

# Fungsi untuk memberikan warna pada cell
def color_cells(val):
    if pd.to_numeric(val, errors='coerce') > 60:
        return 'color: green'
        # return 'background-color: green'
    else:
        return 'color: red'
        # return 'background-color: red'

# Membaca file data.csv
df = pd.read_csv('data.csv')

# Memberikan warna pada cell di kolom 'nilai'
styled_df = df.style.map(color_cells, subset=['NilaiLanjut'])

# Menampilkan dataframe pada aplikasi Streamlit
st.dataframe(styled_df)
