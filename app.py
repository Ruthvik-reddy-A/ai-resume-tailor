# app.py
import streamlit as st
import os
from utils.job_parser import extract_keywords_from_jd
from utils.resume_editor import tailor_resume
from utils.pdf_generator import convert_to_pdf

st.set_page_config(page_title="📄 AI Resume Tailor")
st.title("📄 AI Resume Tailor")
st.markdown("Upload your resume and job description – get a custom tailored resume in PDF!")

jd_text = st.text_area("📝 Paste the Job Description")

resume_file = st.file_uploader("📤 Upload your Resume (.docx)", type=["docx"])

if st.button("⚙️ Generate Tailored Resume"):
    if jd_text and resume_file:
        with open("uploaded_resume.docx", "wb") as f:
            f.write(resume_file.read())

        with st.spinner("🧠 Analyzing job description..."):
            keywords = extract_keywords_from_jd(jd_text)

        with st.spinner("✍️ Editing your resume..."):
            tailored_docx = tailor_resume("uploaded_resume.docx", keywords)

        with st.spinner("📄 Converting to PDF..."):
            tailored_pdf = convert_to_pdf(tailored_docx)

        with open(tailored_pdf, "rb") as f:
            st.success("✅ Resume tailored and ready!")
            st.download_button("📥 Download Tailored Resume (PDF)", f, file_name="tailored_resume.pdf")
    else:
        st.warning("Please upload both your resume and job description.")
