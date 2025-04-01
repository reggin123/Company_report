from langchain.agents import tool
from langchain.chat_models import ChatOpenAI
import os

@tool
def analyze_industry(company: str) -> str:
    """根据公司所属行业，生成深入的行业背景与前景分析"""

    llm = ChatOpenAI(
        temperature=0.4,
        model="deepseek-chat",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )

    prompt = f"""
你是一名行业分析专家，请针对公司「{company}」所处的行业进行全面分析，输出调研报告中的“行业背景与前景”部分内容，内容包括但不限于：

1. 行业基本概况（产业链、市场规模、发展阶段）
2. 政策环境与市场趋势（国家支持、发展方向、下游需求）
3. 竞争格局（主要参与者、集中度、竞争策略）
4. 技术变革与未来发展趋势（数字化、智能化、绿色发展等）
5. 该行业对 {company} 的影响与机会（有利/挑战、重点切入点）

特别关注第四点，分析该行业的数字智能化发展

请用结构清晰、专业语言进行书写，适合用于公司调研报告正文。
"""

    res = llm.invoke(prompt)
    return res.content.strip() if res and hasattr(res, "content") else "暂无行业分析数据"
