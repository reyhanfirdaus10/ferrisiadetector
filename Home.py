import streamlit as st

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
st.write(
    """Ferrisia Detector adalah aplikasi untuk mengidentifikasi spesies ferrisia dengan cara meng-upload gambar tubular duct"""
)
home_1 = Image.open('images/home (1).png')
home_2 = Image.open('images/home (2).png')
home_3 = Image.open('images/home (3).png')
st.subheader('Cara Pengguanaan Aplikasi')
st.caption('Gunakan preparat kutu putih yang ingin di identifikasi')
st.image(home_1, caption='home (1)')
st.caption('Amati dan ambil gambar bagian tubular duct yang memiliki struktur bentuk yang sempurna dengan menggunakan mikroskop')
st.image(home_2, caption='home (2)')
st.caption('Upload hasil gambar yang sudah di ambil ke applikasi Ferrisia Detector')
st.image(home_3, caption='home (3)')
link = '[Start Detect](https://reyhanfirdaus10-ferrisiadetector-home-amv9a1.streamlit.app/Detect)'
st.markdown(link, unsafe_allow_html=True)


st.markdown(
    """
        <style>
            @font-face {
            font-family: 'Poppins';
            src: url(https://fonts.googleapis.com/css2?family=Poppins&display=swap);
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
            }

            html, body, [class*="css"]  {
                font-family: 'Poppins';
            }
        </style>

    """,
        unsafe_allow_html=True,
)
