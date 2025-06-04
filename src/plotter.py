"""
Title: plotter.py
Created: 03 June 2025
Author: George Clayton Bennett

Purpose:
Plot data 
"""
from matplotlib import pyplot as plt
import pandas as pd
from pathlib import Path

from src.config import get_skip_list_from_exclude_variables_toml

def plot_sanitized(df, tag, units, png_filepath):
    skip_list = get_skip_list_from_exclude_variables_toml()
    # Ensure SampledDate is datetime
    if not pd.api.types.is_datetime64_any_dtype(df['SampledDate']):
        df['SampledDate'] = pd.to_datetime(df['SampledDate'], errors='coerce')
    plt.figure(figsize=(12, 6))
    
    for col in df.columns:
        
        if col != 'SampledDate' and col not in skip_list:  # Skip 'Time' if it's the x-axis
            y = pd.to_numeric(df[col], errors='coerce')  # convert to numeric safely
            label = col
            if units and col in units:
                label += f" ({units[col]})"
            plt.plot(df['SampledDate'], y, label=label) # marker='o'

    plt.xlabel('SampledDate')
    plt.ylabel('Value')
    plt.title(tag)
    #plt.title("Maxson Overview, June 2024 to May 2025")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    #plt.ylim(0, 190)        # y-axis from 0 to 35

    #png_filepath = str(csv_filepath).replace("imports","export").replace(".csv",".png")
    #png_filepath = convert_csv_import_path_to_png_export_path(csv_filepath)
    plt.savefig(png_filepath, dpi=300, bbox_inches='tight')
    plt.close()
    #plt.show()


