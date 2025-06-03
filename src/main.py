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
from src.sanitizer import convert_xlims_data_to_columns
from src.plotter import plot_sanitized
from src.helpers import get_csv_files_relative_to_main
from src.helpers import convert_filename_to_title
from src.helpers import check_for_diversity_in_parameter_units_dictionary

def main():
    # Import data from xlims export files (manually prepared)
    parameter_units_dictionary_aggregate = {}

    for csv_filename in get_csv_files_relative_to_main():
        
        df_xlims_primary = import_csv_to_pd_df(csv_file = csv_filename)
        #df_xlims_other = import_csv_to_pd_df(filename = "other.csv") #spoof

        # Sanitize data, convert to unique columns 
        df_sanitized_primary, parameter_units_dictionary = convert_xlims_data_to_columns(df_xlims_primary)
        parameter_units_dictionary_aggregate = check_for_diversity_in_parameter_units_dictionary(parameter_units_dictionary_aggregate,parameter_units_dictionary)
        plot_sanitized(df_sanitized=df_sanitized_primary, tag=convert_filename_to_title(csv_filename))
    
if __name__ == "__main__":
    main()