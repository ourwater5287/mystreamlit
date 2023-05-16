import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title("Map")
# x = st.slider('Select a value')
# st.write(x, 'squared is', x * x)
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50]+[37.76, - 122.4],columns=['lat', 'lon'])
st.map(df)

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
