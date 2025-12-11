import streamlit as st

st.title(":blue[penentuan bilangan ganjil dan genap]")
number =st.number_input("Insert a number", min_value=0, max_value=10000)
if number%2==1:
  st.write("bilangan ", number, "termasuk bilangan ganjil")
 else:
  st.write("bilangan ", number, "termasuk bilangan genap")
