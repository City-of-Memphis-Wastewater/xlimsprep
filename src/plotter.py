"""
Title: plotter.py
Created: 03 June 2025
Author: George Clayton Bennett

Purpose:
Plot data 
"""
from matplotlib import pyplot as plt

def plot_sanitized(df_sanitized, tag):
    
    fig, axs = plt.subplots(1, 1, layout='constrained')
    axs[0].plot(date,)
    axs[0].set_xlim(0, 2)
    axs[0].set_xlabel('Time (June 1, 2024 to June 1, 2025)')
    axs[0].set_ylabel('s1 and s2')
    axs[0].grid(True)
    axs[0].set_title('Primary')
    plt.show()

    
    for col in df.columns:
        if col != 'Time':  # Skip 'Time' if it's the x-axis
            plt.plot(df['Time'], df[col], label=col)

    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(tag)
    plt.legend()
    plt.grid(True)
    plt.show()