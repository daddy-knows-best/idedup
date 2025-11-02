# idedup

## Expectation and Proof of Concept

```
(idedup) macbookair:idedup seungyeop$ tshark -r test.pcapng -T fields -e frame.protocols | cat -n
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
(idedup) macbookair:idedup seungyeop$ tshark -r test.pcapng -T fields -e frame.protocols | ./idedup
     1  eth:ethertype:ip:udp:dhcp
     2  eth:ethertype:ip:udp:data
     6  eth:ethertype:ip:icmp:ip:udp
     8  eth:ethertype:ip:tcp:tls
    10  eth:ethertype:ip:tcp
    13  eth:ethertype:ipv6:udp:data
(idedup) macbookair:idedup seungyeop$
```
