try:
    import yaml
except ImportError as exc:
    raise ImportError("Missing dependency: install pyyaml with 'pip install pyyaml'") from exc


def load_config(filename):
    with open(filename, "r") as file:
        return yaml.safe_load(file)
    
required_sections = ["app","database"]

def check_sections(config,required):
    for section in required:
        if section not in config:
            print(f"Error: missing required section '{section}'")

def validate_types(config):
    db = config.get("database",{})
    if not isinstance(db.get("port"),int):
        print("Error: database.port must be an integer")
    if not isinstance(db.get("enabled"),bool):
        print("Error: database.enabled must be true or false")



DEFAULTS = {
    "app": {"version": "0.0.1"},
    "database": {"host": "localhost", "port": 5432, "enabled": False}
}

def apply_defaults(config, defaults):
    for section, values in defaults.items():
        if section not in config:
            config[section] = {}
        for key, default_value in values.items():
            if key not in config[section]:
                config[section][key] = default_value
    return config


if __name__ == "__main__":
    config = load_config("config.yaml")

    check_sections(config, required_sections)
    validate_types(config)
    config = apply_defaults(config, DEFAULTS)

    print("Config loaded successfully:")
    print(config)
