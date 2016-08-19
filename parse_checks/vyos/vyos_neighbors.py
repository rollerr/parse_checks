import re

from collections import namedtuple
from parse_checks.utilities import helpers

LLDPMap = namedtuple('LLDPMap', ['remote_device', 'local_interface', 'protocol', 'capability', 'platform',
                                 'remote_interface'])


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


def validate_lldp_neighbors(device_output, validation_args):
    supplied_lldp_neighbors = helpers.convert_to_python_obj(validation_args)
    lldp_neighbor_array_output = construct_lldp_neighbor_array(device_output)
    lldp_neighbor_matches = []

    for lldp_neighbor in supplied_lldp_neighbors:
        supplied_local_interface, supplied_remote_device, supplied_remote_interface = lldp_neighbor

        for remote_lldp_neighbor_output in lldp_neighbor_array_output:
            if all([supplied_local_interface == remote_lldp_neighbor_output.local_interface,
                    supplied_remote_device == remote_lldp_neighbor_output.remote_device,
                    supplied_remote_interface == remote_lldp_neighbor_output.remote_interface]
                    ):

                    lldp_neighbor_matches.append((lldp_neighbor, remote_lldp_neighbor_output))
                    break

    return lldp_neighbor_matches
