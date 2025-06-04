import pandas as pd
from pprint import pprint
def convert_xlims_data_to_columns(df_xlims):
    print(f"df_xlims['Parameter'] = {df_xlims['Parameter']}")

    # Pivot the DataFrame so each parameter becomes a column
    df_sanitized = convert_df_single_parameter_column_and_multiple_date_rows_to_multiple_paramter_columns_and_one_row_per_date(df_xlims)
    
    # Create dictionary of unique parameters and units
    parameter_units_dictionary = make_dict_of_unique_parameters_with_respective_units(df_xlims)
    print("df_sanitized = ")
    pprint(df_sanitized)
    print("parameter_units_dictionary = ")
    pprint(parameter_units_dictionary)
    print("parameter_list = ")
    pprint(list(parameter_units_dictionary.keys()))
    return df_sanitized, parameter_units_dictionary

def convert_df_single_parameter_column_and_multiple_date_rows_to_multiple_paramter_columns_and_one_row_per_date(df):
    """
    Pivot a DataFrame with 'SampledDate', 'Parameter', and 'ReportedResult' into a wide format.
    """
    df = df.copy()

    # Ensure SampledDate is datetime
    df["SampledDate"] = pd.to_datetime(df["SampledDate"], errors="coerce")

    # Pivot table
    df_wide = df.pivot_table(
        index="SampledDate",
        columns="Parameter",
        #values="ReportedResult",
        values="SWPPRCalc",
        aggfunc="first"  # or np.mean, depending on needs
    ).reset_index()

    return df_wide

def make_dict_of_unique_parameters_with_respective_units(df_xlims):
    """
    Build a dictionary of parameters and their associated units.
    Assumes each parameter only has one unit.
    """
    df_unique = df_xlims[["Parameter", "Unit"]].drop_duplicates()
    
    parameter_units_dictionary = dict(zip(df_unique["Parameter"], df_unique["Unit"]))
    
    return parameter_units_dictionary

def check_for_diversity_in_parameter_units_dictionary(dict_agg,dict_i):
    # Early assertion to catch unexpected input
    assert isinstance(dict_agg, dict) or dict_agg is None, f"dict_agg must be dict or None, got {type(dict_agg)}"
    assert isinstance(dict_i, dict), f"dict_i must be dict, got {type(dict_i)}"

    if dict_agg is None:
        return dict_i
    
    dict_i_clean = does_dictionary_i_have_redundant_keypairs_that_disagree_with_aggregate_dict(dict_agg,dict_i)
    print("dict_i_clean = ")
    pprint(dict_i_clean)
    print("dict_agg = ")
    pprint(dict_agg)
    dict_agg.update(dict_i_clean)
    print('list_agg')
    pprint(list(dict_agg.keys()))
    return dict_agg

def does_dictionary_i_have_redundant_keypairs_that_disagree_with_aggregate_dict(
    parameter_units_dictionary_aggregate: dict,
    parameter_units_dictionary_i: dict
    ) -> dict:
    """
    Compares two dictionaries for overlapping keys with different values.
    Prints warnings for disagreements and returns a cleaned version of
    the second dictionary that excludes conflicting keys.
    """
    cleaned_dict = {}

    for key, value in parameter_units_dictionary_i.items():
        if key in parameter_units_dictionary_aggregate:
            if parameter_units_dictionary_aggregate[key] != value:
                print(f"WARNING: Conflict for key '{key}': "
                      f"'{parameter_units_dictionary_aggregate[key]}' (aggregate) "
                      f"!= '{value}' (i)")
                continue  # skip conflicting key
        cleaned_dict[key] = value

    return cleaned_dict

def compare_columns(df, columnA, columnB):
    """
    Compares two numeric columns in a DataFrame and prints rows where they differ.

    Args:
        df (pd.DataFrame): The DataFrame to check.
        columnA (str): Name of the first column.
        columnB (str): Name of the second column.
    """
    import numpy as np

    # Ensure columns exist
    if columnA not in df.columns or columnB not in df.columns:
        print(f"ERROR: One or both columns not found: '{columnA}', '{columnB}'")
        return

    # Convert to numeric (safe), forcing errors to NaN
    a = pd.to_numeric(df[columnA], errors='coerce')
    b = pd.to_numeric(df[columnB], errors='coerce')

    # Compare with NaN-aware inequality
    mask = (a != b) & ~(a.isna() & b.isna())

    if mask.any():
        print("Mismatched rows:")
        print(df.loc[mask, [columnA, columnB]])
    else:
        print(f"✅ All numeric values are identical between columns {columnA} and {columnB}.")
