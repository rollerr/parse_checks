import yaml

def convert_to_python_obj(string):
    try:
        return yaml.load(string)
    except ValueError:
        return False
