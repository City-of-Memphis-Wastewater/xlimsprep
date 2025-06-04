'''
Title: exporter.py
Author: George Clayton Bennett
Created: 03 June 2025

Purpose:
    Export data to CSV, 
'''

def export_sanitized(df,csv_export_filepath):
    """
    Exports a sanitized DataFrame to a specified CSV file path.

    Parameters:
    - df (pd.DataFrame): The sanitized DataFrame to export.
    - csv_export_filepath (str or Path): Path where the CSV should be saved.
    """
    from pathlib import Path

    export_path = Path(csv_export_filepath)
    export_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists

    df.to_csv(export_path, index=False)
    print(f"Sanitized data exported to {export_path}")
            