from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini model to get response

model=genai.GenerativeModel("gemini-2.0-flash-lite")



def get_response(input,image,prompt):
    response=model.generate_content([input,prompt,image[0]])
    return response.text


def input_image(upload):
    if upload is not None:
        bytes_data=upload.getvalue()
        image_parts=[{
            'mime_type': upload.type,
            'data': bytes_data      }
        ]
        return image_parts
    else:
        return FileNotFoundError("Image not found")
    
st.set_page_config(page_title="Invoice AI")
st.title("MULTILINGUAL INVOICE EXTRACTOR")
input=st.text_input("Enter the text from the invoice here",key="input")
upload=st.file_uploader("choose image..", type=['jpg','jpeg','png'])
image=""
if upload is not None:
    image=Image.open(upload)
    st.image(image,caption="Uploaded Image",use_container_width=True)

submit=st.button("Tell me about Invoice")

prompt='''you are an expert in understanding invoices. we will upload
image as invoice and you will tell us about the invoice. you can also provide answers based 
on the questions'''

if submit:
    image_data=input_image(upload)
    if image_data and isinstance(image_data, list) and len(image_data) > 0:
         response = get_response(input, image_data, prompt)
         st.subheader("Response:")
         st.write(response)
    else:
         st.error("No valid image uploaded.")
