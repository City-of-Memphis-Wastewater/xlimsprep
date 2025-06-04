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

def plot_sanitized(df, tag, units, csv_filepath):

    

    skip_list = ['% Solids (Generated Monthly-MOR)',
                'Rainfall',
                'Weight of Sludge(Dry) Generated', 
                'Weight of Sludge(Dry) Disposed',
                '% VOL. RED.', 
                'Cake Dry Tons/Day', 
                'Dissolved O2 - North',
                'Hours Bypassed', 
                'Peracetic Acid',
                'Qty Wet Sludge Disposed',
                'Qty Wet Sludge Generated',
                'Volatile Solids Reduction Waste Sludge to Disposal',
                'Temperature - DIG.SDG.',
                'Wet Cake',
                'Dissolved Oxygen, Effluent',
                'Dissolved Oxygen, Influent',
                'Flow(MAX), Influent'
                #'Flow, Effluent',
                '% Volatile Suspended Solids',
                'Total Suspended Solids',
                'Volatile Suspended Solids'
                '% Solids (Generated Monthly-MOR)',
                'Qty Wet Sludge Disposed',
                'Qty Wet Sludge Generated',
                'Volatile Solids Reduction Waste Sludge to Disposal',
                'Weight of Sludge(Dry) Disposed',
                'Weight of Sludge(Dry) Generated',
                '% VOL. RED.',
                'Cake Dry Tons/Day',
                'Dissolved O2 - North',
                'Dissolved Oxygen, Effluent',
                'Dissolved Oxygen, Influent',
                'Flow(MAX), Influent',
                #'Flow, Effluent',
                #'Flow, Influent',
                'Hours Bypassed',
                'Peracetic Acid',
                #'pH - Effluent (Max)',
                #'pH - Effluent (Min)',
                #'pH - Influent',
                'Pounds of Chlorine - Effluent',
                'Pounds of Sulfur Dioxide - Effluent',
                'Rainfall',
                'Temperature - DIG.SDG.',
                #'Temperature - Effluent',
                #'Temperature - Influent',
                #'Temperature - North',
                'Wet Cake',
                '% Volatile Suspended Solids',
                'Total Suspended Solids',
                #'TSS - Change in Wt',
                'Volatile Suspended Solids',
                #'Biochemical Oxygen Demand',
                'Dissolved Oxygen',
                #'pH',
                'Sample Amount',
                'Settleable Solids',
                'Sulfur',
                'Ammonia as N',
                'Chemical Oxygen Demand',
                'Soluble BOD',
                'Organic Nitrogen',
                'Total Nitrogen',
                'Phosphorus-total',
                'LC50 Static 48Hr Acute Ceriodaphnia',
                'LC50 Static 48Hr Acute Pimephales',
                'Total Alkalinity (as CaCO3)',
                'Calcium',
                'Hardness',
                'Magnesium',
                'Arsenic',
                'Cadmium',
                'Chromium',
                'Cobalt',
                'Copper',
                'Lead',
                'Analysis Date/Time',
                'Mercury',
                'Method Reference',
                'Subcontract Lab ID',
                'Molybdenum',
                'Nickel',
                'Selenium',
                'Zinc',
                'Oil and Grease (HEM)',
                'Volatile Acids',
                'SARS-COV2'
                 ]
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
    png_filepath = convert_import_path_to_export_path(csv_filepath)
    plt.savefig(png_filepath, dpi=300, bbox_inches='tight')
    plt.close()
    #plt.show()

def convert_import_path_to_export_path(csv_path: Path) -> Path:
    parts = list(csv_path.parts)
    try:
        i = parts.index('imports')
        parts[i] = 'exports'
        return Path(*parts).with_suffix('.png')
    except ValueError:
        raise ValueError(f"'imports' not found in path: {csv_path}")
