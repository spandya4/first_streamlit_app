import streamlit

streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('Kale, Spinach & Recket Smothie')
streamlit.text('Hard-boiled Free-Range Eggs')
streamlit.text('🥑🍞Avacado toast')

streamlit.header('Build your own fruit smoothie ')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
