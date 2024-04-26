from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import base64
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

st.set_page_config("ATS Resume Expert")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text


#Below method will convert the pdf into the image of JPEG format so that Gemini can understand that


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


#Streamlit Code
st.header("Talk to your resume !!!")
input_text=st.text_area("Enter the job description :",key="input")
uploaded_file = st.file_uploader("Upload your resume in PDF Format", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1 = st.button("Tell me about the resume")
submit2 = st.button("Give me the percentage match with the job description")
submit3 = st.button("What are the weak points of this ?")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt3 = """You are an experienced Human Resource Manager. Your job is to help the candidate to let them know their weak areas as 
per the job description that has been provided. You need to be a guide for them to help them improve. Provide your response in bullet points 
so that its easier for anyone to understand"""
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is: ")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

if submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Response is: ")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

if submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is: ")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

