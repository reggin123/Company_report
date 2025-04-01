from langchain.chat_models import ChatOpenAI
import os
from langchain.agents import tool

@tool
def summarize_recent_bids(company: str) -> str:
    """总结公司近期的中标项目信息"""
    llm = ChatOpenAI(
        temperature=0.4,
        model="deepseek-chat",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )
    prompt = f"""
请你搜索并总结 {company} 最近一年内中标的项目情况，包括：

- 项目名称、金额（如果有）
- 所属行业或领域
- 项目地域和类型（如铁路、公路、水利、城市更新等,重点关注数字信息化建设相关的内容）

请用简洁小段落列出，适合写入公司调研报告中“近期中标项目”部分。
"""
    response = llm.invoke(prompt)
    return response.content.strip() if response and hasattr(response, "content") else "暂无中标项目信息"
