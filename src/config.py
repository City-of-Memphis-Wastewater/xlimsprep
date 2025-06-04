import toml
from pathlib import Path

def get_skip_list_from_exclude_variables_toml():
    config_path = Path(__file__).parent / ".." / "configs" / "exclude_variables.toml"
    config = toml.load(config_path.resolve())
    skip_list = config["skip_parameters"]
    return skip_list