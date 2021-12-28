import os
import re
import textract
import pandas as pd


text = textract.process('sustainablefinance.pdf',language='nor',).decode()

text1 = re.split(r"\s*?\n\s*?\n\s*?",text)

def cleaning_text(raw_text):
    raw_text = raw_text.replace("\n", "").replace(" "," ").strip(" ")
    return re.sub(r'[^\w\s]' , '', raw_text).strip(' ')

Min_paragraph_characters = 200
paragraphs = []

for text_section in text1:
    clean_text = cleaning_text(text_section)
    if len(clean_text) >= Min_paragraph_characters:
        paragraphs.append(clean_text)

df = pd.DataFrame(paragraphs)
df.to_csv("paragraphs.csv")