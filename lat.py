import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.write("Infinity Coding Club")
df = pd.DataFrame({
  'No': [1, 2, 3, 4],
  'Nama' : ['Nurul','Nadia','Vino','Zahwa'],
  'Nilai': [98, 90, 83, 92]
})

df