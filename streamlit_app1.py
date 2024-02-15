import streamlit
streamlit.title('My new healthy dinner')
streamlit.header(' 🥣 Breakfast Menu')
streamlit.text('🥗 Dosa and Idli')
streamlit.text('🐔 chicken and Idli')
streamlit.text('🥑 avacado, Juice and fruits')
streamlit.text('🍞 egg and bread')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
