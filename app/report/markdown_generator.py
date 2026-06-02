def generate(report_items):
    md = "# GitInsight Report\n\n"

    for item in report_items:
        summary = item["summary"].replace("\\n", "\n")
        md += f"""
    
    ## {item['module']}

    Commit: {item['commit']}

    Summary: {item['summary']}

    Risk: {item['risk']}

    ---
    """
    return md