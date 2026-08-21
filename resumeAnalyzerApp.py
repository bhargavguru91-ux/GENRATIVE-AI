import streamlit as st
from utils import extract_pdf , create_vector_text
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

st.set_page_config(page_title="Resume Analyzer")
st.title("Resume Analyzer AI")

resume_file = st.file_uploader("Uplaod resume (PDF)" , type=["pdf"])
jd_text = st.text_area("Paste Job Description")

if st.button("Resume Analysis"):
    if resume_file and jd_text:
        # Extract resume 
        resume_text = extract_pdf(resume_file)

        # combine resume + job description 
        combine_text = resume_text +"\n\n"+ jd_text

        # create vector store
        vector_store = create_vector_text(combine_text)

        # retriver
        retriver = vector_store.as_retriever()

        llm = Ollama(model="gemma2:2b")

        prompt = ChatPromptTemplate.from_template(
            """
            You are an AI placement coach for help4code.
            Context:
            {context}

            Question:
            {question}

            provide:
            1. Skills gap analysis
            2. Missing technologies
            3. ATS Score (0-100)
            4. Technical Interview Question
            5. Resume Improvement Suggestions
            6. 30-90 day skill upskilling roadmap
            7. Overall fit summary for the role

            Keep the response clear, professional, and actionable.
            """)

        chain = (
            {
                "context": retriver ,
                "question": RunnablePassthrough()
            }
            | prompt | llm | StrOutputParser()
        )

        response = chain.invoke("Analyze resume against job description")

        st.subheader("Analysis Result")
        st.write(response)
    else:
        st.warning("Please Upload resume and Job description")