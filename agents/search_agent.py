from langchain.agents import tool
import requests
from bs4 import BeautifulSoup

@tool
def search_company_info(query: str) -> str:
    """使用 360 搜索引擎获取公司信息摘要（国内可用）"""
    search_url = "https://www.so.com/s"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"q": query}

    try:
        res = requests.get(search_url, headers=headers, params=params, timeout=10)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "html.parser")
        results = soup.select(".res-list p")[:3]
        snippets = [r.get_text(strip=True) for r in results if r.get_text(strip=True)]
        return "\n".join(snippets) if snippets else "未找到相关信息。"
    except Exception as e:
        return f"搜索失败：{str(e)}"

