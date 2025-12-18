# #cli.py


import typer
from pathlib import Path
from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import profile_csv as basic_profile
from csv_profiler.render import save_json_report, save_markdown_report

app = typer.Typer(help="CSV Profiler CLI")

@app.command()
def profile(
    csv_path: str = typer.Option(..., prompt="Enter the path to your CSV file"),
    out_dir: str = "outputs"
):
    """
    Generate CSV profiling reports.
    """
    csv_path = Path(csv_path)
    out_dir = Path(out_dir)
    report_name = "report"

    if not csv_path.exists():
        typer.echo(f"Error: CSV file {csv_path} does not exist.")
        raise typer.Exit(code=1)

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
    app()

# from pathlib import Path

# from csv_profiler.io import read_csv_rows
# from csv_profiler.profiling import basic_profile
# from csv_profiler.render import save_json_report, save_markdown_report


# def main():
   
#     csv_path = Path(
#         "C:/Users/janah/OneDrive/المستندات/SDAIA/data/saudi_shopping_with_missing.csv"
#     )
   
#     out_dir = Path("outputs")
#     report_name = "report"

    
#     rows = read_csv_rows(csv_path)

    
#     profile = basic_profile(rows)

    
#     json_path = out_dir / f"{report_name}.json"
#     md_path = out_dir / f"{report_name}.md"

#     save_json_report(profile, json_path)
#     save_markdown_report(profile, md_path)

#     print("✔ Reports generated successfully:")
#     print(json_path)
#     print(md_path)


# if __name__ == "__main__":
#     main()




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
