import inspect
from pathlib import Path

def get_csv_files_relative_to_main():
    # Step 1: Get the path of the current file (e.g., main.py)
    current_file = Path(inspect.getfile(inspect.currentframe())).resolve()
    
    # Step 2: Get the directory containing main.py
    root_dir = current_file.parent.parent
    print(f"root_dir = {root_dir}")
    
    # Step 3: Find the 'imports' directory relative to that location
    imports_dir = root_dir / 'imports'
    
    # Step 4: Get all CSV files in the 'imports' directory
    if imports_dir.exists() and imports_dir.is_dir():
        csv_files = sorted(imports_dir.glob('*.csv'))
        return csv_files
    else:
        print("imports dir not found")
        return []

def convert_filename_to_title(filename):

    # Get the stem (filename without extension)
    name = filename.rsplit('.', 1)[0]  # Remove extension

    # Remove xlims text
    name=name.replace('_xlims', '')
    
    # Replace underscores with spaces and title-case it
    title = name.replace('_', ' ').title()
    
    return title

def test_get_csv_files_relative_to_main():
    # Example usage
    print("Get CSV files in imports dir")
    print("\nFiles:")
    for csv_file in get_csv_files_relative_to_main():
        print(csv_file.name)
        print(convert_filename_to_title(filename=csv_file.name))

    print("\nEND\n")

if __name__ == "__main__":
    test_get_csv_files_relative_to_main()