import re
import yaml

from collections import namedtuple

def convert_to_python_obj(string):
    try:
        yaml.load(string)
    except ValueError:
        return False


def construct_lldp_neighbor_array(device_output):
    '''
    input a string of output
    return data structure representation
    '''
    lldp_neighbor_array = []
    matching_pattern = re.compile('\s{2,}')
    LLDPMap = namedtuple('LLDPMap', ['remote_device', 'local_interface', 'protocol', 'capability', 'platform',
                                     'remote_interface'])
    device_output = device_output.splitlines()

    for line in device_output:
        line = line.strip()
        if 'lldp' in line.lower():
             lldp_neighbor_array.append(LLDPMap(*matching_pattern.split(line)))

    return lldp_neighbor_array


def validate_lldp_neighbors(validation_args, device_output, input_file=None):
    validation_args = convert_to_python_obj(validation_args)

