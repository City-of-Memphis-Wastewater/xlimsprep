"""
Title: plotter.py
Created: 03 June 2025
Author: George Clayton Bennett

Purpose:
Plot data 
"""
from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd

def plot_sanitized(df, tag, units):
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
                 'Wet Cake',
                 'Dissolved Oxygen, Effluent',
                 'Dissolved Oxygen, Influent',
                 'Flow(MAX), Influent']
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
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.ylim(0, 190)        # y-axis from 0 to 35
    plt.show()