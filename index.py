import streamlit as st
import pandas as pd



def main():
    # Judul halaman
    # Use local CSS
    
   

    st.header("Pengumuman Hasil UH Turunan Fungsi Part-1")

    # Memuat data dari file CSV
    @st.cache_data()  # Menggunakan caching untuk meningkatkan performa
    def load_data(file_path):
        data = pd.read_csv(file_path, index_col=0)
        return data

    def color_cells(val):
        if pd.to_numeric(val, errors="coerce") > 60:
            return "color: #36f5ff"
            # return 'background-color: green'
        else:
            return "color: #E694FF"
            # return 'background-color: red'

    # Memuat data CSV
    file_path = "data.csv"
    data = load_data(file_path)
    data['TOTAL'] =  data['SKOR_DASAR']+data['SKOR_LANJUT']
    data['STATUS'] = data['TOTAL'].apply(lambda x: 'Tuntas' if x >= 60 else 'Tidak Tuntas')
    data = data[data['TOTAL'] >= 0]
    data = data.style.map(color_cells, subset=["TOTAL"])

    # Menampilkan data frame
    # st.write(data)
    st.dataframe(data)
    st.markdown(
        """
                <style>
                [data-testid="stElementToolbar"] {
                    display: none;
                }
                </style>
                """,
        unsafe_allow_html=True,
    )



if __name__ == "__main__":
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    main()