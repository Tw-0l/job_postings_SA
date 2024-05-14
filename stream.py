import streamlit as st
import pandas as pd 
import webbrowser


df = pd.read_csv('Jadarat_data.csv')

st.markdown('# Are you looking for a job?')
st.image('job.jpeg', caption='looking for job is so Stressful we feel you')

st.markdown('''## We know that can be hard, but don't worry after you read our story, you will change your view 
first here sample of our data that we collected from (Jadarat)''')
st.write(df)

st.markdown('### Riyadh has the highest job postings in the kingdom, but what region next?:thinking_face::thinking_face:')
st.image('Q1.png')
st.markdown('''
The difference between Riyadh region and Makkah was surprising,
but remember that Riyadh is the capital of the kingdom of Saudi Arabia so its make scenes 
''')
st.markdown('''
### I know you're so anxious about the job that way 
### the following chart will make you happy because we're going to talk about :moneybag::heavy_dollar_sign:
''')
st.image('Q3.png',caption='Most frequent salary for fresh graduate.')
st.markdown('''
In summary, navigating the job market can be stressful, but insights from Jadarat's data offer a fresh perspective. 
Riyadh leads in job postings, likely due to its capital status. Encouragingly, data on salary for fresh graduates suggests promising financial opportunities. 
So, while the job hunt may seem daunting, Jadarat's data provides valuable guidance for job seekers.

''')

url = 'https://youtu.be/lU6b1bGvfdM?si=j6hJE4re9vKc_T-k'

if st.button('Feeling sad ?!'):
    webbrowser.open_new_tab(url)
