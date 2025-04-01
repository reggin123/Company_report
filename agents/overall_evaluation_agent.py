
from langchain.chat_models import ChatOpenAI
import os


def summarize_overall_evaluation(company: str, context: str) -> str:
    """整合前文全部分析内容，生成专业综合评价（用于报告最后部分）"""
    llm = ChatOpenAI(
        temperature=0.4,
        model="deepseek-chat",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("OPENAI_API_BASE")
    )

    prompt = f"""
你是一位公司研究分析师，请根据以下对 {company} 的调研内容，总结一段综合评价。要求：
- 综合行业、财务、业务、趋势信息
- 语言专业、结构清晰
- 提出发展建议或投资建议

调研内容：
{context}

请输出一段 100-200 字的简明综合评价，用于调研报告最后的综合评价部分。
"""

    response = llm.invoke(prompt)
    return response.content.strip() if response and hasattr(response, "content") else "综合评价生成失败。"

