from flask import Flask,request,jsonify


import streamlit as st
import pickle

header=st.header("Sentiment Analyzer")

model = pickle.load(open('model.pkl','rb'))
col2,col3= st.columns([1,1])
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False


def callback():
    st.session_state.button_clicked = True
with col2:
    text=st.text_area('Test with your own text',on_change=callback,
                      placeholder='This is the best sentiment analysis tool ever!!!',height=200)
    if st.button('Classify text'):
        st.session_state.button_clicked = True
        result=model.predict([text])
        with col3:
            col4,col5=st.columns([1,1])
            with col5:
                    if  result== 'positive':
                        st.image('happy.png',width=100,caption="Happy Face")
                        with col4:
                            st.text("Review")
                            st.write("Positive")
                    elif result =='negative':
                        st.image('sad.png', width=100,caption="UnHappy Face")
                        with col4:
                            st.text("Review")
                            st.write("Negative")
