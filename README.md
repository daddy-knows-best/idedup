[![Python package](https://github.com/daddy-knows-best/idedup/actions/workflows/python-package.yml/badge.svg)](https://github.com/daddy-knows-best/idedup/actions/workflows/python-package.yml)
[![Release Python Package](https://github.com/daddy-knows-best/idedup/actions/workflows/release.yml/badge.svg)](https://github.com/daddy-knows-best/idedup/actions/workflows/release.yml)
[![Pybadges](https://github.com/daddy-knows-best/idedup/blob/main/pybadge.svg)](https://github.com/daddy-knows-best/idedup/blob/main/pybadge.svg)

# idedup

## Installation and How to use

```
$ mkdir test_idedup
$ cd test_idedup/
$ uv init
Initialized project `test-idedup`
$ uv venv
Using CPython 3.14.0
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
$ svactivate
(test_idedup) $ uv pip install -i https://test.pypi.org/simple/ idedup
Resolved 1 package in 9ms
Installed 1 package in 5ms
 + idedup==0.1.0
(test_idedup) $ tshark -r test.pcapng -T fields -e frame.protocols | cat -n
     1	eth:ethertype:ip:udp:dhcp
     2	eth:ethertype:ip:udp:data
     3	eth:ethertype:ip:udp:data
     4	eth:ethertype:ip:udp:data
     5	eth:ethertype:ip:udp:data
     6	eth:ethertype:ip:icmp:ip:udp
     7	eth:ethertype:ip:icmp:ip:udp
     8	eth:ethertype:ip:tcp:tls
     9	eth:ethertype:ip:tcp:tls
    10	eth:ethertype:ip:tcp
    11	eth:ethertype:ip:udp:data
    12	eth:ethertype:ip:udp:data
    13	eth:ethertype:ipv6:udp:data
(test_idedup) $ tshark -r test.pcapng -T fields -e frame.protocols | idedup
     1	eth:ethertype:ip:udp:dhcp
     2	eth:ethertype:ip:udp:data
     6	eth:ethertype:ip:icmp:ip:udp
     8	eth:ethertype:ip:tcp:tls
    10	eth:ethertype:ip:tcp
    13	eth:ethertype:ipv6:udp:data
(test_idedup) $
```
