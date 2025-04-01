import os
import sys
import threading

from dotenv import load_dotenv






import streamlit as st
from workflows.report_workflow import build_report_workflow
from agents.report_writer import write_report
from dotenv import load_dotenv
from utils.docx_exporter import save_report_to_word
from agents.overall_evaluation_agent import summarize_overall_evaluation
from agents.finance_agent import analyze_financials
from agents.financial_table_agent import extract_financial_table



load_dotenv()

st.set_page_config(page_title="公司调研报告生成器", layout="centered")
st.title("📊 公司调研报告生成器")

company = st.text_input("请输入公司名称", value="")

if st.button("生成调研报告"):
    with st.spinner("正在生成报告，请稍候..."):
        agent = build_report_workflow()

        # ✅ Step 1：调用各模块工具
        summary = agent.invoke({"input": f"{company} 的公司简介"}).get("output", "")
        industry = agent.invoke({"input": f"{company} 的行业背景"}).get("output", "")
        core = agent.invoke({"input": f"{company} 的核心业务板块"}).get("output", "")
        table = extract_financial_table(company)  # ✅ 替代 agent.invoke 获取表格
        finance = analyze_financials(company, table)  # ✅ 替代 agent.invoke 生成分析
        competitors = agent.invoke({"input": f"{company} 的竞争对手情况"}).get("output", "")
        bid=agent.invoke({"input": f"{company} 的近期招投标项目"}).get("output", "")
        subsidiary=agent.invoke({"input": f"{company} 的下属企业"}).get("output", "")
        trends = agent.invoke({"input": f"{company} 的发展趋势"}).get("output", "")

        # ✅ Step 2：构建 context，传给综合评价 agent
        context = f"""
公司简介：
{summary}

行业背景：
{industry}

核心业务：
{core}

关键财务指标：
{table}

财务分析：
{finance}

竞争对手分析：
{competitors}

近期招投标信息
{bid}

下属企业情况
{subsidiary}

发展趋势预测：
{trends}
"""

        # ✅ Step 3：调用 summarize_overall_evaluation 工具
        # ✅ 直接调用函数（不走 Agent 工具机制）
        overall = summarize_overall_evaluation(company, context)

        # ✅ Step 4：写入报告
        report = write_report(company, industry, summary, core, table,finance, competitors,bid,subsidiary, trends, overall)

        # ✅ 保存为 Markdown + Word
        md_path = f"{company}_report.md"
        docx_path = f"{company}_report.docx"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(report)
        save_report_to_word(report, docx_path)

    st.success("✅ 报告生成完成！")

    with open(md_path, "r", encoding="utf-8") as f:
        st.markdown(f"### 📄 报告预览\n\n```markdown\n{f.read()[:1000]}...\n```")

    with open(docx_path, "rb") as f:
        st.download_button("📥 下载 Word 报告", f, file_name=docx_path)
