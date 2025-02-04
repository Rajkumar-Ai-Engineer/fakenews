import streamlit as st
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq

def fake_news_predict(user_input):
    Fake_Agent = Agent(
        name='Fake_Agent',
        model=Groq(id="deepseek-r1-distill-llama-70b"),
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
st.markdown("""
    <style>
        .stApp {
            background-image: url('https://www.bing.com/images/search?view=detailV2&ccid=xoyACR5J&id=08C2ED5688D0F5516DFD13C4F7127B714F9C0A6A&thid=OIP.xoyACR5JwHTCsaKpW8JeUgHaEJ&mediaurl=https%3A%2F%2Fimg.freepik.com%2Fpremium-photo%2Fhigh-quality-desktop-wallpaper_941097-71081.jpg&exph=351&expw=626&q=neon+spreading+4k+wallpapers+for+pc&simid=607995747528606835&form=IRPRST&ck=988E1085529E355A7C7D0862170A8424&selectedindex=8&itb=0&cw=1334&ch=708&ajaxhist=0&ajaxserp=0&cit=ccid_%2BKbMWVXp*cp_FA28F4201124450B53730581EEB0F993*mid_494C9473CD727A31B81F6543F15C7B405611BB07*simid_607988763924779735*thid_OIP.-KbMWVXpXorogwXmf8KRPwHaEo&vt=2&sim=11'); 
            background-size: cover;
        }
    </style>
    
    
""", unsafe_allow_html=True)



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


