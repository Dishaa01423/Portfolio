import streamlit as st
import pandas as pd

st.set_page_config(layout= "wide")

col1 ,col2 = st.columns([1.5,1.5])

with col1:
    st.image("Photo.jpg",width=350)

with col2:
    st.title("About Me")
    content="""My name is Disha Mathankar. I am 20 and pursuing my BTech degree from Samrat Ashok Technological Institute, Vidisha.
     I thrive on continuous learning and challenges and find joy in coding. My journey in this field began when I opted for my higher education. 
     Since then, I've been dedicated to continuously learning and growing in my craft.
     """
    st.info(content)

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!!")
col3,empty_column2, col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index,row in df[:6].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"])
        st.write(f"[Link to GitHub]({row['url']})")

with col4:
    for index, row in df[6:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"])
        st.write(f"[Link to GitHub]({row['url']})")