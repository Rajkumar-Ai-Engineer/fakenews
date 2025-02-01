from phi.agent import Agent 
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.openai import OpenAIChat
from phi.model.groq import Groq
import streamlit as st
from rich.prompt import Prompt
import typer 

class MyAgent:
    
    def fake_news_predict(self, user: str):
        Fake_Agent = Agent(
            name='Fake_Agent',
            # model=OpenAIChat(id="gpt-4o"),
            model = Groq(id="deepseek-r1-distill-llama-70b"),


            instructions=[
                "You are a fake news detector.",
                "Always analyze multiple sources before deciding.",
                "Provide sources for transparency.",
                "Respond only with 'FAKE' or 'REAL'.",
            ],
            tools=[DuckDuckGo()],
            markdown=True,
            show_tool_calls=False
        )
        
        while True:
            user_input = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            
            if user_input in ('exit', 'quit'):
                break
            
            Fake_Agent.print_response(f"Check if this news is real or fake: {user_input}")
            
    def news_search(self,category,user):
        
        web_agent = Agent(
            name="Web_search",
            # model = OpenAIChat(id='gpt-4o'),
            model = Groq(id="deepseek-r1-distill-llama-70b"),
            tools= [DuckDuckGo()],
            instructions=[
            "You are a real-time news generator that fetches the latest and most relevant information from multiple sources.",
            "Always perform a comprehensive search across various sources before providing an answer.",
            "Include the source URLs in your responses to ensure transparency and credibility.",
            "If the user requests news based on a specific timestamp, retrieve and return the most accurate and relevant information from that period.",
            "Continuously collect and update news in real time. For example, when asked for today's news, provide the latest available information.",
            "Ensure that all news is fact-based and avoid speculation or unverified information."
            ],

            show_tool_calls=False,
            markdown=True,
            )
        
        
        while True:
                user_input = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
            
                if user_input in ('exit', 'quit'):
                    break
            
                web_agent.print_response(f"Generate the real time news : {user_input}")
            
        
if __name__ == "__main__":
    typer.run(MyAgent().news_search(user="Raj Kumar",category=None))
