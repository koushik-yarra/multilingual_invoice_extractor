# 📄 Multilingual Invoice Extractor  

## 🚀 Overview  
Multilingual Invoice Extractor is a Streamlit-based application that utilizes Google Gemini AI to analyze and extract information from invoices. The app supports text input and image uploads, providing insights about invoices in multiple languages.  

## 🎯 Features  
- 🌍 **Multilingual Support** – Extracts invoice data in multiple languages.  
- 🧠 **AI-Powered Analysis** – Uses Google Gemini AI for intelligent invoice understanding.  
- 🖼️ **Image Upload Support** – Users can upload invoice images for processing.  
- 🔍 **Text-Based Querying** – Allows users to ask questions about their invoices.  

## 🛠️ Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-repo/multilingual-invoice-extractor.git
   cd multilingual-invoice-extractor

   
Create a virtual environment (optional but recommended)

bash

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


Install dependencies

bash
pip install -r requirements.txt


Set up the API key
Create a .env file in the project root and add your Google API Key:

ini
GOOGLE_API_KEY=your_google_api_key_here



▶️ Usage
Run the Streamlit application:

bash
streamlit run app.py
Upload an invoice image or enter text to extract relevant information.

📚 Dependencies
The project requires the following Python libraries (from requirements.txt):

streamlit – Web UI framework
google-generativeai – Gemini AI integration
python-dotenv – Environment variable management
langchain – AI model chaining (for future enhancements)
PyPDF2 – PDF processing (potentially for invoice extraction)
chromadb – Vector database for storing AI responses (for future enhancements)

🔥 Future Enhancements
✅ Support for PDF invoices
✅ OCR-based invoice recognition
✅ Improved accuracy with fine-tuned AI models
✅ Storage and retrieval of invoice history

🤝 Contribution
Feel free to fork, modify, and contribute to the project!

