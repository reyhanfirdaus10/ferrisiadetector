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

manual_1 = Image.open('images/manual (1).png')

st.subheader('ABOUT')
st.caption('Ferrisia merupan genus baru di dunia, saat ini di dunia telah ditemukan 18 spesies dan di Indonesia baru ditemukan dua spesies genus Ferrisia, yaitu Ferrisia virgata, dan yang terbaru adalah spesies koya Ferrisa dasylirii (Cockerell) (Hemiptera: Pseudococcidae) telah direkam untuk pertama kali di Indonesia. Spesies ini dijumpai hidup pada tanaman Durio zibethinus Murray (Malvaceae), Gliricidia sepium (Jacq.) (Fabaceae), Hibiscus spp. (Malvaceae), Psidium guajava L. (Myrtaceae), Solanum torvum Swartz (Solanaceae), dan Theobroma cacao L. (Malvaceae) di beberapa bandar di daerah Bengkulu, Sumatera Selatan, Indonesia')
st.image(manual_1, caption='manual (1)')


