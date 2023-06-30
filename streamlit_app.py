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
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
  if not fruit_choice:
     streamlit.error("Please select a fruit to get information.")
  else:
     back_from_function = get_fruityvice_data(fruit_choice)
     streamlit.dataframe(back_from_function)
except URLError as e:
   streamlit.error()

streamlit.header("The fruit load list contains:")
#streamlit.stop()
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = def get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('thanks for adding ', fruit_choice)

my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
