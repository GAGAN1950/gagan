import streamlit as st
a=st.chat_input("enter your command")
if a:
    st.chat_message("user").write(a)
    if a.lower()=="hi":
        st.chat_message("ai").write("hello")
    elif a.lower()=="bye":
        st.chat_message("ai").write("goodbye")
    elif a.lower()=="how are you":
        st.chat_message("ai").write("i am fine!")
    elif a.lower()=="what is your name":
        st.chat_message("ai").write("i am Gagan.R")
    elif a.lower()=="introduce yourself":
        st.chat_message("ai").write("i am gagan from ssmrv college and i have pursued bca with cybersecurity and cloud architecture")
    elif a.lower()=="thanks":
        st.chat_message("ai").write("no problem!")
    elif a.lower()=="what about you":
        st.chat_message("ai").write("good")
    elif a.lower()=="can i know where are you from":
        st.chat_message("ai").write("i am from bangalore")
    elif a.lower()=="how was the day":
        st.chat_message("ai").write("good")
    elif a.lower()=="which year are you studing in":
        st.chat_message("ai").write("i am studing in the second year BCA")
    elif a.lower()=="which is your favourite movie":
        st.chat_message("ai").write("my favourite movie is jana nayagan and jaati ratnalu")
    

