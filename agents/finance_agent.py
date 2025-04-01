from langchain.chat_models import ChatOpenAI
from langchain.agents import tool
import random
import os


def analyze_financials(company: str, financial_table: str) -> str:
    """根据结构化财务表格内容，生成专业财务分析总结"""
    llm = ChatOpenAI(
        temperature=0.3,
        model="deepseek-chat",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )

    prompt = f"""
你是一位企业财务分析专家，请根据 {company} 的以下财务表格数据内容进行专业分析：

{financial_table}

请你结合上表内容，从以下角度输出完整分析：
1. 收入、利润等增长情况
2. 盈利能力与成本控制（如毛利率、净利润率）
3. 偿债能力（如资产负债率、流动性）
4. 现金流状况与经营健康度
5. 是否存在风险或亮点

输出应条理清晰、专业、结构紧凑，适合调研报告正文部分，同时这五个大点每一点不要用中文汉字的数字作为标号。
"""

    res = llm.invoke(prompt)
    return res.content.strip() if res and hasattr(res, "content") else "财务分析生成失败"
