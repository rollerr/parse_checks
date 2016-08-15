from textwrap import dedent
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
vyos_lldp_output_response = 

def test_construct_lldp_neighbor_array
