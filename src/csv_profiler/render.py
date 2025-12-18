# render.py
import json
from pathlib import Path
from typing import Optional


def save_json_report(profile: dict, path: Optional[Path] = None):
    """
    Save profile as JSON file if path is provided,
    otherwise return JSON string (for Streamlit download).
    """
    json_text = json.dumps(profile, indent=2, ensure_ascii=False)

    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json_text, encoding="utf-8")

    return json_text


def save_markdown_report(profile: dict, path: Optional[Path] = None):
    """
    Save profile as Markdown file if path is provided,
    otherwise return Markdown string (for Streamlit download).
    """
    lines = []
    lines.append("# CSV Profiling Report\n")
    lines.append(f"- **Rows:** {profile['n_rows']}")
    lines.append(f"- **Columns:** {profile['n_cols']}\n")

    lines.append("## Missing Values\n")
    lines.append("| Column | Missing |")
    lines.append("|--------|--------:|")

    for col in profile["columns"]:
        lines.append(f"| {col['name']} | {col['missing']} |")

    markdown_text = "\n".join(lines)

    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown_text, encoding="utf-8")

    return markdown_text

