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
    start = st.sidebar.slider('Start', min_value=0, max_value=len(categories)-10, step=1)
    end = start + 10
    selected_categories = categories[start:end]

    # Jika kategori dipilih, tampilkan histogram untuk kategori tersebut
    if selected_categories:
        # Plot histogram horizontal untuk kategori yang dipilih
        fig, ax = plt.subplots()
        for category in selected_categories:
            index = categories.index(category)
            ax.barh(category, values[index], color='skyblue')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Categories')
        ax.set_title('Histogram for Selected Categories')

        # Tampilkan plot menggunakan Streamlit
        st.pyplot(fig)

if __name__ == "__main__":
    main()
