import re
import yaml

from collections import namedtuple

def convert_to_python_obj(string):
	try:
		yaml.load(string)
	except ValueError:
		return False


def construct_lldp_neighbor_dict(device_output):
	'''
	input a list of output
	return data structure representation
	'''
	lldp_neighbor_array = {}
	matching_pattern = re.compile('\s{2,}')
	LLDPMap = namedtuple('LLDPMap', ['remote_device', 'local_interface', 'protocol', 'capability', 'platform',
						 			 'remote_interface'])

	for line in device_output:
		line = line.strip().lower()
		if 'lldp' in line:
			 lldp_neighbor_array.append(*matching_pattern.split(line))

	return lldp_neighbor_array


def validate_lldp_neighbors(validation_args, device_output, input_file=None):
	validation_args = convert_to_python_obj(validation_args)

