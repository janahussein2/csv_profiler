
# profiling.py

MISSING_VALUES = {"", "na", "n/a", "null", "none", "nan"}

def is_missing(value):
    if value is None:
        return True
    return str(value).strip().casefold() in MISSING_VALUES

def try_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def infer_type(values):
    usable = [v for v in values if not is_missing(v)]
    if not usable:
        return "text"
    for v in usable:
        if try_float(v) is None:
            return "text"
    return "number"

def numeric_stats(values):
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)
    nums = [try_float(v) for v in usable if try_float(v) is not None]
    count = len(nums)
    return {
        "count": count,
        "missing": missing,
        "unique": len(set(nums)),
        "min": min(nums) if nums else None,
        "max": max(nums) if nums else None,
        "mean": sum(nums)/count if count else None
    }

def text_stats(values, top_k=3):
    usable = [v for v in values if not is_missing(v)]
    missing = len(values) - len(usable)
    counts = {}
    for v in usable:
        counts[v] = counts.get(v, 0) + 1
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    top = [{"value": v, "count": c} for v, c in sorted_items[:top_k]]
    return {
        "count": len(usable),
        "missing": missing,
        "unique": len(counts),
        "top": top
    }

def profile_csv(rows):
    if not rows:
        return {"n_rows": 0, "n_cols": 0, "columns": []}

    columns = list(rows[0].keys())
    col_profiles = []

    for col in columns:
        values = [row.get(col, "") for row in rows]
        col_type = infer_type(values)
        if col_type == "number":
            stats = numeric_stats(values)
        else:
            stats = text_stats(values)
        col_profiles.append({"name": col, "type": col_type, **stats})

    return {
        "n_rows": len(rows),
        "n_cols": len(columns),
        "columns": col_profiles
    }


# def count_missing(rows):
#     if not rows:
#         return {}

#     columns = list(rows[0].keys())
#     missing = {col: 0 for col in columns}

#     for row in rows:
#         for col in columns:
#             if row.get(col, "").strip() == "":
#                 missing[col] += 1

#     return missing


# def basic_profile(rows):
#     if not rows:
#         return {
#             "n_rows": 0,
#             "n_cols": 0,
#             "columns": [],
#             "missing": {}
#         }

#     columns = list(rows[0].keys())

#     return {
#         "n_rows": len(rows),
#         "n_cols": len(columns),
#         "columns": columns,
#         "missing": count_missing(rows)
#     }


# # Test
# profile = basic_profile(rows)
# print("Profile:")
# for key, value in profile.items():
#     print(f"  {key}: {value}")


# def basic_profile(rows):
#     """
#     Create a basic profile of CSV rows.

#     Args:
#         rows: List of dicts (from csv.DictReader)

#     Returns:
#         Dict with:
#         - "n_rows": number of rows
#         - "n_cols": number of columns
#         - "columns": list of column names
#         - "missing": dict of column -> missing count
#     """

#     # Handle empty data
#     if not rows:
#         return {
#             "n_rows": 0,
#             "n_cols": 0,
#             "columns": [],
#             "missing": {}
#         }

#     # Get column names from first row
#     columns = list(rows[0].keys())

#     return {
#         "n_rows": len(rows),
#         "n_cols": len(columns),
#         "columns": columns,
#         "missing": count_missing(rows)
#     }


# # Test with our CSV data
# profile = basic_profile(rows)
# print("Profile:")
# for key, value in profile.items():
#     print(f"  {key}: {value}")