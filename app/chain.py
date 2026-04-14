from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from app.schemas import ResumeAnalysis
import os

load_dotenv()

def create_chain():
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY")
    )
    parser = JsonOutputParser(pydantic_object=ResumeAnalysis)
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert HR consultant and ATS specialist.
        Analyze the resume against the job description.
        Return ONLY valid JSON — no extra text."""),
        ("human", """
        Job Description:
        {job_description}

        Resume:
        {resume}

        {format_instructions}
        """)
    ]).partial(format_instructions=parser.get_format_instructions())
    chain = prompt | llm | parser
    return chain