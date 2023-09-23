import streamlit as st
from send_email import send_emails

st.header("Contact Me")

with st.form(key = "email_forms"):
    user_email = st.text_input("Your email address",placeholder="Enter your email...")
    raw_message = st.text_area("Your message",placeholder="Message...")
    # message = message + "\n" + user_email
    # or
    message = f"""\
Subject: New email from {user_email}
    
From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_emails(message)
        st.info("Your email was sent!!")