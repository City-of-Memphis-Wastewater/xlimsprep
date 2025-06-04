import inspect
from pathlib import Path

def get_csv_filepaths_in_imports():
    # Step 1: Get the path of the current file (e.g., main.py)
    current_file = Path(inspect.getfile(inspect.currentframe())).resolve()
    
    # Step 2: Get the directory containing main.py
    root_dir = current_file.parent.parent
    
    # Step 3: Find the 'imports' directory relative to that location
    imports_dir = root_dir / 'imports'
    
    # Step 4: Get all CSV files in the 'imports' directory
    if imports_dir.exists() and imports_dir.is_dir():
        #csv_files = sorted(imports_dir.glob('*.csv'))
        csv_file_paths = [f.resolve() for f in imports_dir.glob("*.csv") if f.is_file()]
        return csv_file_paths
    else:
        print("imports dir not found")
        return []

def convert_filename_to_title(filename):

    # Get the stem (filename without extension)
    #name = filename.rsplit('.', 1)[0]  # Remove extension
    name = filename.with_suffix('').name

    # Remove xlims text
    name=name.replace('_xlims', '')
    
    # Replace underscores with spaces and title-case it
    title = name.replace('_', ' ').title()
    
    return title

def convert_csv_import_path_to_png_export_path(csv_path: Path) -> Path:
    parts = list(csv_path.parts)
    try:
        i = parts.index('imports')
        parts[i] = 'exports'
        return Path(*parts).with_suffix('.png')
    except ValueError:
        raise ValueError(f"'imports' not found in path: {csv_path}")
    
def convert_csv_import_filepath_to_csv_export_filepath(csv_path: Path) -> Path:
    parts = list(csv_path.parts)
    try:
        i = parts.index('imports')
        parts[i] = 'exports'
        return Path(*parts).with_suffix('.csv')
    except ValueError:
        raise ValueError(f"'imports' not found in path: {csv_path}")

def test_get_csv_filepaths_in_imports():
    # Example usage
    print("Get CSV files in imports dir")
    print("\nFiles:")
    for csv_file in get_csv_filepaths_in_imports():
        print(csv_file.name)
        print(convert_filename_to_title(filename=csv_file.name))

    print("\nEND\n")

if __name__ == "__main__":
    test_get_csv_filepaths_in_imports()