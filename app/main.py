from core.config import Config
from core.logger import get_logger

from git_parser.parser import GitParser
from llm.client import LLMClient
from llm.prompts import build_prompt

from db.models import init_db, save_analysis
from stats.stats_engine import get_module_stats, get_risk_stats
import sys

from db.models import query_by_module

from report.markdown_generator import generate
import os
from git import Repo
import json

logger = get_logger()

def safe_parse(text):
    import json

    try:
        return json.loads(text)
    except:
        start = text.find("{")
        end = text.rfind("}") + 1
        return json.loads(text[start:end])
    
def main():

    logger.info("GitInsight started")

    init_db()

    repo_path = r"D:\code\git\Tiny_system_2_PthreadLearning"
    parser = GitParser(repo_path)

    llm = LLMClient(use_mock=True)

    commits = parser.get_commits("HEAD~3")

    results = []

    for c in commits:

        diffs = parser.get_diff(c["hash"])

        diff_text = ""

        for d in diffs:
            diff_text = d.diff.decode("utf-8", errors="ignore")

        diff_text = diff_text[:4000]
        
        prompt = build_prompt(c["message"], diff_text)

        print("DIFF LENGTH:", len(diff_text))

        ai_result = llm.analyze_diff(prompt)

        data = None

        try:
            data = safe_parse(ai_result)
        except:
            print("JSON解析失败:", ai_result)
            data = {
                "module": "Unknown",
                "summary": ai_result[:200],
                "impact": "Unknown",
                "risk": "Low"
            }

        result_item = {
            "commit": c["hash"],
            "module": data.get("module"),
            "summary": data.get("summary"),
            "impact": data.get("impact"),
            "risk": data.get("risk")
        }


    results.append(result_item)
    print("results_items:", results)

    md = generate(results)

    with open("report.md", "w", encoding="utf-8") as f:
        f.write(md)

    print("report.md generated")

    logger.info("Done")


if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "search":

        module = sys.argv[2]

        rows = query_by_module(module)

        print(f"\n{module} 历史分析：\n")

        for r in rows:
            print(f"Commit: {r[0]}")
            print(f"Summary: {r[2]}")
            print(f"Risk: {r[3]}")
            print("---")

    elif len(sys.argv) > 1 and sys.argv[1] == "stats":

        print("\nModule统计：\n")
        module_stats = get_module_stats()
        for m, c in module_stats:
            print(f"{m}: {c}")

        print("\nRisk统计：\n")
        risk_stats = get_risk_stats()
        for r, c in risk_stats:
            print(f"{r}: {c}")

    else:
        main()