from langchain.agents import tool
from langchain.chat_models import ChatOpenAI
import os

@tool
def predict_trends(company: str) -> str:
    """基于公司行业与政策方向，预测未来发展趋势"""
    llm = ChatOpenAI(
        temperature=0.6,
        model="deepseek-chat",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )

    prompt = f"""
请根据你对 {company} 所处行业的发展趋势、政策导向、技术创新等方面的理解，对该公司未来3-5年的发展方向、潜在机遇与挑战进行预测分析；
同时重点分析该公司是否在数字化建设方向有发展趋势
要求内容逻辑清晰、结构完整，适合用于调研报告。
"""

    res = llm.invoke(prompt)
    return res.content.strip() if res and hasattr(res, "content") else "暂无未来发展趋势数据"
