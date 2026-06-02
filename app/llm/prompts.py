def build_prompt(commit, diff_text):

    return f"""
你是一名资深嵌入式RTOS开发工程师，负责生成变更的代码的周报，向老板汇报，必须专业可靠。

========================
⚠️ 输出要求（非常重要）
========================
1. 只能输出 JSON（禁止 markdown / 禁止解释）
2. 必须是合法 JSON（双引号，不能换行破坏结构）
3. 所有字段必须存在
4. summary 必须是“单个字符串”，使用 \\n 分段
5. 不允许使用数组、不允许嵌套对象
6. summary内容详细，不要有模糊语义

========================
输出格式如下（严格遵守）：
========================

{{
    "module": "RTOS子系统（task/scheduler/memory/ipc/driver）",

    "summary": "一段完整技术分析，用\\n分隔段落，格式对齐：
                - 修改内容
                - 变更点对整体功能的作用
                - 对RTOS调度/中断/资源影响",

    "impact": "scheduler / kernel / driver / interrupt / power",

    "risk": "Low | Medium | High"
}}

========================
分析任务
========================

Commit:
{commit}

Diff:
{diff_text}

========================
强制规则（必须遵守）
========================
- 不允许使用 ``` 或者 三引号
- 不允许输出任何非 JSON 内容
- 不允许数组（[]）或对象嵌套
- summary 必须是 string（不是 list）
- 必须保证 JSON 可被 json.loads 解析
"""