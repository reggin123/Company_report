from langchain.agents import tool
from agents.search_agent import search_company_info
from langchain.chat_models import ChatOpenAI
import os

@tool
def analyze_core_business(company: str) -> str:
    """抓取公司简介并提炼核心业务板块"""
    try:
        summary = search_company_info.run(f"{company} 简介")
    except Exception as e:
        return f"网页搜索失败：{str(e)}"

    llm = ChatOpenAI(
        temperature=0.5,
        model="deepseek-chat",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )

    prompt = f"""
根据以下公司简介内容，提取其核心业务板块和主营收入来源;
同时关注这些部门都主要负责哪些交通线路的运营以及各线路的信息化建设程度。

公司名称：{company}
公司简介：
{summary}

请用简洁、结构化语言输出，适合用在公司调研报告。
"""

    res = llm.invoke(prompt)
    return res.content.strip() if res and hasattr(res, "content") else "暂无核心业务板块数据"

