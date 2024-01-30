# packet_analysis.py

import pyshark

def analyze_packet_capture(file_path):
    print("Analyzing packet capture:", file_path)
    try:
        cap = pyshark.FileCapture(file_path)
        for pkt in cap:
            print(f"Source IP: {pkt.ip.src}, Destination IP: {pkt.ip.dst}, Protocol: {pkt.transport_layer}")
            print("Packet data:", pkt)
    except Exception as e:
        print(f"Error analyzing packet capture: {e}")

if __name__ == "__main__":
    file_path = input("Enter path to the packet capture file (.pcap): ")
    if file_path.lower().endswith(".pcap"):
        analyze_packet_capture(file_path)
    else:
        print("Invalid file format. Please provide a .pcap file.")
