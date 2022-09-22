
import streamlit as slt
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
slt.title('My New Healthy Dinner')
slt.header('Breakfast Favorites')
slt.text('🍄 Omega 3 & Blueberry Oatmeal')
slt.text('🌿 Kale, Spinach & Rocket Smoothie')
slt.text('🐓 Hard-Boiled Free-Range Egg')
slt.header('🍌🍇 Build your own smoothie 🍉🍋')
fruits_selected=slt.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
slt.dataframe(fruits_to_show)

