PDF Summarizer with Google Gen AI
Overview
This repository contains a Streamlit application that utilizes Google Gen AI to generate summaries of uploaded PDF files. The app supports generating paper-wise summaries and white paper summaries. It uses environment variables to keep sensitive information, such as API keys, secure.

Features
Upload multiple PDF files.
Enter the topic of the papers.
Generate summaries for individual papers.
Generate a comprehensive white paper summary.
Download the generated summaries as DOCX files.
Progress bar to indicate the status of summary generation.
Requirements
Python 3.x
Streamlit
PyPDF2
Google Gen AI SDK
Installation
Clone the Repository:

bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Create a Virtual Environment (Optional but recommended):

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

bash
pip install -r requirements.txt
Set Up Environment Variables:

For local development, create a .env file in the root directory and add your environment variables:

env
GENAI_API_KEY=your-api-key-here
For GitHub Actions, add secrets via the GitHub repository settings as described in the GitHub documentation.

Usage
Run the Streamlit App:

bash
streamlit run app.py
Upload PDF Files:

Navigate to the "Upload PDFs" section in the app.
Select and upload your PDF files.
Enter the topic of the papers and click "Submit."
Generate Summaries:

Choose "Generate Paper-Wise Summary" or "Generate White Paper Summary" from the navigation menu.
Modify the sections if needed and click the respective "Submit Sections" button.
Download the generated summaries by clicking the download buttons once the processing is complete.
Deployment
Streamlit Cloud:

Follow the Streamlit Cloud deployment guide to deploy your app.
Add your environment variables (e.g., GENAI_API_KEY) in the "Secrets" section of your Streamlit Cloud app settings.
GitHub Actions:

Configure GitHub Actions to deploy your app using the provided .github/workflows/deploy.yml file.
Contributing
Contributions are welcome! Please submit a pull request with your proposed changes or improvements.


Contact
For any questions or issues, please contact sgaddamp@cougarnet.uh.edu








