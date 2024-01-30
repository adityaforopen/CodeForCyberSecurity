# botnet_traffic_analyzer.py

import pyshark

def analyze_botnet_traffic(file_path):
    print("Analyzing network traffic for botnet activities:", file_path)
    try:
        cap = pyshark.FileCapture(file_path)
        for pkt in cap:
            # Example: Detecting botnet command and control communication
            # Replace with actual detection logic based on traffic patterns
            if "tcp" in pkt and pkt.tcp.dstport == "6667":
                print("Potential botnet command and control traffic detected:", pkt)
    except Exception as e:
        print(f"Error analyzing botnet traffic: {e}")

if __name__ == "__main__":
    file_path = input("Enter path to the packet capture file (.pcap): ")
    if file_path.lower().endswith(".pcap"):
        analyze_botnet_traffic(file_path)
    else:
        print("Invalid file format. Please provide a .pcap file.")
