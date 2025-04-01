from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from agents.search_agent import search_company_info
from agents.finance_agent import analyze_financials
from agents.industry_agent import analyze_industry
from agents.core_business_agent import analyze_core_business
from agents.financial_table_agent import extract_financial_table
from agents.competitor_analysis_agent import analyze_competitors
from agents.trend_prediction_agent import predict_trends
from agents.overall_evaluation_agent import summarize_overall_evaluation
from agents.subsidiary_agent import analyze_subsidiaries
from agents.bid_agent import summarize_recent_bids

import os

def build_report_workflow():
    llm = ChatOpenAI(
        temperature=0,
        model="deepseek-chat",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )
    tools = [
        search_company_info,
        analyze_industry,
        analyze_core_business,
        extract_financial_table,
        analyze_competitors,
        predict_trends,
        analyze_subsidiaries,
        summarize_recent_bids

    ]
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors=True)
    return agent
