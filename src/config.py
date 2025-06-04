import toml
from pathlib import Path

def get_skip_list_from_exclude_parameters_toml():
    config_path = Path(__file__).parent / ".." / "configs" / "exclude_parameters.toml"
    config = toml.load(config_path.resolve())
    skip_list = config["skip_parameters"]
    return skip_list

def config_show_parameter_list():
    config_path = Path(__file__).parent / ".." / "configs" / "show_parameter_lists.toml"
    config = toml.load(config_path.resolve())
    show_parameter_lists = bool(config["show_parameter_lists"])
    return show_parameter_lists