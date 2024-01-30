# wireless_sniffer.py

import scapy.all as scapy

def sniff_wireless_traffic(interface):
    print(f"Sniffing wireless traffic on interface {interface}...")
    try:
        scapy.sniff(iface=interface, prn=process_packet, store=False)
    except Exception as e:
        print(f"Error sniffing wireless traffic: {e}")

def process_packet(packet):
    # Example: Analyze wireless packets and extract relevant information
    # Replace with actual analysis logic based on the desired information
    if packet.haslayer(scapy.Dot11):
        print(packet.summary())

if __name__ == "__main__":
    interface = input("Enter wireless interface to sniff (e.g., wlan0): ")
    sniff_wireless_traffic(interface)
