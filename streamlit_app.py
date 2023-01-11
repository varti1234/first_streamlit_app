
import streamlit
streamlit.title('My parents New Healthly Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Blueberry')
streamlit.text('Kale,Spinach and Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build your own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=streamlit.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
Streamlit.dataframe(my_fruit_list)
