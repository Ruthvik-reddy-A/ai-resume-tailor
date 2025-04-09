# utils/job_parser.py
import openai

openai.api_key = "w9oJykDtAL6EcJXIBzoOt274Ng1pnITUfBJq3DtUMGEDrS51w7kKLA3WwNHMLYuFwHFSGFf6SHT3BlbkFJ7Ef_Rs9UNh-MI-L3-uVJtg4MrWviV4F0rmRk08oGVgEVh73xMAb9xI7ZUzWfUj8iFg_7PyF6gA"  # Replace this with your API key

def extract_keywords_from_jd(jd_text):
    prompt = f"""
    Extract the key skills, tools, and technologies required from the following job description:
    ---
    {jd_text}
    ---
    Return them as a comma-separated list.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return [kw.strip() for kw in response['choices'][0]['message']['content'].split(',')]
