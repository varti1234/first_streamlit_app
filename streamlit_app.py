
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



streamlit.header("The fruit load list contains:")
#snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
 # add abutton to load the fruit
 if streamlit.button ('Get Fruit load List')
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruit_load_list
    streamlit.dataframe(my_data_rows)
#add_my_fruit=streamlit.text_input('What fruit would you like to add?','Jackfruit') 
#streamlit.write('The user entered ', add_my_fruit)

#my_cur.execute("insert into fruit_load_list values('from streamlit')")
