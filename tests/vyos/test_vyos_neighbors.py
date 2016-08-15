from collections import namedtuple
from textwrap import dedent
from parse_checks.vyos import vyos_neighbors

LLDPMap = namedtuple('LLDPMap', ['remote_device', 'local_interface', 'protocol', 'capability', 'platform',
                                     'remote_interface'])

vyos_lldp_output = dedent("""\
                  Capability Codes: R - Router, B - Bridge, W - Wlan r - Repeater, S - Station
                  D - Docsis, T - Telephone, O - Other

                  Device ID                 Local  Proto  Cap   Platform             Port ID
                  ---------                 -----  -----  ---   --------             -------
                  dc2-tor-r1                eth0   LLDP   R     Vyatta Router        eth0
                  dc2-edg-r1                eth0   LLDP   R     Vyatta Router        eth0
                  dc2-edg-r2                eth0   LLDP   R     Vyatta Router        eth0
                  dc2-tor-r1                eth1   LLDP   R     Vyatta Router        eth5
                  dc2-tor-r1                eth2   LLDP   R     Vyatta Router        eth6
                  dc2-tor-r1                eth3   LLDP   R     Vyatta Router        eth7
                  dc2-tor-r1                eth4   LLDP   R     Vyatta Router        eth8
                  dc2-edg-r1                eth5   LLDP   R     Vyatta Router        eth1
                  dc2-edg-r1                eth6   LLDP   R     Vyatta Router        eth2
                  dc2-edg-r2                eth7   LLDP   R     Vyatta Router        eth1
                  dc2-edg-r2                eth8   LLDP   R     Vyatta Router        eth2
                  """)
vyos_lldp_output_response =[LLDPMap(remote_device='dc2-tor-r1', local_interface='eth0', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth0'),
                            LLDPMap(remote_device='dc2-edg-r1', local_interface='eth0', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth0'),
                            LLDPMap(remote_device='dc2-edg-r2', local_interface='eth0', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth0'),
                            LLDPMap(remote_device='dc2-tor-r1', local_interface='eth1', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth5'),
                            LLDPMap(remote_device='dc2-tor-r1', local_interface='eth2', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth6'),
                            LLDPMap(remote_device='dc2-tor-r1', local_interface='eth3', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth7'),
                            LLDPMap(remote_device='dc2-tor-r1', local_interface='eth4', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth8'),
                            LLDPMap(remote_device='dc2-edg-r1', local_interface='eth5', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth1'),
                            LLDPMap(remote_device='dc2-edg-r1', local_interface='eth6', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth2'),
                            LLDPMap(remote_device='dc2-edg-r2', local_interface='eth7', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth1'),
                            LLDPMap(remote_device='dc2-edg-r2', local_interface='eth8', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth2')]
 

def test_construct_lldp_neighbor_array(device_output, expected_response):
    assert vyos_neighbors.construct_lldp_neighbor_array(device_output) == expected_response

