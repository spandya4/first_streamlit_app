import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry oatmeal')
streamlit.text('Kale, Spinach & Recket Smothie')
streamlit.text('Hard-boiled Free-Range Eggs')
streamlit.text('🥑🍞Avacado toast')

streamlit.header('Build your own fruit smoothie ')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Apple")
#streamlit.text(fruityvice_response.json())

#New Section to display fruityvice api response.
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
  if not fruit_choice:
     streamlit.error("Please select a fruit to get information.")
  else:
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Apple")
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     streamlit.dataframe(fruityvice_normalized)
except URLError as e:
   streamlit.error()

#streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List contains:")
streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('thanks for adding ', fruit_choice)

my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
