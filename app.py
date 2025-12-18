# app.py
import streamlit as st
import csv
from io import StringIO
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src" / "csv_profiler"))

try:
    from profiling import profile_csv
except ModuleNotFoundError:
    st.error("profiling.py not found inside src/csv_profiler!")

try:
    from render import save_json_report, save_markdown_report
except ModuleNotFoundError:
    st.warning("render.py not found! Download buttons will not work.")

st.set_page_config(page_title="CSV Profiler", layout="wide")
st.title("CSV Profiler")
st.caption("Upload CSV → Profile → Export")

uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded:
    text = uploaded.getvalue().decode("utf-8")
    rows = list(csv.DictReader(StringIO(text)))

    st.write(f"File uploaded: **{uploaded.name}**")
    st.dataframe(rows)

    if st.button("Generate Profile"):
        profile = profile_csv(rows)
        st.session_state["profile"] = profile
        st.success("Profile generated!")

if "profile" in st.session_state:
    profile = st.session_state["profile"]

    st.subheader("Summary")
    st.write(f"Rows: {profile['n_rows']}")
    st.write(f"Columns: {profile['n_cols']}")

    st.subheader("Columns")
    for col in profile["columns"]:
        st.markdown(f"**{col['name']}** ({col['type']})")

        st.write(
            f"Count: {col['count']}, "
            f"Missing: {col['missing']}, "
            f"Unique: {col['unique']}"
        )

        if col["type"] == "number":
            st.write(
                f"Min: {col['min']}, "
                f"Max: {col['max']}, "
                f"Mean: {col['mean']}"
            )
        else:
            st.write("Top values:")
            for t in col["top"]:
                st.write(f"- {t['value']} ({t['count']})")

    
    json_data = save_json_report(profile)
    st.download_button(
        "Download JSON",
        data=json_data,
        file_name="profile.json",
        mime="application/json"
    )

    
    markdown_data = save_markdown_report(profile)
    st.download_button(
        "Download Markdown",
        data=markdown_data,
        file_name="profile.md",
        mime="text/markdown"
    )





# # app.py
# import streamlit as st
# import csv
# from io import StringIO
# import json
# import sys
# from pathlib import Path

# # إضافة مجلد src لمسار بايثون
# sys.path.append(str(Path(__file__).parent / "src" / "csv_profiler"))

# # استدعاء دوال البروفايل من ملفاتك داخل src
# try:
#     from profiling import profile_csv
# except ModuleNotFoundError:
#     st.error("profiling.py not found inside src folder!")

# try:
#     from render import save_json, save_markdown
# except ModuleNotFoundError:
#     st.warning("render.py not found inside src folder! Download buttons will not work.")

# # إعداد الصفحة
# st.set_page_config(page_title="CSV Profiler", layout="wide")
# st.title("CSV Profiler")
# st.caption("Upload CSV → Profile → Export")

# # رفع ملف CSV
# uploaded = st.file_uploader("Upload CSV", type=["csv"])

# if uploaded:
#     # قراءة الملف
#     text = uploaded.getvalue().decode("utf-8")
#     rows = list(csv.DictReader(StringIO(text)))

#     st.write(f"File uploaded: **{uploaded.name}**")
#     st.dataframe(rows)  # عرض البيانات في جدول

#     # زر توليد التقرير
#     if st.button("Generate Profile"):
#         profile = profile_csv(rows)
#         st.session_state["profile"] = profile
#         st.success("Profile generated!")

# # عرض التقرير إذا موجود
# if "profile" in st.session_state:
#     profile = st.session_state["profile"]

#     # عرض ملخص عام
#     st.subheader("Summary")
#     st.write(f"Rows: {profile['n_rows']}")
#     st.write(f"Columns: {profile['n_cols']}")

#     # عرض تفاصيل الأعمدة
#     st.subheader("Columns")
#     for col in profile["columns"]:
#         st.markdown(f"**{col['name']}** ({col['type']})")
#         if col["type"] == "number":
#             st.write(f"Count: {col['count']}, Missing: {col['missing']}, Unique: {col['unique']}")
#             st.write(f"Min: {col['min']}, Max: {col['max']}, Mean: {col['mean']}")
#         else:
#             st.write(f"Count: {col['count']}, Missing: {col['missing']}, Unique: {col['unique']}")
#             st.write("Top values:")
#             for t in col["top"]:
#                 st.write(f"  {t['value']} ({t['count']})")

#     # زر تنزيل JSON
#     if 'save_json' in globals():
#         json_data = json.dumps(profile, indent=2)
#         st.download_button("Download JSON", data=json_data, file_name="profile.json", mime="application/json")

#     # زر تنزيل Markdown
#     if 'save_markdown' in globals():
#         markdown_data = save_markdown(profile)
#         st.download_button("Download Markdown", data=markdown_data, file_name="profile.md", mime="text/markdown")
