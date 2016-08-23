import yaml

def convert_to_python_obj(string):
    try:
        return yaml.load(string)
    except ValueError:
        return False


def convert_file_to_python_obj(filename, root_path=None):
    array = []
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                array.append(line)
        return array
    except IOError:
        return "File not found"

