import streamlit as st
import PyPDF2
from gen_ai import init_model_paper_wise, init_model_white_paper

# Function to extract text from a PDF file
def get_pdf_text(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def generate_default_prompt():
    default_prompt = """1. Paper Title: [Title of the paper]
2. Executive Summary: A concise overview of the paper's main arguments and findings related to [Insert Topic].
3. Key Insights and Contributions: Summarize the paper’s significant contributions to the understanding of [Insert Topic], including any novel perspectives or data presented.
4. Implications for the Field: Discuss how the findings of the paper impact the broader discussion or application of [Insert Topic] in relevant fields.
5. Challenges and Limitations: Outline any challenges or limitations highlighted in the paper regarding [Insert Topic], including gaps in the research or areas for future exploration.
6. Practical Applications: Detail any recommendations or strategies provided for applying the paper’s findings to real-world scenarios involving [Insert Topic].
7. Overall Conclusions: Summarize the key conclusions and implications of the paper in the context of [Insert Topic].
"""
    return default_prompt

# Function to initialize the model
def initialize_model():
    if 'model' not in st.session_state:
        st.session_state['model'] = init_model_paper_wise()

# Main function to control the app layout and navigation
def main():
    st.title("PDF Summarizer with Google Gen AI")
    
    # Sidebar for navigation
    menu = ["Upload PDFs", "Generate Paper-Wise Summary", "Generate White Paper Summary"]
    choice = st.sidebar.selectbox("Select an Option", menu)
    
    if choice == "Upload PDFs":
        upload_pdfs()
    elif choice == "Generate Paper-Wise Summary":
        generate_paper_wise_summary()
    elif choice == "Generate White Paper Summary":
        generate_white_paper_summary()

# Function to upload PDFs
def upload_pdfs():
    st.header("Upload PDF Files")
    uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type='pdf')
    topic = st.text_input("What are these papers about?")
    
    if st.button("Submit"):
        if uploaded_files:
            raw_texts = []
            pdf_texts = {}
            for f in uploaded_files:
                file_name = f.name 
                raw_text = get_pdf_text(f)
                pdf_texts[file_name] = raw_text
                raw_texts.append(raw_text)
            
            # Store in session state
            st.session_state['raw_texts'] = raw_texts
            st.session_state['pdf_texts'] = pdf_texts
            st.session_state['topic'] = topic
            st.write("Files uploaded successfully.")
            st.write(f"Topic: {topic}")
        else:
            st.warning("Please upload at least one PDF file.")


def generate_paper_wise_summary():
    st.header("Generate Paper-Wise Summary")
    
    if 'raw_texts' in st.session_state:
        st.subheader("Modify the sections in the summary for each paper as needed.")
        
        if "user_prompt" not in st.session_state:
            st.session_state.user_prompt = generate_default_prompt()
        
        user_input = st.text_area(
            "Literature Review Prompt",
            value=st.session_state.user_prompt,
            height=300
        )
        
        if st.button("Submit Sections"):
            st.session_state.user_prompt = user_input
            st.write("Prompt submitted successfully!")
            st.write("User's submitted text:")
            st.write(st.session_state.user_prompt)

            # Initialize progress bar
            with st.spinner('Generating paper-wise summaries...'):
                progress_bar = st.progress(0)
                # Generate the docx binary stream
                doc_stream = init_model_paper_wise(st.session_state.topic, st.session_state.user_prompt, st.session_state.raw_texts)
                
                # Update progress bar
                progress_bar.progress(100)
                
                # Provide download link for the .docx file
                st.download_button(
                    label="Download Paper-Wise Summary",
                    data=doc_stream,
                    file_name="paper_wise_summary.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
        else:
            st.warning("Please upload PDFs first.")
    else:
        st.warning("Please upload PDFs first.")

def generate_white_paper_summary():
    st.header("Generate White Paper Summary")
    
    if 'raw_texts' in st.session_state:
        
        user_input = st.text_area(
            "Literature Review Prompt",
            value='''
            Abstract
            Introduction
            Excecutive summary
            Methodologies
            Implementation Ideas
            Implications
            Beniftts
            Limitations
            ethical considerations and theoritical framework
            Conclusion''',
            height=300
        )
        
        if st.button("Submit Sections"):
            user_input_list = [line.strip() for line in user_input.split('\n') if line.strip()]
            st.session_state.white_user_prompt = user_input_list
            st.write("Prompt submitted successfully!")

            # Initialize progress bar
            with st.spinner('Generating white paper summary...'):
                progress_bar = st.progress(0)
                # Generate the docx binary stream
                doc_stream = init_model_white_paper(st.session_state.topic, st.session_state.white_user_prompt, st.session_state.pdf_texts)
                
                # Update progress bar
                progress_bar.progress(100)
                
                # Provide download link for the .docx file
                st.download_button(
                    label="Download White Paper Summary",
                    data=doc_stream,
                    file_name="white_paper_summary.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
        else:
            st.warning("Please upload PDFs first.")
    else:
        st.warning("Please upload PDFs first.")

# Run the app
if __name__ == "__main__":
    main()
