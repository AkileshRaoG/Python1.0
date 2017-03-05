
from scapy.all import *

p = rdpcap("C:\\Users\\raoga3\\Desktop\\Rao\\pcaps\\x11_lua.pcap")
s = p.sessions()
d=[]
for k in s:
    if 'TCP' in k:
        d.append(s[k])
pktdump = PcapWriter("C:\\Users\\raoga3\\Desktop\\Rao\\pcaps\\smtp_packet1.pcap", append=True, sync=True)

for i in d:
    pktdump.write(i)
