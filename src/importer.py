"""
Title: importer.py
Created: 03 June 2025
Author: George Clayton Bennett

Purpose:
Import data from X-Lims export for
    - Primary clarifier
    - Other
"""
import pandas as pd

def import_csv_to_pd_df(csv_filepath):
    """
    Import a CSV file into a pandas DataFrame.

    Args:
        csv_filepath (str): Path to the CSV file.
        encoding (str): File encoding (default 'utf-8').
        parse_dates (bool): Try to parse date columns automatically.

    Returns:
        pd.DataFrame: DataFrame containing the CSV contents.
    """
    try:
        df = pd.read_csv(csv_filepath, 
                         encoding='utf-8', 
                         parse_dates=True,
                         delimiter=',',
                         skiprows=3,
                        engine='python',  # safer for mixed formatting
                        on_bad_lines='warn')  # warn on bad rows
        return df
    except FileNotFoundError:
        print(f"ERROR: File not found: {csv_filepath}")
    except pd.errors.ParserError as e:
        print(f"ERROR parsing CSV file: {e}")
    except Exception as e:
        print(f"Unexpected error reading '{csv_filepath}': {e}")
    
    return pd.DataFrame()  # Return empty DataFrame on failure
    