import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Judul aplikasi
    st.title('Horizontal Histogram with Scroll')

    # Data
    categories = ['Category ' + str(i) for i in range(1, 101)]
    values = np.random.randint(1, 100, size=100)

    # Tampilkan daftar kategori dengan scroll vertikal di sidebar
    selected_category = st.sidebar.selectbox('Select a Category', categories)

    # Jika kategori dipilih, tampilkan histogram untuk kategori tersebut
    if selected_category:
        # Plot histogram horizontal untuk kategori yang dipilih
        index = categories.index(selected_category)
        fig, ax = plt.subplots()
        ax.barh(selected_category, values[index], color='skyblue')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Categories')
        ax.set_title('Histogram for {}'.format(selected_category))

        # Tampilkan plot menggunakan Streamlit
        ax.set_xlim([0, 100])
        st.pyplot(fig)

if __name__ == "__main__":
    main()
