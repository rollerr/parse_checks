from collections import namedtuple
from textwrap import dedent
from parse_checks.vyos.vyos_neighbors import *


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

validation_args = [['eth1', 'dc2-tor-r1', 'eth5'], ['eth2', 'dc2-tor-r1', 'eth6']]

vyos_lldp_dict = {'vyos-r1': dedent("""\
                  Capability Codes: R - Router, B - Bridge, W - Wlan r - Repeater, S - Station
                  D - Docsis, T - Telephone, O - Other

                  Device ID                 Local  Proto  Cap   Platform             Port ID
                  ---------                 -----  -----  ---   --------             -------
                  dc2-tor-r1                eth10  LLDP   R     Vyatta Router        eth11
                  dc2-edg-r1                eth4   LLDP   R     Vyatta Router        eth9
                  dc2-edg-r2                eth18  LLDP   R     Vyatta Router        eth2
                  """),
                  'vyos-r2': dedent("""\
                  Capability Codes: R - Router, B - Bridge, W - Wlan r - Repeater, S - Station
                  D - Docsis, T - Telephone, O - Other

                  Device ID                 Local  Proto  Cap   Platform             Port ID
                  ---------                 -----  -----  ---   --------             -------
                  dc4-tor-r1                eth8   LLDP   R     Vyatta Router        eth11
                  dc4-edg-r1                eth4   LLDP   R     Vyatta Router        eth4
                  dc4-edg-r2                eth2   LLDP   R     Vyatta Router        eth2
                  dc4-tor-r1                eth1   LLDP   R     Vyatta Router        eth5
                  """)}

vyos_lldp_dict_2 = {'vyos-r1': u'Capability Codes: R - Router, B - Bridge, W - Wlan r - Repeater, S - Station\n                  D - Docsis, T - Telephone, O - Other\n\nDevice ID                 Local  Proto  Cap   Platform             Port ID \n---------                 -----  -----  ---   --------             ------- \nvyos-r1                   eth0   LLDP   R     Vyatta Router        eth1    \nvyos-r1                   eth0   LLDP   R     Vyatta Router        eth2    \nvyos-r1                   eth0   LLDP   R     Vyatta Router        eth3    \nvyos-r2                   eth0   LLDP   R     Vyatta Router        eth0    \nc8:60:00:0a:95:f5         eth0   LLDP   ?     Not received         Not received\nvyos-r1                   eth1   LLDP   R     Vyatta Router        eth0    \nvyos-r1                   eth1   LLDP   R     Vyatta Router        eth2    \nvyos-r1                   eth1   LLDP   R     Vyatta Router        eth3    \nvyos-r2                   eth1   LLDP   R     Vyatta Router        eth0    \nc8:60:00:0a:95:f5         eth1   LLDP   ?     Not received         Not received\nvyos-r1                   eth2   LLDP   R     Vyatta Router        eth0    \nvyos-r1                   eth2   LLDP   R     Vyatta Router        eth1    \nvyos-r1                   eth2   LLDP   R     Vyatta Router        eth3    \nvyos-r2                   eth2   LLDP   R     Vyatta Router        eth0    \nc8:60:00:0a:95:f5         eth2   LLDP   ?     Not received         Not received\nvyos-r1                   eth3   LLDP   R     Vyatta Router        eth0    \nvyos-r1                   eth3   LLDP   R     Vyatta Router        eth1    \nvyos-r1                   eth3   LLDP   R     Vyatta Router        eth2    \nvyos-r2                   eth3   LLDP   R     Vyatta Router        eth0    \nc8:60:00:0a:95:f5         eth3   LLDP   ?     Not received         Not received'}
vyos_lldp_csv_4 = dedent("""\
                         vyos-r1,eth0,vyos-r2,eth0
                         vyos-r1,eth1,vyos-r2,eth0
                         vyos-r1,eth9,vyos-l3,eth8
                         """)
vyos_lldp_csv_1 = dedent("""\
                       vyos-r1,eth10,dc2-tor-r1,eth11
                       vyos-r2,eth2,dc4-edg-r2,eth2
                       vyos-r1,eth4,dc2-edg-r1,eth9
                       vyos-r2,eth8,dc4-tor-r1,eth11
                       vyos-r2,eth4,dc4-edg-r1,eth4
                       vyos-r2,eth1,dc4-tor-r1,eth5
                       vyos-r1,eth18,dc2-edg-r2,eth2
                       """)

vyos_lldp_csv_2 = dedent("""\
                       vyos-r1,eth10,dc2-tor-r1,eth11
                       vyos-r1,eth18,dc2-edg-r2,eth2
                       """)

vyos_lldp_csv_3 = dedent("""\
                       vyos-r1,eth10,dc2-tor-r1,eth91
                       vyos-r1,eth18,dc2-edg-r2,eth2
                       """)


def test_construct_lldp_neighbor_array():
    assert construct_lldp_neighbor_array(vyos_lldp_output) == vyos_lldp_output_response


def test_validate_lldp_neighbors():
    vyos_lldp_output_response = [(['eth1', 'dc2-tor-r1', 'eth5'], LLDPMap(remote_device='dc2-tor-r1', local_interface='eth1', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth5')), (['eth2', 'dc2-tor-r1', 'eth6'], LLDPMap(remote_device='dc2-tor-r1', local_interface='eth2', protocol='LLDP', capability='R', platform='Vyatta Router', remote_interface='eth6'))]
    assert validate_lldp_neighbors(vyos_lldp_output, validation_args) == vyos_lldp_output_response


def test_link_checker():
    assert link_checker(vyos_lldp_dict, vyos_lldp_csv_1) == 'All neighbors match'
    assert link_checker(vyos_lldp_dict, vyos_lldp_csv_2) == 'All neighbors match'
    # bad remote interface
    assert link_checker(vyos_lldp_dict, vyos_lldp_csv_3) == 'Not found: vyos-r1,eth10,dc2-tor-r1,eth91'
    assert link_checker(vyos_lldp_dict_2, vyos_lldp_csv_4) == 'Not found: vyos-r1,eth9,vyos-l3,eth8'
