from langchain.chat_models import ChatOpenAI
import os
from langchain.agents import tool

@tool
def analyze_subsidiaries(company: str) -> str:
    """总结公司下属企业的结构和主要子公司"""
    llm = ChatOpenAI(
        temperature=0.4,
        model="deepseek-chat",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )
    prompt = f"""
请你总结 {company} 的下属企业情况。包括但不限于：

- 子公司、分公司、控股单位有哪些？
- 哪些属于主营业务或区域布局的关键单位？
- 有哪些最新的架构或组织变动？
- 重点了解哪个部门负责信息化建设

请用清晰的结构和简洁语言组织内容，适合写入公司调研报告。
"""
    response = llm.invoke(prompt)
    return response.content.strip() if response and hasattr(response, "content") else "暂无下属企业信息"
