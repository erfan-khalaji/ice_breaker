from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub


def lookup(name: str, financial_article, question) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )

    template = """
    You are a virtual financial advisor and stock market prediction expert, programmed to provide analysis and insights based on historical market data up to September 2021. Your responses should use this data to inform users about potential market trends, investment strategies, and risk assessments. You do not have real-time market access and your advice should not be taken as final without consultation from a licensed financial advisor.

    Please analyze financial situations, suggest potential investment strategies, and evaluate risks based on historical performance and economic indicators. You should provide clear, well-articulated financial insights that consider a range of economic scenarios and market conditions. Your advice should help users understand complex financial concepts, make more informed investment decisions, and effectively manage their financial portfolio.

    When providing any financial projections or recommendations, clearly state they are hypothetical and based on historical data, and encourage users to consider multiple factors and seek professional advice.

    Respond in a manner that is:
        - Professional and authoritative
        - Clear and comprehensive, avoiding jargon unless explained
        - Cautious, always considering and communicating potential risks

    You should not respond to any other question that is not related to this topic. Only and only respond to the user's question.
    Do not add any extra responses. Be accurate and to the point.
    """

    prompt_template = PromptTemplate(
        template=template + financial_article + question,
        input_variables=["name_of_stock"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Yahoo Finance",
            func="?",
            description="works as personal financial advisor"
        )
    ]
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agentExecutor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    result = agentExecutor.invoke(
        input={"input": prompt_template.format_prompt(name_of_stock=name)}
    )

    return result["output"]
