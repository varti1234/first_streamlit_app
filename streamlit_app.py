
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

#create the repeatable code block(called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response=requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
  #new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
       streamlit.error("please select a fruit to get information.")
   else:
      back_from_function= get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
   
        
