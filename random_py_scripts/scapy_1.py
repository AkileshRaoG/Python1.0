
from scapy.all import *

p = rdpcap("C:\\Users\\raoga3\\Desktop\\Rao\\pcaps\\packet-000000014.pcap")
s = p.sessions()
d=[]
for k in s:
    if 'SMTP' in k:
        d.append(s[k])
pktdump = PcapWriter("smtp_packet1.pcap", append=True, sync=True)

for i in d:
    pktdump.write(i)
