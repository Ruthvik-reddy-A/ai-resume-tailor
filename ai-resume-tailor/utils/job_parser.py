from openai import OpenAI
import streamlit as st

# Initialize OpenAI client using the Streamlit secrets config
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
def extract_keywords_from_jd(jd_text):
    """
    Uses GPT to extract key skills or keywords from a job description.
    """
    prompt = f"""
    Extract the key technical and soft skills from the following job description.

    Job Description:
    {jd_text}

    Format the output as a comma-separated list.
    """

    # Make the API call using new method
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    # Return the content (a comma-separated list of keywords)
    return response.choices[0].message.content.strip()
