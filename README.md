[![Python package](https://github.com/daddy-knows-best/idedup/actions/workflows/python-package.yml/badge.svg)](https://github.com/daddy-knows-best/idedup/actions/workflows/python-package.yml)
[![Release Python Package](https://github.com/daddy-knows-best/idedup/actions/workflows/release.yml/badge.svg)](https://github.com/daddy-knows-best/idedup/actions/workflows/release.yml)
![https://github.com/daddy-knows-best/idedup/blob/main/pybadge.svg](https://github.com/daddy-knows-best/idedup/blob/main/pybadge.svg)

# idedup

## Expectation and Proof of Concept

```
(idedup) $ tshark -r test.pcapng -T fields -e frame.protocols | cat -n
     1  eth:ethertype:ip:udp:dhcp
     2  eth:ethertype:ip:udp:data
     3  eth:ethertype:ip:udp:data
     4  eth:ethertype:ip:udp:data
     5  eth:ethertype:ip:udp:data
     6  eth:ethertype:ip:icmp:ip:udp
     7  eth:ethertype:ip:icmp:ip:udp
     8  eth:ethertype:ip:tcp:tls
     9  eth:ethertype:ip:tcp:tls
    10  eth:ethertype:ip:tcp
    11  eth:ethertype:ip:udp:data
    12  eth:ethertype:ip:udp:data
    13  eth:ethertype:ipv6:udp:data
(idedup) $ tshark -r test.pcapng -T fields -e frame.protocols | ./idedup
     1  eth:ethertype:ip:udp:dhcp
     2  eth:ethertype:ip:udp:data
     6  eth:ethertype:ip:icmp:ip:udp
     8  eth:ethertype:ip:tcp:tls
    10  eth:ethertype:ip:tcp
    13  eth:ethertype:ipv6:udp:data
(idedup) $
```
