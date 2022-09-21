
import streamlit as slt
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/furit_macros.txt")
slt.title('My New Healthy Dinner')
slt.header('Breakfast Favorites')
slt.text('🍄 Omega 3 & Blueberry Oatmeal')
slt.text('🌿 Kale, Spinach & Rocket Smoothie')
slt.text('🐓 Hard-Boiled Free-Range Egg')
slt.header('🍌🍇 Build your own smoothie 🍉🍋')
slt.dataframe(my_fruit_list)

