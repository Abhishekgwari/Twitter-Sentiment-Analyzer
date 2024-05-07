import streamlit as st
import pickle
import time

model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

st.title('Twitter Sentiment Analysis')

tweet = st.text_input('Enter your tweet')

submit = st.button('Predict')

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write('Prediction time taken: ', round(end-start, 2), 'seconds')
    st.write(prediction[0])
    
st.image('img.png', caption='Your Image', width=500, use_column_width=True)

st.markdown(
    f"""
    <style>
        .reportview-container .main .block-container{{
            max-width: 100%;
            padding-top: 1rem;
            padding-right: 1rem;
            padding-left: 1rem;
            padding-bottom: 1rem;
        }}
        .reportview-container .main {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 90vh;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
