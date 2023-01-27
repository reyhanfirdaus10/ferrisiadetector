import streamlit as st
from PIL import Image

hidemenu =  """
<style>
#MainMenu{
    visibility:hidden;
}
footer{
    visibility:visible;
}
footer:after{
    content:'Copyright © 2022 Universitas Bengkulu';
    display:block;
    position:relative;
    color:tomato;
}
</style>
"""

st.markdown("# :red[FERRISIA] DETECTOR")

about_1 = Image.open('images/about (1).png')

st.subheader('ABOUT')
st.caption('APA ITU FERRISIA ?')
st.caption('Ferrisia adalah Genus dari famili Kutu Putih (Pseudococcidae)')
st.image(about_1, caption='about (1)')
st.caption('Spesies Ferrisia di indonesia baru ditemukan sebanyak dua spesies yaitu spesies Ferrisia Virgata dan Ferrisia Dasylirii sedangkan di Dunia sudah di temukan 18 spesies Ferrisia')
st.caption('Oleh karena itu Aplikasi ini berguna untuk mendeteksi Spesies ferrisia yang di harapkan dapat mempermudah proses identifikasi kutu putih sehingga memungkinkan ditemukannya spesies baru ')


