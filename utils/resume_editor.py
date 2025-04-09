# utils/resume_editor.py
#from docx import Document

#def tailor_resume(base_resume_path, keywords):
 #   doc = Document(base_resume_path)
  #  for para in doc.paragraphs:
   #     for keyword in keywords:
    #        if keyword.lower() in para.text.lower():
     #           para.text = para.text.replace(
      #             keyword, f"{keyword} ✅"
       #         )
   # tailored_path = "tailored_resume.docx"
    #doc.save(tailored_path)
    #return tailored_path
from openai import OpenAI
from docx import Document
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def rewrite_resume_with_gpt(resume_text, job_description):
    prompt = f"""
    Rewrite this resume to better match the job description.

    Job Description:
    {job_description}

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
