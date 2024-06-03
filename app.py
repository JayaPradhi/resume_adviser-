import streamlit as st
import google.generativeai as genai
import PyPDF2 as pdf 
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader  


genai.configure(api_key="AIzaSyA67Qp5CQpencHHxTbfLJRGL55Nq2jgn0Y")

def get_respons(input):
    model=genai.GenerativeModel("gemini-pro")
    respons=model.generate_content(input)
    return respons.text

def pdf_context(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

prompt=""" hey,you are a experience ATS(application tracking system with a deep understansing of data science,
data analytisc.you want to evaluate a resume based on given job description and you should provied best assistance  for improving there resume
assign a score base on job description and give me the missing word  with hidher accuracy and give some tipes of base in job description then give some important interview question base ob jd
and Grammar and Spelling Check in resume,
resume={resume}
job description={jd}

i want the respons is easy understandablr format
"""

st.markdown("<h1 style='color: red;'>Resume Adviser</h1>", unsafe_allow_html=True)
st.text("Enhance your resume using LLM (Large Language Models)")
jd=st.text_area("Job Description")
file=st.file_uploader("Uplode your resume",type='pdf')
submit=st.button("submit")
 
if submit:
    if file is not None:
        text=pdf_context(file)
        res=get_respons(prompt)
        st.subheader(res)
        
     

