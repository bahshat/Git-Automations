from pathlib import Path
import yaml
import sys

def load_config(path=Path("config.yaml")):
    try:
        return yaml.safe_load(path.read_text())
    except FileNotFoundError:
        sys.exit("Config file not found.")
    except yaml.YAMLError:
        sys.exit("Invalid YAML format.")