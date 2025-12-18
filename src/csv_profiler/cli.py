
from pathlib import Path

from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import basic_profile
from csv_profiler.render import save_json_report, save_markdown_report


def main():
   
    csv_path = Path(
        "C:/Users/janah/OneDrive/المستندات/SDAIA/data/saudi_shopping_with_missing.csv"
    )
   
    out_dir = Path("outputs")
    report_name = "report"

    
    rows = read_csv_rows(csv_path)

    
    profile = basic_profile(rows)

    
    json_path = out_dir / f"{report_name}.json"
    md_path = out_dir / f"{report_name}.md"

    save_json_report(profile, json_path)
    save_markdown_report(profile, md_path)

    print("✔ Reports generated successfully:")
    print(json_path)
    print(md_path)


if __name__ == "__main__":
    main()




# def main():
#     print("C:\\Users\\janah\\OneDrive\\المستندات\\SDAIA\\data\\saudi_shopping_with_missing.csv")
    
# if __name__ == "__main__":
#     main()

# import typer

# app = typer.Typer()

# @app.command()
# def hello(name: str):
#     print(f"Hello {name}")

# if __name__ == "__main__":
#     app()
