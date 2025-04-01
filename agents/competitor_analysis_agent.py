from langchain.agents import tool
from langchain.chat_models import ChatOpenAI
import os

@tool
def analyze_competitors(company: str) -> str:
    """由大模型根据行业背景生成竞争对手分析"""
    llm = ChatOpenAI(
        temperature=0.5,
        model="deepseek-chat",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )

    prompt = f"""
请分析 {company} 所处行业的主要竞争对手，并对比其与对手在地域、资本实力、业务规模或资源优势方面的异同；
要求内容专业、简洁，适合用于公司调研报告。
"""

    res = llm.invoke(prompt)
    return res.content.strip() if res and hasattr(res, "content") else "暂无主要竞争对手数据"
