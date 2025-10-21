import os
import time
import pandas as pd
from typing import List, Dict

from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

import streamlit as st


os.environ["OPENAI_API_KEY"] = "......"


llm = ChatOpenAI(model="gpt-4o-mini", max_tokens=1000, temperature=0.7)


class Agent:
    def __init__(self, name: str, role: str, skills: List[str]):
        self.name = name
        self.role = role
        self.skills = skills
        self.llm = llm

    def process(self, task: str, context: List[Dict] = None) -> str:
        messages = [
            SystemMessage(content=f"You are {self.name}, a {self.role}. Your skills include: {', '.join(self.skills)}. Respond to the task based on your role and skills.")
        ]
        
        if context:
            for msg in context:
                if msg['role'] == 'human':
                    messages.append(HumanMessage(content=msg['content']))
                elif msg['role'] == 'ai':
                    messages.append(AIMessage(content=msg['content']))
        
        messages.append(HumanMessage(content=task))
        response = self.llm.invoke(messages)
        return response.content


class HistoryResearchAgent(Agent):
    def __init__(self):
        super().__init__("Clio", "History Research Specialist", ["deep knowledge of historical events", "understanding of historical contexts", "identifying historical trends"])

class DataAnalysisAgent(Agent):
    def __init__(self):
        super().__init__("Data", "Data Analysis Expert", ["interpreting numerical data", "statistical analysis", "data visualization description"])

    # Grafik kısmını kaldırdık, sadece tablo özet
    def analyze_dataframe(self, df: pd.DataFrame, context: List[Dict] = None) -> pd.DataFrame:
        summary = df.describe().transpose()
        summary['Percentage_of_Max'] = (summary['mean'] / summary['max'] * 100).round(2)
        if context:
            context.append({"role": "ai", "content": f"Data Agent: Statistical summary table created."})
        return summary


def research_historical_context(history_agent, task: str, context: list) -> list:
    history_task = f"Provide relevant historical context and information for the following task: {task}"
    result = history_agent.process(history_task)
    context.append({"role": "ai", "content": f"History Agent: {result}"})
    return context

def identify_data_needs(data_agent, task: str, context: list) -> list:
    historical_context = context[-1]["content"]
    data_need_task = f"Based on the historical context, what specific data or statistical information would be helpful? Context: {historical_context}"
    result = data_agent.process(data_need_task, context)
    context.append({"role": "ai", "content": f"Data Agent: {result}"})
    return context

def provide_historical_data(history_agent, task: str, context: list) -> pd.DataFrame:
    data = {
        "Year": [1789, 1790, 1791, 1792, 1793],
        "Event_Impact_Score": [7, 5, 6, 8, 9]
    }
    df = pd.DataFrame(data)
    context.append({"role": "ai", "content": f"History Agent: Historical data provided."})
    return df

def analyze_data(data_agent, df: pd.DataFrame, context: list) -> list:
    summary_df = data_agent.analyze_dataframe(df, context)
    return context, summary_df

def synthesize_final_answer(history_agent, task: str, context: list) -> str:
    synthesis_task = "Based on all the historical context, data, and analysis, provide a comprehensive answer."
    final_result = history_agent.process(synthesis_task, context)
    return final_result

st.title("Multi-Agent History & Data Analysis System")

task_input = st.text_input("Enter a historical task/question:", "Explain the causes and consequences of the French Revolution.")

if st.button("Run Analysis"):

    
    history_agent = HistoryResearchAgent()
    data_agent = DataAnalysisAgent()

    context = []
    st.info("🏛️ Researching historical context...")
    context = research_historical_context(history_agent, task_input, context)
    st.write(context[-1]["content"])

    st.info("📊 Identifying data needs...")
    context = identify_data_needs(data_agent, task_input, context)
    st.write(context[-1]["content"])

    st.info("🏛️ Providing historical data...")
    df = provide_historical_data(history_agent, task_input, context)
    st.dataframe(df)

    st.info("📈 Analyzing data...")
    context, summary_df = analyze_data(data_agent, df, context)
    st.dataframe(summary_df)
    st.write(context[-1]["content"])

    st.info("🏛️ Synthesizing final answer...")
    final_answer = synthesize_final_answer(history_agent, task_input, context)
    st.success(final_answer)
