# utils/resume_editor.py
from docx import Document

def tailor_resume(base_resume_path, keywords):
    doc = Document(base_resume_path)
    for para in doc.paragraphs:
        for keyword in keywords:
            if keyword.lower() in para.text.lower():
                para.text = para.text.replace(
                    keyword, f"{keyword} ✅"
                )
    tailored_path = "tailored_resume.docx"
    doc.save(tailored_path)
    return tailored_path
