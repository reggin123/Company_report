from langchain.agents import tool
from agents.search_agent import search_company_info
from langchain.chat_models import ChatOpenAI
import os

@tool
def extract_financial_table(company: str) -> str:
    """抓取公司公开信息，生成关键财务指标表格（模拟或总结）"""
    try:
        search_text = search_company_info.run(f"{company} 财务数据")
    except Exception as e:
        return f"搜索失败：{str(e)}"

    llm = ChatOpenAI(
        temperature=0.4,
        model="deepseek-chat",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )

    prompt = f"""
请你提取 {company} 最近一年的关键财务数据，以Markdown表格形式输出，包括以下字段（如有）：
- 营业收入（亿元）
- 净利润（亿元）
- 总资产（亿元）
- 净资产（亿元）
- 资产负债率（%）
- ROE（%）
- 经营活动现金流（亿元）

如果数据不全，请根据公开信息合理补充估算。

原始财务相关内容：
{search_text}

"""

    res = llm.invoke(prompt)
    return res.content.strip() if res and hasattr(res, "content") else "暂无财务数据"
