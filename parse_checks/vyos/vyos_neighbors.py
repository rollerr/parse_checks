import re
import yaml

from collections import namedtuple

LLDPMap = namedtuple('LLDPMap', ['remote_device', 'local_interface', 'protocol', 'capability', 'platform',
                                 'remote_interface'])

def convert_to_python_obj(string):
    try:
        return yaml.load(string)
    except ValueError:
        return False


def construct_lldp_neighbor_array(device_output):
    '''
    input a string of output
    return data structure representation
    '''
    lldp_neighbor_array = []
    matching_pattern = re.compile('\s{2,}')
    device_output = device_output.splitlines()

    for line in device_output:
        line = line.strip()
        if 'lldp' in line.lower():
             lldp_neighbor_array.append(LLDPMap(*matching_pattern.split(line)))

    return lldp_neighbor_array


# dectorate with a wrapper for output or input file
def validate_lldp_neighbors(device_output, validation_args, input_file=None, validate_local_interface=False):
    supplied_lldp_neighbors = convert_to_python_obj(validation_args)
    lldp_neighbor_array_output = construct_lldp_neighbor_array(device_output)
    lldp_neighbor_matches = []

    for lldp_neighbor in supplied_lldp_neighbors:
        lldp_neighbor = [None] + lldp_neighbor if not(validate_local_interface) else lldp_neighbor
        supplied_local_interface, supplied_remote_device, supplied_remote_interface = lldp_neighbor 
        
        for remote_lldp_neighbor_output in lldp_neighbor_array_output:
            if validate_local_interface:
                if all([supplied_local_interface == remote_lldp_neighbor_output.local_interface,
                        supplied_remote_device == remote_lldp_neighbor_output.remote_device,
                        supplied_remote_interface == remote_lldp_neighbor_output.remote_interface]
                        ):
                        
                        lldp_neighbor_matches.append((lldp_neighbor, remote_lldp_neighbor_output))
                        break
    import pdb;pdb.set_trace()
    return lldp_neighbor_matches

