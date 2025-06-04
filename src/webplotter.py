import pandas as pd
import plotly.express as px
from pathlib import Path

EXPORTS_DIR = Path("exports")
OUTPUT_DIR = Path("webpage/graphs")
INDEX_PATH = Path("webpage/index.html")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

html_links = []

for csv_file in EXPORTS_DIR.glob("*.csv"):
    df = pd.read_csv(csv_file)
    df = df.set_index(['SampledDate'])

    # Try to guess what to plot — adjust as needed
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) < 2:
        print(f"Skipping {csv_file.name} — not enough numeric columns")
        continue

    fig = px.line(df, x=df.index, y=numeric_cols[1:], title=csv_file.stem)
    html_filename = csv_file.stem + ".html"
    html_path = OUTPUT_DIR / html_filename

    fig.write_html(html_path, full_html=True, include_plotlyjs='cdn')

    # For the index.html
    html_links.append(f'<li><a href="graphs/{html_filename}" target="_blank">{csv_file.stem.replace("_", " ").title()}</a></li>')

# Write the index.html
index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Graph Viewer</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <h1>Graphs</h1>
  <ul>
    {'\n    '.join(html_links)}
  </ul>
</body>
</html>
"""

INDEX_PATH.write_text(index_html)
print("Done generating plots and index.html")
