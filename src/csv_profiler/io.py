# def read_csv_rows(path: str | Path) -> list[dict[str, str]]:
#     path = Path(path)
#     with path.open("r", encoding="utf-8", newline="") as f:
#         reader = DictReader(f)
#         return [dict(row) for row in reader]

from pathlib import Path
from csv import DictReader
from typing import Union

def read_csv_rows(path: Union[str, Path]) -> list[dict[str, str]]:
    path = Path(path)
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = DictReader(f)
        return [dict(row) for row in reader]
