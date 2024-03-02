import streamlit as st
def page_2():
    st.title("Halaman 2")
    st.write('Halaman ini digunakan untuk Menampilkan youtube')
    st.video('https://www.youtube.com/watch?v=OIViEk9Sy_E')

    st.latex(r'''
    f'(x) = \mathop {\lim }\limits_{h \to 0} \frac{{f(x + h) - f(x)}}{h}
    ''')
    st.latex(r'''
    f'(x) = n{u^{n - 1}}.u'
    ''')