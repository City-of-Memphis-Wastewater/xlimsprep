"""
Title: main.py
Created: 03 June 2025
Author: George Clayton Bennett

Purpose:
Import data from X-Lims export for
    - Primary clarifier
    - Other
Sanitize Data 
Plot data
Export sanitized data to 
"""

from src.importer import import_csv_to_pd_df
from src.helpers import get_csv_filepaths_in_imports
from src.helpers import convert_filename_to_title
from src.helpers import convert_csv_import_path_to_png_export_path
from src.helpers import convert_csv_import_filepath_to_csv_export_filepath
from src.sanitizer import convert_xlims_data_to_columns
from src.sanitizer import compare_columns
from src.sanitizer import check_for_diversity_in_parameter_units_dictionary
from src.exporter import export_sanitized
from src.plotter import plot_sanitized
from src.exporter import export_sanitized

def main():
    
    #print(f"get_csv_filepaths_in_imports() = {get_csv_filepaths_in_imports()}")
    print(f"csv file count = {len(get_csv_filepaths_in_imports())}")

    # Import data from xlims export files (manually prepared)
    parameter_units_dictionary_aggregate = {}
    for csv_filepath in get_csv_filepaths_in_imports():
        print(f"csv_filepath = {csv_filepath.name}")
        df_xlims_i = import_csv_to_pd_df(csv_filepath = csv_filepath)
        #print(f"df_xlims_i = {df_xlims_i}")
        compare_columns(df = df_xlims_i, columnA= "SWPPRCalc", columnB= "ReportedResult")
        # Sanitize data, convert to unique columns
        parameter_units_dictionary_i = None  
        df_sanitized_i, parameter_units_dictionary_i = convert_xlims_data_to_columns(df_xlims_i)
        parameter_units_dictionary_aggregate = check_for_diversity_in_parameter_units_dictionary(parameter_units_dictionary_aggregate,parameter_units_dictionary_i)
        if df_sanitized_i is not None:
            export_sanitized(df=df_sanitized_i, csv_export_filepath = convert_csv_import_filepath_to_csv_export_filepath(csv_filepath))
            plot_sanitized(df=df_sanitized_i, tag=convert_filename_to_title(csv_filepath), units = parameter_units_dictionary_i, png_filepath = convert_csv_import_path_to_png_export_path(csv_filepath))

if __name__ == "__main__":
    main()