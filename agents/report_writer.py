def write_report(company: str,
                 industry_info: str,
                 search_summary: str,
                 core_business: str,
                 financial_table: str,
                 finance_info: str,
                 competitor_analysis: str,
                 recent_bids:str,
                 subsidiaries:str,
                 trend_prediction: str,
                 overall_evaluation: str) -> str:

    return f"""# {company} 调研报告

一、公司简介
{search_summary}

二、行业背景与前景
{industry_info}

三、核心业务板块
{core_business}

四、关键财务指标
{financial_table}

五、财务状况分析
{finance_info}

六、行业竞争格局
{competitor_analysis}

七、近期招投标信息
{recent_bids}

八、下属企业情况
{subsidiaries}

九、发展前景与趋势预测
{trend_prediction}

十、综合评价   
{overall_evaluation}
"""
