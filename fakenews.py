import streamlit as st
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
import base64

def fake_news_predict(user_input):
    Fake_Agent = Agent(
        name='Fake_Agent',
        # model=Groq(id="deepseek-r1-distill-llama-70b")
        model =  OpenAIChat(id="gpt-4o"),
        instructions=[
            "You are a fake news detector.",
            "Always analyze multiple sources before deciding.",
            "Provide sources for transparency.",
            "Respond only with 'FAKE' or 'REAL' followed by a brief explanation.",
        ],
        tools=[DuckDuckGo()],
        markdown=True,
        show_tool_calls=False
    )
    response = Fake_Agent.run(f"Check whether this is real or fake: {user_input}")
    return response

def news_search(user_input):
    web_agent = Agent(
        name="Web_search",
        model=Groq(id="deepseek-r1-distill-llama-70b"),
        tools=[DuckDuckGo()],
        instructions=[
            "You are a real-time news generator that fetches the latest and most relevant information from multiple sources.",
            "Always perform a comprehensive search across various sources before providing an answer.",
            "Include the source URLs in your responses to ensure transparency and credibility.",
            "Continuously collect and update news in real time.",
        ],
        show_tool_calls=False,
        markdown=True,
    )
    response = web_agent.run(f"Generate news based on: {user_input}")
    return response

# Streamlit UI Setup
st.set_page_config(page_title="News Verification", layout="wide")
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    

# Example usage
set_background("background.png") 

def set_sidebar_bg(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    
set_sidebar_bg("back.png")
    




st.sidebar.title("More Options")
option = st.sidebar.radio("Select an option", ["Fake News Detection", "Real News Search"])

if option == "Fake News Detection":
    st.title("Fake News Detection")
    user_input = st.text_input("Enter news text:")
    if st.button("Detect"):
        with st.spinner("Analyzing..."):
            result = fake_news_predict(user_input)
        st.markdown(f"### Result: {result.content}")
   

elif option == "Real News Search":
    st.title("Real News Search")
    user_input = st.text_input("Enter topic:")
    if st.button("Search"):
        with st.spinner("Fetching latest news..."):
            result = news_search(user_input)
        st.markdown(f"### Search Result: {result.content}")
        # st.text_area("News Results:", result, height=300)


