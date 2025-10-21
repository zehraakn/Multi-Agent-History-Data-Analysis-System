# Multi-Agent-History-Data-Analysis-System


## System Purpose:
This system is designed to provide comprehensive, data-driven, and analytical answers to users’ historical questions. It goes beyond simply summarizing events, evaluating economic, social, and political contexts, and supports answers with data analysis and statistics when necessary.System Purpose:
This system is designed to provide comprehensive, data-driven, and analytical answers to users’ historical questions. It goes beyond simply summarizing events, evaluating economic, social, and political contexts, and supports answers with data analysis and statistics when necessary.

<img width="1024" height="1536" alt="Veri ve Tarih Analiz Akış Şeması" src="https://github.com/user-attachments/assets/f06f3121-a62c-4769-bead-289fe78d3d5f" />


## System Components & Workflow:

### 1.History Agent:

-Receives the user’s question.
-Researches the historical background, causes, and consequences of the event.

-Summarizes and explains in a clear and detailed manner.

-Example: Explains the reasons, historical context, and economic/political impacts of the Ankara Agreement.

### 2.Data Agent:

-Identifies relevant data to illustrate the impact of the historical event.

-Collects and analyzes economic indicators (GDP, inflation, unemployment), trade volume, FDI, social and demographic data.

-Provides analysis with tables, graphs, and visualization suggestions.

-Example: Analyzes Turkey’s GDP and trade changes after the Ankara Agreement.

### 3.Synthesis & Answer Generation:

-Combines outputs from History Agent and Data Agent.

-Produces a comprehensive, analytical, and data-supported response.

-Offers a detailed summary from short-term effects to long-term consequences.

### Key Features of System Responses:

Detailed & explanatory: Provides causes and effects along with historical and economic context.

Data-supported: Includes statistics, economic indicators, and visualization recommendations.

Analytical & holistic: Evaluates social, cultural, political, and economic impacts together.

Long-term perspective: Explains effects of the event up to the present.

User-friendly: Delivers history, data, and analysis in a single answer.

### Summary:
This is a multi-agent research and analysis system that answers historical questions, performs data-driven analysis, and produces comprehensive responses. With a single question, users receive a holistic analysis covering both historical context and relevant economic and social data.

#### The main libraries and tools I used in the system are as follows:

LangChain: I used it to manage multi-agent interactions and direct tasks using natural language processing. Specifically, I integrated LLM (Large Language Model) with ChatOpenAI and managed message flow using HumanMessage, AIMessage, and SystemMessage classes.

Pandas: I used it to process, summarize, and analyze historical data in tabular form.

Streamlit: I used it to create the user interface and make the system interactive, allowing the user to input tasks and visualize results.

OS and Typing: I used them to manage environment variables and ensure type safety in the code.
