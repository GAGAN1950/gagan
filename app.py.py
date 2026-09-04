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
    
    

