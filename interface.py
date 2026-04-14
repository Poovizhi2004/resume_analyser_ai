import streamlit as st 
from analysis import analyze_resume

st.set_page_config('Resume Analyzer',page_icon='🛠️')

st.title('RESUME ANALYZER USING AI 🤖🧠🇦🇮👾' )

st.header(':blue[AI powered analyzer with given job description using AI 🤖]')


st.subheader('''This page helps you to compare the resume and the given job description and provides ATS score, probability of selection, good fit or not good fit, skills match, missing skills, soft skills match,linkedIn profile match and SWOT analysis of the resume as per the job description etc...📌''')

st.sidebar.subheader("Drop your resume here")

pdf_doc = st.sidebar.file_uploader('Click here',type=['pdf'])

st.sidebar.markdown('Designed by Poovizhi Punniyamoorthy 👨🏻‍💻')

st.sidebar.markdown('Git hub: https://github.com/Poovizhi2004')


job_des = st.text_area('Copy and paste the JD here ✍️',max_chars=10000)

submit = st.button('Get Results🎯')

if submit:
    with st.spinner('Loading....⌛'):
        analyze_resume(pdf_doc,job_des)